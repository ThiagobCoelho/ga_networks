#!/usr/bin/python

import info
import net

import sys, getopt

import numpy as np
import random 

from rwa_ga import rwa_ga

from rwa_std_fix import rwa_std_fix
from rwa_std_alt import rwa_std_alt

from rwa_alt import rwa_alt
from rwa_fix import rwa_fix

def usage():
	print '\nUsage: python pytest.py -t <topology>\n'
	print '-t, --topology \tChoose the topology for the algorithm'
	print '\n<topology> \tChoose a number:'
	print '\t\t1 - NSF'
	print '\t\t2 - ARPA'
	print '\t\t3 - Italian network'
	print '\t\t4 - RNP'
	print '\t\t5 - CLARA'
	print '\t\t6 - JANET6'

def topology_select(argv):
	try:
		opts, args = getopt.getopt(argv,"ht:",["topology="])
	except getopt.GetoptError:
		usage()
		sys.exit()
	
	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit()
		elif opt in ("-t", "--topology"):
			if int(arg) not in [1,2,3,4,5,6]:
				print '\nError: Not valid topology number.'
				usage()
				sys.exit()
			else:
				return arg
	
	usage()

def get_wave_availability(k, n):
	return (int(n) & ( 1 << k )) >> k

if __name__ == "__main__":
	top = topology_select(sys.argv[1:])
	
	if top is None:
		sys.exit()

	net_wave, net_adj, net_time, net_links, num_channels, num_nodes = net.generate(top)

	if info.DEBUG:
		print net_wave

	# Matrix with nodes X loads for each simulation (info.NUM_SIM) containing
	# the blocking probilities
	blocking_p_ga = np.ones((info.NUM_SIM, num_nodes*info.SIM_MAX_LOAD))
	blocking_p_alt = np.ones((info.NUM_SIM, num_nodes*info.SIM_MAX_LOAD))
	blocking_p_fix = np.ones((info.NUM_SIM, num_nodes*info.SIM_MAX_LOAD))

	for sim in xrange(info.NUM_SIM):
		blocked_ga  = []
		blocked_std_fix = []
		blocked_std_alt = []
		blocked_alt = []
		blocked_fix = []

		# Table with blocked calls, arrived calls and blocking probability
		# for each node with each load
		block_table_ga  = np.zeros((info.SIM_MAX_LOAD, num_nodes, 3))
		block_table_alt = np.zeros((info.SIM_MAX_LOAD, num_nodes, 3))
		block_table_fix = np.zeros((info.SIM_MAX_LOAD, num_nodes, 3))

		for load in xrange(info.SIM_MIN_LOAD, info.SIM_MAX_LOAD):
			N_ga  = net_wave.copy()
			N_std_fix = net_wave.copy()
			N_std_alt = net_wave.copy()
			N_alt = net_wave.copy()
			N_fix = net_wave.copy()

			T_ga  = net_time.copy() # holding time
			T_std_fix = net_time.copy() # holding time
			T_std_alt = net_time.copy() # holding time
			T_alt = net_time.copy() # holding time
			T_fix = net_time.copy() # holding time
		
			paths_fix = []
			paths_alt = []

			count_block_ga  = 0
			count_block_std_fix = 0
			count_block_std_alt = 0
			count_block_alt = 0
			count_block_fix = 0

			for gen in xrange(info.SIM_NUM_GEN):
				S, D = random.sample(range(0,num_nodes),2)

				# increase arrived calls counter for the given source node S
				block_table_ga[load][S][1]  += 1
				block_table_alt[load][S][1] += 1
				block_table_fix[load][S][1] += 1

				# exponential distribution (poisson arrival)
				until_next   = -np.log(1-np.random.rand())/load
				holding_time = -np.log(1-np.random.rand())
		
				# genetic algorithm
				if rwa_ga(N_ga,  net_adj, T_ga,  holding_time, num_nodes, num_channels, S, D):
					block_table_ga[load][S][0] += 1

				# yen + first-fit
				if rwa_alt(N_alt, net_adj, T_alt, holding_time, num_channels, S, D):
					block_table_alt[load][S][0] += 1

				# dijkstra + first-fit
				if rwa_fix(N_fix, net_adj, T_fix, holding_time, num_nodes, S, D):
					block_table_fix[load][S][0] += 1

				#count_block_std_fix += rwa_std_fix(N_std_fix, net_adj, T_std_fix, holding_time, paths_fix)
				#count_block_std_alt += rwa_std_alt(N_std_alt, net_adj, T_std_alt, holding_time, paths_alt)

				if info.DEBUG:
					sys.stdout.write('\rSimul: %04d/%04d ' % (sim+1, info.NUM_SIM))
					sys.stdout.write('Load: %02d/%02d ' % (load, info.SIM_MAX_LOAD-1))
					sys.stdout.write('Gen: %04d/%04d\t' % (gen+1, info.SIM_NUM_GEN))

					sys.stdout.write('Tga:  %04d, ' % block_table_ga[load].sum(0)[0])
					sys.stdout.write('Talt: %04d, ' % block_table_alt[load].sum(0)[0])
					sys.stdout.write('Tfix: %04d '  % block_table_fix[load].sum(0)[0])
