# imports
import sys
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.image import NonUniformImage
from matplotlib import cm

################################################
### Field variables 
X_SIZE = 105.0
Y_SIZE = 68.0

BOX_HEIGHT = ((16.5*2 + 7.32)/Y_SIZE*100)/1.3
BOX_WIDTH = 16.5/X_SIZE*100

GOAL = 7.32/Y_SIZE*100

GOAL_AREA_HEIGHT = 5.4864*2/Y_SIZE*100 + GOAL
GOAL_AREA_WIDTH = 5.4864/X_SIZE*100
################################################

def save_png(plt):
	name = 'heatmap'
	plt.savefig(name + ".png")

def draw_patches(axes):
		plt.xlim([0,100])
		plt.ylim([0,68])

		#half-way line
		axes.add_line(plt.Line2D([50, 50], [100, 0],
										c='w'))
		
		#penalty areas
		axes.add_patch(plt.Rectangle((100-BOX_WIDTH, (70-BOX_HEIGHT)/2),  BOX_WIDTH, BOX_HEIGHT,
											 ec='w', fc='none'))
		axes.add_patch(plt.Rectangle((0, (70-BOX_HEIGHT)/2),  BOX_WIDTH, BOX_HEIGHT,
															 ec='w', fc='none'))                       
		
		#goal areas
		axes.add_patch(plt.Rectangle((100-GOAL_AREA_WIDTH, (73-GOAL_AREA_HEIGHT)/2),  GOAL_AREA_WIDTH, GOAL_AREA_HEIGHT,
											 ec='w', fc='none'))
		axes.add_patch(plt.Rectangle((0, (73-GOAL_AREA_HEIGHT)/2),  GOAL_AREA_WIDTH, GOAL_AREA_HEIGHT,
															 ec='w', fc='none'))                       
		#halfway circle
		axes.add_patch(Ellipse((50, 35), 2*9.15/X_SIZE*100, 2*9.15/Y_SIZE*100,
																		ec='w', fc='none'))

		return axes

# helper definitions
def _create_histogram(array):
	x, y = array[:,1], array[:,2]
	heatmap, xedges, yedges = np.histogram2d(x, y, bins=50, range=[[0, 105], [0, 68]])
	heatmap = heatmap.T
	fig = plt.figure(figsize=(X_SIZE/15, Y_SIZE/15))
	axes = fig.add_subplot(1, 1, 1)
	im = NonUniformImage(axes, interpolation='bilinear',cmap='gnuplot')
	xcenters = (xedges[:-1] + xedges[1:]) / 2
	ycenters = (yedges[:-1] + yedges[1:]) / 2
	im.set_data(xcenters, ycenters,heatmap)
	axes.images.append(im)
	axes = draw_patches(axes)
	plt.axis('off')
	# plt.text(80, 60, total_distance, fontsize = 22,color = 'white')
	# plt.savefig(str(value) + ".png")
	save_png(plt)

def _is_ndarray(array):
	if type(array) is np.ndarray:
		return True
	else:
		return False

# public definitions

# takes a numpy.ndarray
def heatmap(array):
	try:
		ndarray = _is_ndarray(array)
		if(ndarray):
			pass
		else:
			raise ValueError()
	except ValueError:
		print("not ndarray")
		sys.exit()

	_create_histogram(array)











