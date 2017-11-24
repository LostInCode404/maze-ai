# Import libraries
from __future__ import print_function 
import numpy as np
import argparse
import pickle
import matplotlib.pyplot as plt

# Import project modules
from plot import grid_states as states
from plot import plot_maze
from generate import generate_maze as generate
from solve import solve_maze as solve

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--do", type = str)
parser.add_argument("--save", type = str)
parser.add_argument("--file", type = str)
parser.add_argument("--x", type = int)
parser.add_argument("--y", type = int)
args = parser.parse_args()

# Only generate the maze
if(args.do=='generate'):
	grid=generate(args.x,args.y,show_progress=False)
	if(args.save):
		with open(args.save,'wb') as file:
			pickle.dump(grid,file)

# Only solve a maze after loading it
elif(args.do=='solve'):
	with open(args.file,'rb') as file:
		grid=np.array(pickle.load(file))
		solve(grid,(0,0),(grid.shape[0]-1,grid.shape[1]-1))

# Plot performance
elif(args.do=='plot_performance'):
	
	# Open file
	with open(args.file,'r') as file:

		# Initialize
		gen_y=[]
		gen_label=[]
		sol_y=[]
		sol_label=[]
		# Read file
		for line in file:
			line=line.strip().split(" ")
			if(line[0]=='generate'):
				gen_y.append(float(line[2]))
				gen_label.append(line[1])
			elif(line[0]=='solve'):
				sol_y.append(float(line[2]))
				sol_label.append(line[1])

		# Set plot config
		plt.rc('xtick', labelsize=7) 
		plt.rc('ytick', labelsize=7) 

		# Plot generation performance plot
		gen_x=np.array(list(range(len(gen_y))))+1
		plt.xticks(gen_x,gen_label,)
		plt.plot(gen_x,gen_y)
		plt.plot(gen_x,gen_y,'ro')
		plt.title("Performance of maze generator: Grid size vs Time taken")
		plt.xlabel("Grid dimension")
		plt.ylabel("Time(seconds)")		
		fig=plt.gcf()
		fig.savefig('images/plot_generator')
		plt.show()

		# Plot solving performance plot
		sol_x=np.array(list(range(len(sol_y))))+1
		plt.xticks(sol_x,sol_label,)
		plt.plot(sol_x,sol_y)
		plt.plot(sol_x,sol_y,'ro')
		plt.title("Performance of maze solver(including optimizer): Grid size vs Time taken")
		plt.xlabel("Grid dimension")
		plt.ylabel("Time(seconds)")
		fig=plt.gcf()
		fig.savefig('images/plot_solver')
		plt.show()

else:
	print("Invalid option passed. Exiting...")