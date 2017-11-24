# Import libraries
from __future__ import print_function 
import numpy as np
import math
import sys

# Import project modules
from plot import grid_states as states
from util import *
from graph import graph
from plot import plot_maze

# Main Solve maze method
def solve_maze(grid,start,end,show_progress=False):

	# Print init
	if(show_progress):
		print("Input grid received for solving...")
		print("Size:  "+str(grid.shape[0])+"x"+str(grid.shape[1]))
		print("Start: ("+str(start[0]+1)+","+str(start[1]+1)+")")
		print("End:   ("+str(end[0]+1)+","+str(end[1]+1)+")")
	
	# Optimize to grid to a graph by drastically reducing nodes
	if(show_progress):
		print("Optimizing grid...",end='')
	maze=optimize_to_graph(grid)
	if(show_progress):	
		print("Done")

	# Just for tesing the performance of optimiser
	if(show_progress):
		print("Performance of optimiser:")
		nc=0
		cel=0
		for i in range(grid.shape[0]):
			for j in range(grid.shape[1]):
				if(grid[i][j]==states['NODE']):
					nc+=1
				if(grid[i][j]!=states['WALL']):
					cel+=1
		print("Total cells in maze: "+str(grid.shape[0]*grid.shape[1]))
		print("Walkable cells in maze: "+str(cel))
		print("Total nodes in graph: "+str(nc+2))
		nc=0
		for fro_n in maze.list:
			for t in maze.list[fro_n]:
				nc+=1
		print("Total bi-dir edges in graph: "+str(nc/2))

	# If show progress is True, show the nodes selected by optimizer
	# and edges that'll be considered and those that will be pruned
	if(show_progress):
		for node in maze.list:
			for edge in maze.list[node]:
				plot_edge(grid,maze.list[node][edge])
		plot_maze(grid,full=False,show=True,save="images/pruned")
		for node in maze.list:
			for edge in maze.list[node]:
				unplot_edge(grid,maze.list[node][edge])

	# Solve the maze
	if(show_progress):
		print("Solving... ",end='\n')

	# Run A* and get shortest path
	shortest_path=a_star(maze,(0,0),(grid.shape[0]-1,grid.shape[1]-1))
	# Loop and plot the shortest path
	for i in range(len(shortest_path)-1):
		plot_full_edge(grid,maze.list[shortest_path[i]][shortest_path[i+1]])

	# Return modified grid
	return grid


# Method to optimize path finding
def optimize_to_graph(grid):

	# Initialize variables
	maze=graph()
	visited=np.zeros(shape=(grid.shape[0],grid.shape[1]))
	
	# Explore all grid cells to generate graph nodes
	explore(0,0,grid,None,visited,[],maze)

	# Return the graph
	return maze


# Explore all cells and make optimized graph structure
def explore(x,y,grid,prev,visited,edge,maze):

	# Queue to make the algo iterative else it hits recursion limit
	queue=[]
	queue.append((x,y,prev,edge))

	# Driver loop
	while(len(queue)>0):

		# Initialize variables for current iteration
		last_one=queue[-1]
		queue.pop()
		x=last_one[0]
		y=last_one[1]
		prev=last_one[2]
		edge=last_one[3]

		# Exit recursion if visiting a already visited node
		if(visited[x][y]==1):
			continue

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
			maze.add_edge_from_seq(edge)
			continue
		elif(counter==1 and not(x==grid.shape[0]-1 and y==grid.shape[1]-1)):
			for pos in possibilities:
				if(possibilities[pos]):
					edge.append((x,y))
					queue.append((next_positions[pos][0],next_positions[pos][1],not_to_move[pos],edge))					
		else:
			edge.append((x,y))
			maze.add_edge_from_seq(edge)
			if(not(x==grid.shape[0]-1 and y==grid.shape[1]-1)):
				grid[x][y]=states['NODE']
			for pos in possibilities:
				if(possibilities[pos]):
					queue.append((next_positions[pos][0],next_positions[pos][1],not_to_move[pos],[(x,y)]))
					

# A* shortest path finding algorithm
def a_star(maze,start,end):

	# Initialize variables
	adj_list=maze.list
	open_list={}
	closed_list={}

	# Add initial node
	current_node={
		'f':get_h(start,end),
		'g':0,
		'h':get_h(start,end),
		'parent':None
	}
	open_list[start]=current_node

	# Loop while open_list is not empty
	while(len(open_list)>0):

		# Get current_node from open_list with minimun f(n)=g(n)+h(n)
		current_node=get_min_f_node(open_list)

		# End if we have reached goal node
		if(current_node==end):
			print("Reached end node by shortest path. Getting path...",end='')
			print("Done")
			return get_path(start,end,open_list,closed_list)

		# Add current_node to closed list and remove from open
		closed_list[current_node]=open_list[current_node]
		del open_list[current_node]

		# Traverse all neighbours of current node
		for neighbour in adj_list[current_node]:

			# If neighbour in closed list, ignore it
			if(neighbour not in closed_list):

				# Neighbout in open list, update g() and parent if required
				if(neighbour in open_list):
					new_g_value=closed_list[current_node]['g']+len(adj_list[current_node][neighbour])
					if(open_list[neighbour]['g']>new_g_value):
						open_list[neighbour]['g']=new_g_value
						open_list[neighbour]['parent']=current_node

				# Neighbour is not in open list yet, add it
				else:
					new_node={
						'parent':current_node,
						'g':closed_list[current_node]['g']+len(adj_list[current_node][neighbour]),
						'h':get_h(neighbour,end)
					}
					new_node['f']=new_node['g']+new_node['h']
					open_list[neighbour]=new_node

	# If no path found(will never happen with current generator)
	print("No path found! LOL")
	return None


# Below functions are utility functions for A* algorithm
# Heuristic function h() for A*, using manhattan distance
def get_h(node,goal):

	# Return manhattan distance
	x_dif=abs(node[0]-goal[0])
	y_dif=abs(node[1]-goal[1])
	return x_dif+y_dif


# Select node with minimum f value, i.e. f(n)=g(n)+h(n)
def get_min_f_node(open_list):

	# Initialize variables
	min_f=float('inf')
	min_node=None

	# Loop over all nodes in open_list
	for node in open_list:

		# Check and edit min_f and min_node
		if(open_list[node]['f']<min_f):
			min_f=open_list[node]['f']
			min_node=node

	# Return the required node
	return min_node


# Get the path by backtracking
def get_path(start,end,open_list,closed_list):

	# Initialise dictionary with data for all nodes
	new_dict={}
	new_dict.update(open_list)
	new_dict.update(closed_list)

	# Initialize variables
	path=[]
	current=end

	# Backtrack from end node till we reach start parent
	while(current!=None):

		# Add current to path
		path.append(current)

		# Set current for next iteration to parent of the current node
		current=new_dict[current]['parent']

	# Return path
	return path
