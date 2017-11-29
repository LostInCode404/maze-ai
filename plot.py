# Import libraries
from __future__ import print_function 
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
	'GOAL':4,
	'NODE':5
}

# Map colors to different states
color_mapper=[
	(0.1,0.1,0.1),
	(0.6,0.6,0.6),
	(0,0.8,1),
	(1,0,0),
	(0,1,0),
	(0,0,1)
]

# Method to plot based one the above given mappings
def plot_maze(grid,save=False,full=False,show=False,show_progress=False):

	# Print init message
	if(show_progress):
		print("Creating maze image... ",end='')
	
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
	grid_const=800
	fig,axes=plt.subplots(1,1,figsize=(10,10))
	axes.scatter(x,y,math.pow(grid_const/max(grid.shape[0],grid.shape[1]),2),color,marker="s",lw=0.05)
	axes.set_aspect('equal','box')
	fig.tight_layout()
	plt.ylim((0,grid.shape[1]+1))
	plt.xlim((0,grid.shape[0]+1))
	plt.axis('off')
	if(show_progress):
		print("Done")
	
	# If plot needs saving
	if(save):
		if(show_progress):
			print("Saving maze image... ",end='')
		fig.savefig(save+'.png',dpi=200)
		if(show_progress):
			print("Done")

	# If full screen required
	if(full):
		mng = plt.get_current_fig_manager()
		mng.resize(*mng.window.maxsize())

	# Show plot
	if(show):
		if(show_progress):
			print("Showing maze image... ",end='')
		plt.show()
		if(show_progress):
			print("Done")	
