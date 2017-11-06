import sys
reload(sys)  
sys.setdefaultencoding('utf8') # for plot in PT_BR

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib.ticker import EngFormatter

def plot_graph():
	fig = plt.figure()
	ax = fig.add_subplot(111)

	# define vertices or nodes as points in 2D cartesian plan
	nsfnodes = [\
		(1.10, 8.00),	#0 
		(2.00, 7.00),	#1
		(2.90, 7.50),	#2
		(3.50, 4.50),	#3
		(3.60, 7.20),	#4
		(2.80, 5.00),	#5
		(4.70, 7.00),	#6
		(5.70, 6.60),	#7
		(6.20, 6.10),	#8
		(6.30, 5.70),	#9
		(5.30, 5.70),	#10
		(6.10, 5.20),	#11
		(3.90, 6.30),	#12
		(5.80, 4.50),	#13
		(5.30, 4.00),	#14
		(4.80, 3.50),	#15
		(4.20, 2.70),	#16
		(4.00, 2.10),	#17
		(3.20, 2.10),	#18
		(3.80, 3.20),	#19
		(2.90, 1.20),	#20
		(1.70, 0.60),	#21
		(2.10, 1.90),	#22
		(1.30, 3.00),	#23
		(1.80, 4.30),	#24
		(2.60, 3.50),	#25
		(1.10, 5.00),	#26
		(0.50, 5.00)	#27
	]

	# define links or edges as node index ordered pairs in cartesian plan
	nsflinks = [\
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
	# draw edges before vertices
	for link in nsflinks:
		x = [ nsfnodes[link[0]][0], nsfnodes[link[1]][0] ]
		y = [ nsfnodes[link[0]][1], nsfnodes[link[1]][1] ]
		plt.plot(x, y, 'k-', linewidth=2)

	# draw vertices
	i = 0
	for node in nsfnodes:
		# parameter to adjust text on the center of the vertice
		if i < 10:
			corr = 0.060
		else:
			corr = 0.085

		plt.plot(node[0], node[1], 'wo', markersize=25)
		ax.annotate(str(i), xy=(node[0]-corr, node[1]-corr))

		i += 1

	routes = ([0,5,10,11,13], [0,2,8,9,11,13], [0,5,6,3,13])
	colors = ['red', 'green', 'blue']


#	# highlight source node
#	plt.plot(nsfnodes[0][0], nsfnodes[0][1], 'ko', markersize=25, markeredgewidth=3.0)
#	ax.annotate("0", xy=(nsfnodes[0][0]-corr+0.01, nsfnodes[0][1]-corr), color='white')
#
#	# highlight destination node
#	plt.plot(nsfnodes[13][0], nsfnodes[13][1], 'ko', markersize=25, markeredgewidth=3.0)
#	ax.annotate("13", xy=(nsfnodes[13][0]-corr, nsfnodes[13][1]-corr), color='white')

#	# highlight 
#	idx = 0;
#	for bestroute in routes:
#		for i in xrange(len(bestroute)-1):
#			x = [ nsfnodes[bestroute[i]][0], nsfnodes[bestroute[i+1]][0] ]
#			y = [ nsfnodes[bestroute[i]][1], nsfnodes[bestroute[i+1]][1] ]
#			if i == len(bestroute)-2:
#				include_head = True
#				head_length = 0.3
#				head_width = 0.2
#			else:
#				include_head = False
#				head_length = 0
#				head_width = 0
#
#			if idx == 0:
#				myX = x[0]-x[0]*0.01
#				myY = y[0]-y[0]*0.01
#			elif idx == 1:
#				myX = x[0]#+x[0]*0.0075
#				myY = y[0]#+y[0]*0.0075
#			elif idx == 2:
#				myX = x[0]+x[0]*0.01
#				myY = y[0]+y[0]*0.01
#			else:
#				pass
#
#			plt.arrow(myX, myY, 
#						(x[1]-x[0])-(x[1]-x[0])*0.05, (y[1]-y[0])-(y[1]-y[0])*0.05,
#						length_includes_head=include_head,
#						width=0.04, head_width=head_width, head_length=head_length,
#						fc=colors[idx], ec=colors[idx])
#		idx += 1

	plt.xticks(np.arange(0, 7, 1))
	plt.yticks(np.arange(0, 8, 1))
	plt.show(block=False)

if __name__=='__main__':
	plot_graph()
	raw_input('Press enter')
