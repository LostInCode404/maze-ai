# Import libraries
from __future__ import print_function 
import numpy as np
import math
import sys

# Import project modules
from plot import grid_states as states
from plot import plot_maze
from generate import generate_maze as generate
from solve import solve_maze as solve

# Generate maze
maze=generate(25,25,show_progress=True)

# Plot the generated maze
plot_maze(maze,full=True,show=True,save="images/maze_generated",show_progress=True)

# Solve the maze
solve(maze,(0,0),(maze.shape[0]-1,maze.shape[1]-1),show_progress=True)

# Plot the solved maze
plot_maze(maze,full=True,show=True,save="images/maze_solved",show_progress=True)