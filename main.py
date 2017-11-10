# Import libraries
import numpy as np
import math

# Import project modules
from plot import grid_states as states
from plot import plot_maze
from generate import generate_maze as generate

# Generate maze
maze=generate(50,50)

# Plot the generated maze
plot_maze(maze,full=True,save="images/plot")