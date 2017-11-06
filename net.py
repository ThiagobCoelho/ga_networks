#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8
#
# GA: RWA with GOF
# Genetic Algorithm
# Routing and Wavelength Assignment
# General Objective Function
#
# Copyright 2017
# Programa de Pós-Graduação em Ciência da Computação (PPGCC)
# Universidade Federal do Pará (UFPA)
#
# Author: April 2016
# Cassio Trindade Batista - cassio.batista.13@gmail.com
#
# Last revised on February 2017


import sys
reload(sys)  
sys.setdefaultencoding('utf8') # for plot in PT_BR

import info
import random
import numpy as np

def generate(top):
	def NSF():
		print 'Chosen topology: NSF'
		num_channels = info.NSF_NUM_CHANNELS
		num_nodes = info.NSF_NUM_NODES

		nsf_links = [\
			(0,1), (0,2), (0,5),	# 0
			(1,2), (1,3),			# 1
			(2,8),					# 2
			(3,4), (3,6), (3,13),	# 3
			(4,9),					# 4
			(5,6), (5,10),			# 5
			(6,7),					# 6
			(7,8),					# 7
			(8,9),					# 8
			(9,11), (9,12),			# 9
			(10,11), (10,12),		# 10
			(11,13)					# 11
		]
		return nsf_links, num_nodes, num_channels

	def RNP():
		print 'Chosen topology: RNP'
		num_channels = info.RNP_NUM_CHANNELS
		num_nodes = info.RNP_NUM_NODES
		rnp_links = [\
			(0,1),									# 0
			(1,3), (1,4),							# 1
			(2,4),									# 2
			(3,4), (3,7), (3,17), (3,19), (3,25), 	# 3
			(4,6), (4,12),							# 4
			(5,25),									# 5
			(6,7),									# 6
			(7,8), (7,11), (7,18), (7,19),			# 7
			(8,9),									# 8
			(9,10),									# 9
			(10,11),								# 10
			(11,12), (11,13), (11,15),				# 11
			(13,14),								# 13
			(14,15),								# 14
			(15,16), (15,19),						# 15
			(16,17),								# 16
			(17,18),								# 17
			(18,19), (18,20), (18,22),				# 18
			(20,21),								# 20
			(21,22),								# 21
			(22,23),								# 22
			(23,24),								# 23
			(24,25), (24,26),						# 24
			(26,27)									# 26
		]
		return rnp_links, num_nodes, num_channels

	def ARPA():
		print 'Chosen topology: ARPA'
		num_channels = info.ARPA_NUM_CHANNELS
		num_nodes = info.ARPA_NUM_NODES
		arpa_links = [\
			(0,1), (0,2), (0,19),		# 0
			(1,2), (1,3),				# 1
			(2,4),						# 2
			(3,4), (3,5),				# 3
			(4,6),						# 4
			(5,6), (5,7),				# 5
			(6,9),						# 6
			(7,8), (7,9), (7,10),		# 7
			(8,9), (8,19),				# 8
			(9,15),						# 9
			(10,11), (10,12),			# 10
			(11,12),					# 11
			(12,13),					# 12
			(13,14), (13,16),			# 13
			(14,15), 					# 14
			(15,17), (15,18),			# 15
			(16,17), (16,19),			# 16
			(17,18)						# 17
			# (18,15), (18,17)			# 18
			# (19,16), (19,0)			# 19
		]
		return arpa_links, num_nodes, num_channels

	def ITA():
		print 'Chosen topology: ITA'
		num_channels = info.ITA_NUM_CHANNELS
		num_nodes = info.ITA_NUM_NODES
		ita_links = [\
			(0,1), (0,2),							# 0
			(1,2), (1,3), (1,4),					# 1
			(2,7), (2,8), (2,9),					# 2
			(3,4), (3,5), 							# 3
			(4,6), (4,7),							# 4
			(5,6),									# 5
			(6,7),									# 6
			(7,9), (7,10),							# 7
			(8,9), (8,12),							# 8
			(9,11), (9,12),							# 9
			(10,13),								# 10
			(11,12), (11,13),						# 11
			(12,14), (12,20),						# 12
			(13,14), (13,15),						# 13
			(14,15), (14,16), (14,18), (14,19),		# 14
			(15,16),								# 15
			(16,17),								# 16
			(17,18),								# 17
			(18,19),								# 18
			(19,20)									# 19
			#(20,12)								# 20
		]
		return ita_links, num_nodes, num_channels
		
	def CLARA():
		print 'Chosen topology: CLARA'
		num_channels = info.CLARA_NUM_CHANNELS
		num_nodes = info.CLARA_NUM_NODES
		#CLARA topology 2017
		clara_links = [\
			(0,1), (0,5), (0,8), (0,11),						#0
			(1,2),												#1
			(2,3),												#2
			(3,4),												#3
			(4,5),												#4
			(5,6), (5,7), (5,11),								#5
			(7,8),												#7
			(8,9), (8,11),										#8
			(9,10), (9,11),										#9
			(11,12)												#11
		]
		return clara_links, num_nodes, num_channel

	def set_wave_availability(nc):
		nwaves = 2**nc
		if info.NSF_CHANNEL_FREE:
			return np.uint8(nwaves-1)
		return np.uint8(random.randrange(1, nwaves))

	topology = { '1': NSF, '2': ARPA, '3': ITA, '4': RNP }
	net_links, num_nodes, num_channels = topology[top]()
	
	net_wave = np.zeros((num_nodes, num_nodes), dtype=np.uint8)
	for link in net_links:
		net_wave[link[0]][link[1]] = set_wave_availability(num_channels) 
		net_wave[link[1]][link[0]] = net_wave[link[0]][link[1]] 

	net_adj = np.zeros((num_nodes, num_nodes), dtype=np.uint8)
	for link in net_links:
		net_adj[link[0]][link[1]] = 1
		net_adj[link[1]][link[0]] = net_adj[link[0]][link[1]] 

	net_time = np.zeros((num_nodes, num_nodes, num_channels))
	for link in net_links:
		availability = format(net_wave[link[0]][link[1]], '0%db' % num_channels)
		for w in xrange(num_channels):
			net_time[link[0]][link[1]][w] = int(availability[w]) * np.random.rand()
			net_time[link[1]][link[0]][w] = net_time[link[0]][link[1]][w]

	return net_wave, net_adj, net_time, net_links, num_channels 

