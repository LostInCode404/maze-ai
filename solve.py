# Import libraries
from __future__ import print_function 
import numpy as np
import math
import sys

# Import project modules
from plot import grid_states as states
from util import *

# Main Solve maze method
def solve_maze(grid,start,end):

	# Print init
	print("Input grid received for solving...")
	print("Size:  "+str(grid.shape[0])+"x"+str(grid.shape[1]))
	print("Start: ("+str(start[0]+1)+","+str(start[1]+1)+")")
	print("End:   ("+str(end[0]+1)+","+str(end[1]+1)+")")
	print("Solving... ",end='')

	# Optimize to grid to a graph by drastically reducing nodes
	optimize_to_graph(grid)

	# Return modified grid
	print("Done")
	return grid


# Method to optimize path finding
def optimize_to_graph(grid):

	# Initialize variables
	visited=np.zeros(shape=(grid.shape[0],grid.shape[1]))
	
	# Explore all grid cells to generate graph nodes
	explore(0,0,grid,None,visited,[])


# Explore all
def explore(x,y,grid,prev,visited,edge):

	# Exit recursion if visiting a already visited node
	if(visited[x][y]==1):
		return

	# Bools to check possible movement
	possibilities={
		'left':False,
		'right':False,
		'up':False,
		'down':False
	}

	# Bools to check repeated nodes
	nodes={
		'left':False,
		'right':False,
		'up':False,
		'down':False
	}

	# Next positions
	next_positions={
		'left':(-1,-1),
		'right':(-1,-1),
		'up':(-1,-1),
		'down':(-1,-1)
	}

	# Where not to move
	not_to_move={
		'left':'right',
		'right':'left',
		'up':'down',
		'down':'up'
	}

	# Total neighbour count
	counter=0

	# Total walls counter
	wall_counter=0

	# Total visited nodes counter
	node_counter=0
	ndir=(-1,-1)
	ndir_name=None

	# Get next cells
	next_left=left_cell(x,y,grid)
	next_right=right_cell(x,y,grid)
	next_up=up_cell(x,y,grid)
	next_down=down_cell(x,y,grid)

	# Explore left neighbour
	if(next_left!=(-1,-1) and grid[next_left[0]][next_left[1]]!=states['WALL']):
		if(prev!='left' and visited[next_left[0]][next_left[1]]==0):
			next_positions['left']=next_left
			possibilities['left']=True
			counter+=1
		elif(prev!='left' and grid[next_left[0]][next_left[1]]==states['NODE']):
			node_counter+=1
			nodes['left']=True
			ndir=next_left
			ndir_name='left'
	else:
		wall_counter+=1

	# Explore right neighbour
	if(next_right!=(-1,-1) and grid[next_right[0]][next_right[1]]!=states['WALL']):
		if(prev!='right' and visited[next_right[0]][next_right[1]]==0):
			next_positions['right']=next_right
			possibilities['right']=True
			counter+=1
		elif(prev!='right' and grid[next_right[0]][next_right[1]]==states['NODE']):
			node_counter+=1
			nodes['right']=True
			ndir=next_right
			ndir_name='right'
	else:
		wall_counter+=1

	# Explore up neighbour
	if(next_up!=(-1,-1) and grid[next_up[0]][next_up[1]]!=states['WALL']):
		if(prev!='up' and visited[next_up[0]][next_up[1]]==0):
			next_positions['up']=next_up
			possibilities['up']=True
			counter+=1
		elif(prev!='up' and grid[next_up[0]][next_up[1]]==states['NODE']):
			node_counter+=1
			nodes['up']=True
			ndir=next_up
			ndir_name='up'
	else:
		wall_counter+=1

	# Explore down neighbour
	if(next_down!=(-1,-1) and grid[next_down[0]][next_down[1]]!=states['WALL']):
		if(prev!='down' and visited[next_down[0]][next_down[1]]==0):
			next_positions['down']=next_down
			possibilities['down']=True
			counter+=1
		elif(prev!='down' and grid[next_down[0]][next_down[1]]==states['NODE']):
			node_counter+=1
			nodes['down']=True
			ndir=next_down
			ndir_name='down'
	else:
		wall_counter+=1

	# Set visited
	visited[x][y]=1

	# If just one direction we don't need to create new node
	if(counter==0):
		edge.append((x,y))		
		if(wall_counter==3):
			if(not(x==grid.shape[0]-1 and y==grid.shape[1]-1)):
				grid[x][y]=states['NODE']
		else:
			edge.append(ndir)
		# print(edge)
		return
	elif(counter==1 and not(x==grid.shape[0]-1 and y==grid.shape[1]-1)):
		for pos in possibilities:
			if(possibilities[pos]):
				edge.append((x,y))
				explore(next_positions[pos][0],next_positions[pos][1],grid,not_to_move[pos],visited,edge)
	else:
		edge.append((x,y))
		# print(edge)
		if(not(x==grid.shape[0]-1 and y==grid.shape[1]-1)):
			grid[x][y]=states['NODE']
		for pos in possibilities:
			if(possibilities[pos]):
				explore(next_positions[pos][0],next_positions[pos][1],grid,not_to_move[pos],visited,[(x,y)])
				
