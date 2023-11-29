from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue
import math

class TreeNode:    
    def __init__(self, parent, s, c):
        self.parent = parent
        self.s = s
        self.c = c
        
    def __lt__(self, node):
        return False


    def path(self):
        node = self
        path = [] 
        while node != None:
            path.insert(0, node.s)
            node = node.parent                
        return path

def maze_bfs(maze, s0, sg):
    # Number of rows and columns of the maze.
    nr = len(maze)
    nc = len(maze[0])

    # Check initial and goal positions
    if (s0[0]<0) or (s0[0]>=nr) or (s0[1]<0) or (s0[1]>=nc):
        print("Warning: Initial position", s0, "is not in the maze.")
        
    if (sg[0]<0) or (sg[0]>=nr) or (sg[1]<0) or (sg[1]>=nc):
        print("Warning: Goal position", sg, "is not in the maze.")
        
    # Initialize frontier
    frontier = Queue()
    frontier.put(TreeNode(None, s0, 0))

    # Initialize explored set
    explored_set = {}
    
    # Find path
    while True:
        if frontier.empty():
            return None
        
        # Get node from frontier
        node = frontier.get()
        
        # Test node
        if node.s == sg:
            # Return path and cost as a dictionary
            return {"Path": node.path(), "Cost": node.c}
        
        # Expand node if it is not in the explored set
        if node.s not in explored_set:
            
            neighbors = []
            
            # Check possible neighbors
            row = node.s[0]
            col = node.s[1]

            if row > 0 and row <= nr-1 and maze[row-1][col] == ' ':
                neighbors.append((row - 1, col))

            if row >= 0 and row < nr-1 and maze[row+1][col] == ' ':
                neighbors.append((row + 1, col))
        
            if col > 0 and col <= nc-1 and maze[row][col-1] == ' ':
                neighbors.append((row, col-1))

            if col >= 0 and col < nc-1 and maze[row][col+1] == ' ':
                neighbors.append((row, col+1))

            # Add neighbors to the frontier
            for neighbor in neighbors:
                frontier.put(TreeNode(node, neighbor, node.c + 1))
                
        # Add node to the explored set
        explored_set[node.s] = 0  

def maze_dfs(maze, s0, sg):
    # Number of rows and columns of the maze.
    nr = len(maze)
    nc =len(maze[0])

    # Check initial and goal positions
    if (s0[0]<0) or (s0[0]>=nr) or (s0[1]<0) or (s0[1]>=nc):
        print("Warning: Initial position", s0, "is not in the maze.")
        
    if (sg[0]<0) or (sg[0]>=nr) or (sg[1]<0) or (sg[1]>=nc):
        print("Warning: Goal position", sg, "is not in the maze.")
        
    # Initialize frontier
    frontier = LifoQueue()
    frontier.put(TreeNode(None, s0, 0))

    # Initialize explored set
    explored_set = {}
    
    # Find path
    while True:
        if frontier.empty():
            return None
        
        # Get node from frontier
        node = frontier.get()
        
        # Test node
        if node.s == sg:
            # Return path and cost as a dictionary
            return {"Path": node.path(), "Cost": node.c}
        
        # Expand node if it is not in the explored set
        if node.s not in explored_set:
            
            neighbors = []
            
            # Check possible neighbors
            row = node.s[0]
            col = node.s[1]

            if row > 0 and row <= nr-1 and maze[row-1][col] == ' ':
                neighbors.append((row - 1, col))

            if row >= 0 and row < nr-1 and maze[row+1][col] == ' ':
                neighbors.append((row + 1, col))
        
            if col > 0 and col <= nc-1 and maze[row][col-1] == ' ':
                neighbors.append((row, col-1))

            if col >= 0 and col < nc-1 and maze[row][col+1] == ' ':
                neighbors.append((row, col+1))

            # Add neighbors to the frontier
            for neighbor in neighbors:
                frontier.put(TreeNode(node, neighbor, node.c + 1))
                
        # Add node to the explored set
        explored_set[node.s] = 0  
        
