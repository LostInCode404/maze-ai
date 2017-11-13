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

# Allow recursion to high depth
# Used for now, later, will implement iterative code
sys.setrecursionlimit(10000)

# Generate maze
maze=generate(101,101)

# Plot the generated maze
plot_maze(maze,full=True,show=True,save="images/generated")

# Solve the maze
solve(maze,(0,0),(maze.shape[0]-1,maze.shape[1]-1))

# Plot the solved maze
plot_maze(maze,full=True,show=True,save="images/solved")