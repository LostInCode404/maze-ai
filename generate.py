# Import libraries
from __future__ import print_function 
import numpy as np
import math
from random import shuffle
from random import randint

# Import project modules
from plot import grid_states as states
from util import can_be_removed


# Method to generate maze
def generate_maze(x,y):

	# Print begin message
	print("Generating maze... ",end='')

	# Initialize x and y
	x=int(x+1)/2
	y=int(y+1)/2

	# Initialize variables for backtracking
	visited=np.zeros(shape=(x,y))
	parent_x=-1*np.ones(shape=(x,y))
	parent_y=-1*np.ones(shape=(x,y))

	# Current cell
	cx=0
	cy=0

	# Loop till all cells are not visited
	while True:

		# Get next possible random move
		nx,ny=get_moves(visited,cx,cy,x-1,y-1)

		# Reached end, need to backtrack
		if(nx==-1 or ny==-1):
			cx=int(cx)
			cy=int(cy)
			visited[cx][cy]=1
			ncx=parent_x[cx][cy]
			ncy=parent_y[cx][cy]
			cx=ncx
			cy=ncy
			cx=int(cx)
			cy=int(cy)

		# Move to next cell
		else:
			cx=int(cx)
			cy=int(cy)
			parent_x[nx][ny]=cx
			parent_y[nx][ny]=cy
			visited[cx][cy]=1
			cx=nx
			cy=ny
			cx=int(cx)
			cy=int(cy)

		if(cx==0 and cy==0):
			print("Done")
			break

	# Convert to required format
	return convert_to_maze_format(visited,parent_x,parent_y)


# Get all possible directions for maze generator
def get_moves(visited,x,y,x_lim,y_lim):

	# Randomly choose move
	what_to_try=['up','down','right','left']
	shuffle(what_to_try)

	# Just in case
	x=int(x)
	y=int(y)

	# Try different moves if possible
	for direction in what_to_try:
		if(direction=='up'):
			if(y>0 and visited[x][y-1]==0):
				return x,y-1
		elif(direction=='down'):
			if(y<y_lim and visited[x][y+1]==0):
				return x,y+1
		elif(direction=='left'):
			if(x>0 and visited[x-1][y]==0):
				return x-1,y
		elif(direction=='right'):
			if(x<x_lim and visited[x+1][y]==0):
				return x+1,y
	
	# Need to backtrack
	return (-1,-1)


# Convert to different grid format for caclulations and plotting
def convert_to_maze_format(grid,parent_x,parent_y):

	# Print begin message
	print("Converting to required format... ",end='')

	# New grid to store values
	newgrid=np.zeros(shape=(grid.shape[0]*2-1,grid.shape[1]*2-1))
	newgrid[0][0]=states['START']

	# Generate new grid
	for i in range(grid.shape[0]):
		for j in range(grid.shape[1]):
			if(i!=0 or j!=0):
				newgrid[i*2][j*2]=states['EMPTY']
				xdif=i-parent_x[i][j]
				ydif=j-parent_y[i][j]
				newgrid[int(i*2-xdif)][int(j*2-ydif)]=states['EMPTY']

	# Randomly clear some boxes so that it is not a perfect maze
	box_size=20
	boxes_x=int(newgrid.shape[0]/box_size)
	boxes_y=int(newgrid.shape[1]/box_size)
	for i in range(boxes_x):
		for j in range(boxes_y):
			done=False
			while(not done):
				index_x=randint(0,box_size-1)
				index_y=randint(0,box_size-1)
				if(newgrid[i*box_size+index_x][j*box_size+index_y]!=states['EMPTY']):
					if(can_be_removed(i*box_size+index_x,j*box_size+index_y,newgrid)):
						newgrid[i*box_size+index_x][j*box_size+index_y]=states['EMPTY']
						done=True



	# Set last tile as goal
	newgrid[grid.shape[0]*2-2][grid.shape[1]*2-2]=states['GOAL']

	# Done
	print("Done")

	# Return the generated grid
	return newgrid
