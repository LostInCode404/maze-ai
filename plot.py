# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import math
import warnings

# Supress warnings from matplotlib
warnings.filterwarnings("ignore")

# Mapping of number to states of a grid cell
grid_states={
	'WALL':0,
	'EMPTY':1,
	'PATH':2,
	'START':3,
	'GOAL':4
}
color_mapper=[
	(0.1,0.1,0.1),
	(0.6,0.6,0.6),
	(0,0.8,1),
	(1,0,0),
	(0,1,0)
]

# Method to plot based one the above given mappings
def plot_maze(grid,save=False,full=False):
	
	# Initialize variables and plot parameters
	x=[]
	y=[]
	color=[]
	for i in range(grid.shape[0]):
		for j in range(grid.shape[1]):
			x.append(j+1)
			y.append(grid.shape[1]-i)
			color.append(color_mapper[int(grid[i][j])])

	# Configure grid
	grid_const=400
	if(full):
		grid_const=550
	fig,axes=plt.subplots(1,1)
	axes.scatter(x,y,math.pow(grid_const/max(grid.shape[0],grid.shape[1]),2),color,marker="s")
	axes.set_aspect('equal','box')
	fig.tight_layout()
	plt.ylim((0,grid.shape[1]+1))
	plt.xlim((0,grid.shape[0]+1))
	plt.axis('off')
	
	# If plot needs saving
	if(save):
		fig.savefig(save)

	# If full screen required
	if(full):
		mng = plt.get_current_fig_manager()
		mng.resize(*mng.window.maxsize())

	# Show plot
	plt.show()
