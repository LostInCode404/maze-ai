# Import libraries
import numpy as np
import math
import sys

# Import project modules
from plot import grid_states as states
from plot import plot_maze

# Ask python to not to save complied bytecode
sys.dont_write_bytecode = True	


grid=np.zeros(shape=(50,50))

for i in range(10,40):
	grid[0][i]=states['EMPTY']

for i in range(10,40):
	grid[i][0]=states['PATH']

grid[0][0]=states['START']
grid[49][49]=states['GOAL']

plot_maze(grid,full=True,save="plots/plot.png")