#					sys.stdout.write('STF: %04d, ' % count_block_std_fix)
#					sys.stdout.write('STA: %04d, ' % count_block_std_alt)
					sys.stdout.flush()
		
				aux_fix = {idx:[] for idx in xrange(num_channels)}
				aux_alt = {idx:[] for idx in xrange(num_channels)}

				# Atualiza os todos os canais que ainda estao sendo usados 
				for link in net_links:
					i, j = link
					for w in xrange(num_channels):

						# GA + GOF
						if  T_ga[i][j][w] > until_next:
							T_ga[i][j][w] -= until_next
							T_ga[j][i][w]  = T_ga[i][j][w]
						else:
							T_ga[i][j][w] = 0
							T_ga[j][i][w] = 0
							if not get_wave_availability(w, N_ga[i][j]):
								N_ga[i][j] += 2**w # free channel
								N_ga[j][i] = N_ga[i][j] 

						# Dijkstra + Graph coloring
						if  T_std_fix[i][j][w] > until_next:
							T_std_fix[i][j][w] -= until_next
							T_std_fix[j][i][w]  = T_std_fix[i][j][w]
						else:
							T_std_fix[i][j][w] = 0
							T_std_fix[j][i][w] = 0
							if not get_wave_availability(w, N_std_fix[i][j]):
								N_std_fix[i][j] += 2**w # free channel
								N_std_fix[j][i] = N_std_fix[i][j] 
								aux_fix[w].append((i,j))
								aux_fix[w].append((j,i))

						# Yen + Graph coloring
						if  T_std_alt[i][j][w] > until_next:
							T_std_alt[i][j][w] -= until_next
							T_std_alt[j][i][w]  = T_std_alt[i][j][w]
						else:
							T_std_alt[i][j][w] = 0
							T_std_alt[j][i][w] = 0
							if not get_wave_availability(w, N_std_alt[i][j]):
								N_std_alt[i][j] += 2**w # free channel
								N_std_alt[j][i] = N_std_alt[i][j] 
								aux_alt[w].append((i,j))
								aux_alt[w].append((j,i))

						# Yen + First-fit
						if  T_alt[i][j][w] > until_next:
							T_alt[i][j][w] -= until_next
							T_alt[j][i][w]  = T_alt[i][j][w]
						else:
							T_alt[i][j][w] = 0
							T_alt[j][i][w] = 0
							if not get_wave_availability(w, N_alt[i][j]):
								N_alt[i][j] += 2**w # free channel
								N_alt[j][i] = N_alt[i][j] 

						# Dijkstra + First-fit
						if  T_fix[i][j][w] > until_next:
							T_fix[i][j][w] -= until_next
							T_fix[j][i][w]  = T_fix[i][j][w]
						else:
							T_fix[i][j][w] = 0
							T_fix[j][i][w] = 0
							if not get_wave_availability(w, N_fix[i][j]):
								N_fix[i][j] += 2**w # free channel
								N_fix[j][i] = N_fix[i][j] 

				pop_fix = []
				for path in paths_fix:
					R, color = path
					count = 0
					if color == None:
						continue
					for r in xrange(len(R)-1):
						rcurr = R[r]
						rnext = R[r+1]
						if (rcurr,rnext) in aux_fix[color]:
							count += 1
					if count == len(R)-1:
						pop_fix.append(paths_fix.index(path))

				pop_fix.sort() # make sure the last elements are popped first
				while len(pop_fix):
					paths_fix.pop(pop_fix.pop())

				pop_alt = []
				for path in paths_alt:
					R, color = path
					count = 0
					if color == None:
						continue
					for r in xrange(len(R)-1):
						rcurr = R[r]
						rnext = R[r+1]
						if (rcurr,rnext) in aux_alt[color]:
							count += 1
					if count == len(R)-1:
						pop_alt.append(paths_alt.index(path))

				pop_alt.sort() # make sure the last elements are popped first
				while len(pop_alt):
					paths_alt.pop(pop_alt.pop())

		# Initialize Erlang 0 as 1, because there's no Erlang 0 (warning)
		block_table_ga[0] = block_table_alt[0] = block_table_fix[0] = 1

		# Divide all blocks in source for its respective number of arrived calls
		# BT[?][?][2] = BT[?][?][0] / BT[?][?][1]
		block_table_ga[...,2]  = block_table_ga[...,0]/block_table_ga[...,1]
		block_table_alt[...,2] = block_table_alt[...,0]/block_table_alt[...,1]
		block_table_fix[...,2] = block_table_fix[...,0]/block_table_fix[...,1]

		# Gets all blocking probabilities and reshapes into array
		blocking_p_ga[sim] = block_table_ga[...,2].reshape(info.SIM_MAX_LOAD*num_nodes)
		blocking_p_alt[sim] = block_table_alt[...,2].reshape(info.SIM_MAX_LOAD*num_nodes)
		blocking_p_fix[sim] = block_table_fix[...,2].reshape(info.SIM_MAX_LOAD*num_nodes)

		#if info.DEBUG:
		#	print '\tGA:  ', blocked_ga
		#	print '\tSTF: ', blocked_std_fix
		#	print '\tSTA: ', blocked_std_alt
		#	print '\tALT: ', blocked_alt
		#	print '\tFIX: ', blocked_fix

		#with open('TESTE_{}.m'.format(top), 'a') as f:
		#	text = str(block_table_ga[:].reshape(info.SIM_MAX_LOAD,num_nodes,3))
		#	f.write('%s; ...\n' % text)
		#

	# Final probability gets the mean for each load in each node for N simulations
	# and reshapes into matrix for better understanding
	final_p_ga = blocking_p_ga.mean(axis=0).reshape(info.SIM_MAX_LOAD,num_nodes)*100
	with open('blocks_ga_top_{}.m'.format(top), 'a') as f:
		text = str(np.around(final_p_ga,4))
		f.write('%s; ...\n' % text)

	final_p_alt = blocking_p_alt.mean(axis=0).reshape(info.SIM_MAX_LOAD,num_nodes)*100
	with open('blocks_alt_top_{}.m'.format(top), 'a') as f:
		text = str(np.around(final_p_alt,4))
		f.write('%s; ...\n' % text)

	final_p_fix = blocking_p_fix.mean(axis=0).reshape(info.SIM_MAX_LOAD,num_nodes)*100
	with open('blocks_fix_top_{}.m'.format(top), 'a') as f:
		text = str(np.around(final_p_fix,4))
		f.write('%s; ...\n' % text)

### EOF ###
