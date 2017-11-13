# Import libraries
from __future__ import print_function 


# Define graph class
class graph(object):


	# Constructor
	def __init__(self):
		self.list={}


	# Method to add new edge
	def add_edge(self,from_node,to_node,path):

		# Check if from_node is not in graph
		if(from_node not in self.list):
			self.list[from_node]={}

		# Check if to_node is not in graph
		if(to_node not in self.list):
			self.list[to_node]={}

		# Add the from_node to to_node edge
		if(to_node not in self.list[from_node]):
			self.list[from_node][to_node]=[]
		self.list[from_node][to_node].append(path)

		# Add the to_node to from_node edge
		# Note: no need to reverse edge list, as it'll just be used for plotting
		if(from_node not in self.list[to_node]):
			self.list[to_node][from_node]=[]
		self.list[to_node][from_node].append(path)


	# Method to add edge based on input sequence
	def add_edge_from_seq(self,edge):

		# Call add_edge with appropriate parameters
		self.add_edge(edge[0],edge[-1],edge)