def maze_ucs(maze, s0, sg):
    # Number of rows and columns of the maze.
    nr = len(maze)
    nc =len(maze[0])

    # Check initial and goal positions
    if (s0[0]<0) or (s0[0]>=nr) or (s0[1]<0) or (s0[1]>=nc):
        print("Warning: Initial position", s0, "is not in the maze.")
        
    if (sg[0]<0) or (sg[0]>=nr) or (sg[1]<0) or (sg[1]>=nc):
        print("Warning: Goal position", sg, "is not in the maze.")
        
    # Initialize frontier
    frontier = PriorityQueue()
    frontier.put((0, TreeNode(None, s0, 0)))

    # Initialize explored set
    explored_set = {}
    
    # Find path
    while True:
        if frontier.empty():
            return None
        
        # Get node from frontier
        node = frontier.get()[1]
        
        # Test node
        if node.s == sg:
            # Return path and cost as a dictionary
            return {"Path": node.path(), "Cost": node.c}
        
        # Expand node if it is not in the explored set
        if node.s not in explored_set:
            
            neighbors = []
            
            # Check possible neighbors
            row = node.s[0]
            col = node.s[1]

            if row > 0 and row <= nr-1 and maze[row-1][col] == ' ':
                neighbors.append((row - 1, col))

            if row >= 0 and row < nr-1 and maze[row+1][col] == ' ':
                neighbors.append((row + 1, col))
        
            if col > 0 and col <= nc-1 and maze[row][col-1] == ' ':
                neighbors.append((row, col-1))

            if col >= 0 and col < nc-1 and maze[row][col+1] == ' ':
                neighbors.append((row, col+1))

            # Add neighbors to the frontier
            for neighbor in neighbors:
                frontier.put((node.c + 1, TreeNode(node, neighbor, node.c + 1)))
                
        # Add node to the explored set
        explored_set[node.s] = 0  
       
def maze_astar(maze, s0, sg):
    # Number of rows and columns of the maze.
    nr = len(maze)
    nc =len(maze[0])

    # Check initial and goal positions
    if (s0[0]<0) or (s0[0]>=nr) or (s0[1]<0) or (s0[1]>=nc):
        print("Warning: Initial position", s0, "is not in the maze.")
        
    if (sg[0]<0) or (sg[0]>=nr) or (sg[1]<0) or (sg[1]>=nc):
        print("Warning: Goal position", sg, "is not in the maze.")
        
    # Initialize frontier
    frontier = PriorityQueue()
    frontier.put((0, TreeNode(None, s0, 0)))

    # Initialize explored set
    explored_set = {}
    
    # Find path
    while True:
        if frontier.empty():
            return None
        
        # Get node from frontier
        node = frontier.get()[1]
        
        # Test node
        if node.s == sg:
            # Return path and cost as a dictionary
            return {"Path": node.path(), "Cost": node.c}
        
        # Expand node if it is not in the explored set
        if node.s not in explored_set:
            
            neighbors = []
            
            # Check possible neighbors
            row = node.s[0]
            col = node.s[1]

            if row > 0 and row <= nr-1 and maze[row-1][col] == ' ':
                neighbors.append((row - 1, col))

            if row >= 0 and row < nr-1 and maze[row+1][col] == ' ':
                neighbors.append((row + 1, col))
        
            if col > 0 and col <= nc-1 and maze[row][col-1] == ' ':
                neighbors.append((row, col-1))

            if col >= 0 and col < nc-1 and maze[row][col+1] == ' ':
                neighbors.append((row, col+1))

            # Add neighbors to the frontier
            for neighbor in neighbors:
                
                # Calculate squared distance to the goal
                h = math.sqrt((neighbor[0]-sg[0])**2 + (neighbor[1]-sg[1])**2)
                g = node.c + 1
                f = g + h
                
                # Add new node
                frontier.put((f, TreeNode(node, neighbor, g)))
                
        # Add node to the explored set
        explored_set[node.s] = 0  
        
def maze_idastar(maze, s0, sg, flimit = 1):
    # Number of rows and columns of the maze.
    nr = len(maze)
    nc =len(maze[0])

    # Check initial and goal positions
    if (s0[0]<0) or (s0[0]>=nr) or (s0[1]<0) or (s0[1]>=nc):
        print("Warning: Initial position", s0, "is not in the maze.")
        
    if (sg[0]<0) or (sg[0]>=nr) or (sg[1]<0) or (sg[1]>=nc):
        print("Warning: Goal position", sg, "is not in the maze.")
        
    # Initialize frontier
    frontier = PriorityQueue()
    frontier.put((0, TreeNode(None, s0, 0)))

    # Initialize explored set
    explored_set = {}
    
    # Initialize next limit value
    fnext = 100000000000
    flimitChanged = False
    
    # Find path
    while True:
        if frontier.empty():
            if not flimitChanged:
                # In this case, the limit has not changed, so there is no solution.
                return None
            else:
                # In this case, there is at least one node that have surprass the initial limit. Try again using fnext.
                return maze_idastar(maze, s0, sg, fnext) 
        
        # Get node from frontier
        node = frontier.get()
        fval = node[0]
        node = node[1]
        
        # Test node
        if node.s == sg:
            # Return path and cost as a dictionary
            return {"Path": node.path(), "Cost": node.c}
        
        # Expand node if it is not in the explored set
        if node.s not in explored_set:
            
            # Check if the f value of the node is below the limit.
            if fval <= flimit:
                neighbors = []
            
                # Check possible neighbors
                row = node.s[0]
                col = node.s[1]

                if row > 0 and row <= nr-1 and maze[row-1][col] == ' ':
                    neighbors.append((row - 1, col))

                if row >= 0 and row < nr-1 and maze[row+1][col] == ' ':
                    neighbors.append((row + 1, col))
        
                if col > 0 and col <= nc-1 and maze[row][col-1] == ' ':
                    neighbors.append((row, col-1))

                if col >= 0 and col < nc-1 and maze[row][col+1] == ' ':
                    neighbors.append((row, col+1))

                # Add neighbors to the frontier
                for neighbor in neighbors:
                
                    # Calculate squared distance to the goal
                    h = math.sqrt((neighbor[0]-sg[0])**2 + (neighbor[1]-sg[1])**2)
                    g = node.c + 1
                    f = g + h
                
                    # Add new node
                    frontier.put((f, TreeNode(node, neighbor, g)))    
                    
            else:
                fnext = min(fnext, fval)
                flimitChanged = True
                
        # Add node to the explored set
        explored_set[node.s] = 0  

