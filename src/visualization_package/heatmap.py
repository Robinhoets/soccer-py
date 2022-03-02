# imports
import sys
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.image import NonUniformImage
from matplotlib import cm

# helper definitions
def _create_histogram(array):
	x, y = array[:,1], array[:,2]
	heatmap, xedges, yedges = np.histogram2d(x, y, bins=50, range=[[0, 105], [0, 68]])

def _is_ndarray(array):
	print(type(array))
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