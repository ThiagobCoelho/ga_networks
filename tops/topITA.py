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
	itanodes = [\
		(0.70, 6.50),	#0 
		(1.80, 7.00),	#1
		(1.80, 6.00),	#2
		(3.00, 7.70),	#3
		(2.70, 6.80),	#4
		(4.00, 6.70),	#5
		(3.30, 6.30),	#6
		(2.90, 5.70),	#7
		(2.00, 5.00),	#8
		(2.90, 5.00),	#9
		(3.80, 5.20),	#10
		(3.20, 4.50),	#11
		(2.50, 3.50),	#12
		(3.90, 4.00),	#13
		(3.70, 2.50),	#14
		(4.90, 3.00),	#15
		(4.50, 2.00),	#16
		(4.70, 1.00),	#17
		(3.80, 0.50),	#18
		(2.70, 0.60),	#19
		(1.20, 1.50)	#20
	]

	# define links or edges as node index ordered pairs in cartesian plan
	italinks = [\
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
	# draw edges before vertices
	for link in italinks:
		x = [ itanodes[link[0]][0], itanodes[link[1]][0] ]
		y = [ itanodes[link[0]][1], itanodes[link[1]][1] ]
		plt.plot(x, y, 'k--', linewidth=2)

	# draw vertices
	i = 0
	for node in itanodes:
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
#	plt.plot(itanodes[0][0], itanodes[0][1], 'ko', markersize=25, markeredgewidth=3.0)
#	ax.annotate("0", xy=(itanodes[0][0]-corr+0.01, itanodes[0][1]-corr), color='white')
#
#	# highlight destination node
#	plt.plot(itanodes[13][0], itanodes[13][1], 'ko', markersize=25, markeredgewidth=3.0)
#	ax.annotate("13", xy=(itanodes[13][0]-corr, itanodes[13][1]-corr), color='white')

#	# highlight 
#	idx = 0;
#	for bestroute in routes:
#		for i in xrange(len(bestroute)-1):
#			x = [ itanodes[bestroute[i]][0], itanodes[bestroute[i+1]][0] ]
#			y = [ itanodes[bestroute[i]][1], itanodes[bestroute[i+1]][1] ]
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
