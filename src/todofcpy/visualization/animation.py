from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.patches import ConnectionPatch, Arc

from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

from matplotlib.image import NonUniformImage

import numpy as np
import pandas as pd

def _create_histogram(self,ax):
    """
    Returns a matplotlib.pyplot with histogram2d & NonUniformImage added.

    Parameters
    ----------
    self (self.data)
    ax = fig.subplot
    """

    array = self.data
    x = array['x_pos'].to_numpy()
    y = array['y_pos'].to_numpy()

    if 'color' in self.__dict__:
        color = self.color
        print(color)
    else:
        color = 'gnuplot'

    # x, y = array[:,0], array[:,1]
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=50, range=[[0, 105], [0, 68]])
    heatmap = heatmap.T
    im = NonUniformImage(ax, interpolation='bilinear', cmap=color)
    xcenters = (xedges[:-1] + xedges[1:]) / 2
    ycenters = (yedges[:-1] + yedges[1:]) / 2
    im.set_data(xcenters, ycenters,heatmap)
    ax.images.append(im)

    return plt

def _draw_pitch(ax):
    # focus on only half of the pitch
    #Pitch Outline & Centre Line
    Pitch = plt.Rectangle([0,0], width = 120, height = 80,color="white", fill = False)
    #Left, Right Penalty Area and midline
    LeftPenalty = plt.Rectangle([0,22.3], width = 14.6, height = 35.3, color="white",fill = False)
    RightPenalty = plt.Rectangle([105.4,22.3], width = 14.6, height = 35.3, color="white",fill = False)
    midline = ConnectionPatch([60,0], [60,80], "data", "data",color="white")

    #Left, Right 6-yard Box
    LeftSixYard = plt.Rectangle([0,32], width = 4.9, height = 16, color="white",fill = False)
    RightSixYard = plt.Rectangle([115.1,32], width = 4.9, height = 16, color="white",fill = False)

    #Prepare Circles
    centreCircle = plt.Circle((60,40),8.1,color="white", fill = False)
    centreSpot = plt.Circle((60,40),0.71,color="white")
    #Penalty spots and Arcs around penalty boxes
    leftPenSpot = plt.Circle((9.7,40),0.71,color="white")
    rightPenSpot = plt.Circle((110.3,40),0.71,color="white")
    leftArc = Arc((9.7,40),height=16.2,width=16.2,angle=0,theta1=310,theta2=50,color="white")
    rightArc = Arc((110.3,40),height=16.2,width=16.2,angle=0,theta1=130,theta2=230,color="white")

    element = [Pitch, LeftPenalty, RightPenalty, midline, LeftSixYard, RightSixYard, centreCircle,
               centreSpot, rightPenSpot, leftPenSpot, leftArc, rightArc]
    for i in element:
        ax.add_patch(i)

def _create_frame(t,self):
    data = self.data
    heatmap = self.heatmap
    fig=plt.figure()
    fig.set_size_inches(7, 5)
    ax=fig.add_subplot(1,1,1)
    fig.set_facecolor('black')
    _draw_pitch(ax)
    plt.ylim(-2, 82)
    plt.xlim(-2, 122)
    plt.axis('off')

    if(heatmap=='on'):
        _create_histogram(self,ax)

    if 'player_color' in self.__dict__:
        player_color = self.player_color
    else:
        player_color = gray

    f = int(t*20)
    data = data.loc[f]
    ax.add_artist(Ellipse((data['x_pos'],
					        data['y_pos']),
							2/105*100, 2/68*100,
							edgecolor='white',
							linewidth=2,
							facecolor=player_color,
							alpha=1,
							zorder=20))

    return fig, ax, data

def _create_dataframe(self,kwargs):
    array = kwargs['data']
    self.__dict__['data'] = pd.DataFrame({'x_pos': array[:, 0], 'y_pos': array[:, 1]})

class Animation:
    def __init__(self,**kwargs):
		"""
		Set's Animations variables.

		Kwargs:
           data (np.ndarray): 2d array of length 2.
		   color (Matplotlib.cm): (optional) Matplotlib.cm, ['viridis', 'plasma', 'inferno', 'magma', 'cividis'].
           duration (int): Number of secods desired for clip.
           player_color (rgba,string): Color for desired player to be.

		"""

        self.__dict__.update(kwargs)
        _create_dataframe(self,kwargs)

    def animate(self):
        # default duration is 30 seconds
        if self.__dict__['duration']:
            duration = self.duration
        else:
            duration = 30

        animation = VideoClip(lambda x: mplfig_to_npimage(_create_frame(x,self)[0]),duration=duration)
        animation.to_videofile("pc.mp4", fps=20)