# Initialize map
initial_position = (1,2)
goal_position = (1,40)
maze = ('++++++++++++++++++++++++++++++++++++++++++',
        '+     + ++ ++ +       +++   + + ++       +',
        '+   + +     + +++++ +     ++ +++ +       +',
        '+ +    ++  +  + +++ +   + ++ +++ +       +',
        '+ +   + +     +     ++++                 +',
        '+   + ++ ++++ + + ++ ++  +  +++          +',
        '++ ++ + +     +++  ++++ ++++  ++++ +++++++',
        '++ ++ +++  ++++++ ++    ++ + ++     + + ++',
        '+          + +  + ++++      ++  + ++ +  ++',
        '+++++ +++++++++++ ++++++++   +      ++  ++',
        '+     +    ++      +  +++++  + + ++ ++ + +',
        '++ ++++ +      ++            +      +   ++',
        '++         +++++++++  ++++  + + ++  ++++++',
        '++++++++++++++++++++++++++++++++++++++++++')

#### Solve maze using BFS ####
print("\n***** BFS *****")
result = maze_bfs(maze, initial_position, goal_position)

for r in range(len(maze)):
    for c in range(len(maze[0])):
        if ((r,c) == initial_position):
            print('O', end = '')
        elif ((r,c) == goal_position):
            print('X', end = '') 
        elif (r,c) in result['Path']:     
            print('@', end = '') 
        else:
            print(maze[r][c], end = '')
    print()        

print("Cost:", result['Cost'])

#### Solve maze using DFS ####
print("\n***** DFS *****")

result = maze_dfs(maze, initial_position, goal_position)

for r in range(len(maze)):
    for c in range(len(maze[0])):
        if ((r,c) == initial_position):
            print('O', end = '')
        elif ((r,c) == goal_position):
            print('X', end = '') 
        elif (r,c) in result['Path']:     
            print('@', end = '') 
        else:
            print(maze[r][c], end = '')
    print()        

print("Cost:", result['Cost'])

#### Solve maze using UCS ####
print("\n***** UCS *****")

result = maze_ucs(maze, initial_position, goal_position)

for r in range(len(maze)):
    for c in range(len(maze[0])):
        if ((r,c) == initial_position):
            print('O', end = '')
        elif ((r,c) == goal_position):
            print('X', end = '') 
        elif (r,c) in result['Path']:     
            print('@', end = '') 
        else:
            print(maze[r][c], end = '')
    print()        

print("Cost:", result['Cost'])

#### Solve maze using A-Star ####
print("\n***** A-Star *****")

result = maze_astar(maze, initial_position, goal_position)

for r in range(len(maze)):
    for c in range(len(maze[0])):
        if ((r,c) == initial_position):
            print('O', end = '')
        elif ((r,c) == goal_position):
            print('X', end = '') 
        elif (r,c) in result['Path']:     
            print('@', end = '') 
        else:
            print(maze[r][c], end = '')
    print()        

print("Cost:", result['Cost'])

#### Solve maze using IDA-Star ####
print("\n***** IDA-Star *****")

result = maze_idastar(maze, initial_position, goal_position)

for r in range(len(maze)):
    for c in range(len(maze[0])):
        if ((r,c) == initial_position):
            print('O', end = '')
        elif ((r,c) == goal_position):
            print('X', end = '') 
        elif (r,c) in result['Path']:     
            print('@', end = '') 
        else:
            print(maze[r][c], end = '')
    print()        

print("Cost:", result['Cost'])