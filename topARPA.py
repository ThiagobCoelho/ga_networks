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
	arpanodes = [\
		(1.80, 5.70),
		(2.80, 5.00),
		(3.40, 6.30),
		(3.40, 5.50),
		(4.50, 5.60),
		(4.70, 4.60),
		(5.30, 4.80),
		(3.60, 4.40),
		(2.20, 4.00),
		(4.80, 3.50),
		(2.40, 2.60),
		(2.50, 1.50),
		(1.40, 2.30),
		(1.80, 3.20),
		(3.70, 2.70),
		(5.20, 2.50),
		(0.80, 3.90),
		(1.20, 0.50),
		(3.60, 0.80),
		(0.80, 5.50)
	]

	# define links or edges as node index ordered pairs in cartesian plan
	arpalinks = [\
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
	# draw edges before vertices
	for link in arpalinks:
		x = [ arpanodes[link[0]][0], arpanodes[link[1]][0] ]
		y = [ arpanodes[link[0]][1], arpanodes[link[1]][1] ]
		plt.plot(x, y, 'k--', linewidth=2)

	# draw vertices
	i = 0
	for node in arpanodes:
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
#	plt.plot(arpanodes[0][0], arpanodes[0][1], 'ko', markersize=25, markeredgewidth=3.0)
#	ax.annotate("0", xy=(arpanodes[0][0]-corr+0.01, arpanodes[0][1]-corr), color='white')

#	# highlight destination node
#	plt.plot(arpanodes[13][0], arpanodes[13][1], 'ko', markersize=25, markeredgewidth=3.0)
#	ax.annotate("13", xy=(arpanodes[13][0]-corr, arpanodes[13][1]-corr), color='white')

#	# highlight 
#	idx = 0;
#	for bestroute in routes:
#		for i in xrange(len(bestroute)-1):
#			x = [ arpanodes[bestroute[i]][0], arpanodes[bestroute[i+1]][0] ]
#			y = [ arpanodes[bestroute[i]][1], arpanodes[bestroute[i+1]][1] ]
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
