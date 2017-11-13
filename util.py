from plot import grid_states as states

# Get left neighbour
def left_cell(x,y,grid):

	# Check if not on left most point on grid
	if(y>0):
		return (x,y-1)

	# Return default value
	return (-1,-1)


# Get right neighbour
def right_cell(x,y,grid):

	# Check if not on right most point on grid
	rightlim=grid.shape[1]-1
	if(y<rightlim):
		return (x,y+1)

	# Return default value
	return (-1,-1)


# Get up neighbour
def up_cell(x,y,grid):

	# Check if not on top most point on grid
	if(x>0):
		return (x-1,y)

	# Return default value
	return (-1,-1)


# Get down neighbour
def down_cell(x,y,grid):
	# Check if not on down most point on grid
	downlim=grid.shape[0]-1
	if(x<downlim):
		return (x+1,y)

	# Return default value
	return (-1,-1)


# Check if a cell is not part of a corner
def can_be_removed(x,y,grid):

	# Bools to return result later
	up=False
	down=False
	left=False
	right=False

	# Set the value of above bools
	n_cell=up_cell(x,y,grid)
	if(n_cell!=(-1,-1) and grid[n_cell[0]][n_cell[1]]==states['WALL']):
		up=True
	n_cell=down_cell(x,y,grid)
	if(n_cell!=(-1,-1) and grid[n_cell[0]][n_cell[1]]==states['WALL']):
		down=True
	n_cell=left_cell(x,y,grid)
	if(n_cell!=(-1,-1) and grid[n_cell[0]][n_cell[1]]==states['WALL']):
		left=True
	n_cell=right_cell(x,y,grid)
	if(n_cell!=(-1,-1) and grid[n_cell[0]][n_cell[1]]==states['WALL']):
		right=True

	# print("\n"+str(x)+","+str(y))
	# print(str(up)+" "+str(down)+" "+str(left)+" "+str(right)+" ")

	# Return true if part of vertical wall
	if(up and down and not left and not right):
		return True

	# Return true if part of horizontal wall
	if(left and right and not up and not down):
		return True

	# Otherwise, return false
	return False
