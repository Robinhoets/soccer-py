# imports
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.image import NonUniformImage
from matplotlib import cm

# helper definitions
def _is_ndarray(array):
	if type(array) is np.ndarray:
		return True
	else:
		return False

# public definitions

# takes a numpy.ndarray
def heatmap(array):


	try:
		is_ndarry(array)
		print("is ndarray")
	except:
		print("not ndarray")
