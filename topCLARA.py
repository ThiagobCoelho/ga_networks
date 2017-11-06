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
	claranodes = [\
		(2.00, 6.00),#0
		(1.00, 6.00),#1
		(1.00, 4.50),#2
		(1.00, 2.50),#3
		(1.00, 1.00),#4
		(2.00, 1.00),#5
		(1.50, 1.70),#6
		(3.00, 1.00),#7
		(4.00, 1.00),#8
		(5.00, 3.50),#9
		(5.00, 1.00),#10
		(4.00, 6.00),#11
		(5.00, 6.00),#12
	]

	# define links or edges as node index ordered pairs in cartesian plan
	claralinks = [\
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
	# draw edges before vertices
	for link in claralinks:
		x = [ claranodes[link[0]][0], claranodes[link[1]][0] ]
		y = [ claranodes[link[0]][1], claranodes[link[1]][1] ]
		plt.plot(x, y, 'k--', linewidth=2)


	countries = ['US','MX','GT','SV','CR','PN','VE','CO','CL','AR','UY','BR','UK']
	# draw vertices
	i = 0
	for node in claranodes:
		# parameter to adjust text on the center of the vertice

		plt.plot(node[0], node[1], 'wo', markersize=25)
		ax.annotate(countries[i], xy=(node[0]-0.1, node[1]-0.09))

		i += 1

	routes = ([0,5,10,11,13], [0,2,8,9,11,13], [0,5,6,3,13])
	colors = ['red', 'green', 'blue']


#	# highlight source node
#	plt.plot(claranodes[0][0], claranodes[0][1], 'ko', markersize=25, markeredgewidth=3.0)
#	ax.annotate("0", xy=(claranodes[0][0]-corr+0.01, claranodes[0][1]-corr), color='white')

#	# highlight destination node
#	plt.plot(claranodes[13][0], claranodes[13][1], 'ko', markersize=25, markeredgewidth=3.0)
#	ax.annotate("13", xy=(claranodes[13][0]-corr, claranodes[13][1]-corr), color='white')

#	# highlight 
#	idx = 0;
#	for bestroute in routes:
#		for i in xrange(len(bestroute)-1):
#			x = [ claranodes[bestroute[i]][0], claranodes[bestroute[i+1]][0] ]
#			y = [ claranodes[bestroute[i]][1], claranodes[bestroute[i+1]][1] ]
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
