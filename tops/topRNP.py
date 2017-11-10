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
	rnpnodes = [\
		(5.00, 3.25),	#0 
		(5.50, 3.75),	#1
		(8.25, 3.75),	#2
		(4.00, 5.00),	#3
		(9.00, 3.00),	#4
		(3.00, 3.00),	#5
		(9.00, 4.00),	#6
		(9.50, 5.00),	#7
		(10.50, 5.00),	#8
		(10.50, 3.00),	#9
		(10.50, 1.00),	#10
		(9.50, 1.00),	#11
		(9.00, 2.00),	#12
		(8.00, 2.00),	#13
		(7.00, 2.00),	#14
		(6.00, 2.00),	#15
		(6.00, 1.00),	#16
		(4.00, 1.00),	#17
		(2.00, 1.00),	#18
		(6.00, 5.50),	#19
		(1.00, 1.00),	#20
		(1.00, 2.00),	#21
		(2.00, 2.00),	#22
		(2.00, 4.00),	#23
		(2.00, 5.00),	#24
		(3.00, 5.00),	#25
		(1.00, 5.00),	#26
		(1.00, 4.00)	#27
	]

	# define links or edges as node index ordered pairs in cartesian plan
	rnplinks = [\
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
	for link in rnplinks:
		x = [ rnpnodes[link[0]][0], rnpnodes[link[1]][0] ]
		y = [ rnpnodes[link[0]][1], rnpnodes[link[1]][1] ]
		plt.plot(x, y, 'k--', linewidth=2)

	states = ['RR','AM','AP','DF','PA','TO','MA','CE','RN','PB',
				'PB','PE','PI','AL','SE','BA','ES','RJ','SP','MG',
					'SC','RS','PR','MS','MT','GO','RO','AC']
	# draw vertices
	i = 0
	for node in rnpnodes:

		plt.plot(node[0], node[1], 'wo', markersize=25)
		ax.annotate(states[i], xy=(node[0]-0.19, node[1]-0.09))

		i += 1

	routes = ([0,5,10,11,13], [0,2,8,9,11,13], [0,5,6,3,13])
	colors = ['red', 'green', 'blue']


#	# highlight source node
#	plt.plot(rnpnodes[0][0], rnpnodes[0][1], 'ko', markersize=25, markeredgewidth=3.0)
#	ax.annotate("0", xy=(rnpnodes[0][0]-corr+0.01, rnpnodes[0][1]-corr), color='white')
#
#	# highlight destination node
#	plt.plot(rnpnodes[13][0], rnpnodes[13][1], 'ko', markersize=25, markeredgewidth=3.0)
#	ax.annotate("13", xy=(rnpnodes[13][0]-corr, rnpnodes[13][1]-corr), color='white')

#	# highlight 
#	idx = 0;
#	for bestroute in routes:
#		for i in xrange(len(bestroute)-1):
#			x = [ rnpnodes[bestroute[i]][0], rnpnodes[bestroute[i+1]][0] ]
#			y = [ rnpnodes[bestroute[i]][1], rnpnodes[bestroute[i+1]][1] ]
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

	plt.xticks(np.arange(0, 12, 1))
	plt.yticks(np.arange(0, 7, 1))
	plt.show(block=False)

if __name__=='__main__':
	plot_graph()
	raw_input('Press enter')
