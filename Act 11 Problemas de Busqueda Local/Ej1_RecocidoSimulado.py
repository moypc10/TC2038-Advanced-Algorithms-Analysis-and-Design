import time
import random
import math

class Board(object):
    def __init__(self, n, randomize = True):        
        self.n = n
        self.queens = []
        if (randomize):
            # Initialize the board randomly
            for q in range(n):
                empty_space = False
                while not empty_space:
                    row = random.choice(range(n))
                    col = random.choice(range(n))
                    if not [row, col] in self.queens:
                        empty_space = True;
                self.queens.append([row, col])
        else:
            # Place the queens on the first row
            for q in range(n):
                self.queens.append([0, q])

    def show(self):                      
        for row in range(self.n):
            for col in range(self.n):
                if [row, col] in self.queens:
                    print (' Q ', end = '')
                else:
                    print (' - ', end = '')
            print('')
        print('')
    
    def cost(self):
        c = 0
        for i in range(self.n):
            queen = self.queens[i]
            safe = True
            for j in range(self.n):
                if i == j:
                    continue
                other_queen = self.queens[j]
                if (queen[0] == other_queen[0]):
                    # The queens are on the same row
                    safe = False
                elif (queen[1] == other_queen[1]):
                    # The queens are on the same column
                    safe = False
                elif abs(queen[0]-other_queen[0]) == abs(queen[1]-other_queen[1]):
                    # The queens are on the same diagonal
                    safe = False
            if not safe:
                c += 1
        return c

    def neighbor(self):
        # Copy current board
        new_board = Board(self.n, False)
        for i in range(self.n):
            new_board.queens[i][0] = self.queens[i][0]
            new_board.queens[i][1] = self.queens[i][1]
             
        # Select one empty position randomly
        valid_position = False
        while not valid_position:            
            new_row = random.choice(range(self.n))
            new_col = random.choice(range(self.n))
            
            valid_position = True
            for q in range(self.n):
                if new_board.queens[q][0] == new_row and new_board.queens[q][1] == new_col:
                    valid_position = False
                    break
        
        # Update one queen selected randomly
        queen_index = random.choice(range(self.n))
        new_board.queens[queen_index][0] = new_row
        new_board.queens[queen_index][1] = new_col

        return new_board
    
                                       
#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------
random.seed(time.time()*1000)

board = Board(8, True)      # Initialize board
board.show()    

cost = board.cost()         # Initial cost    
step = 0                    # Step count

alpha = 0.9995              # Coefficient of the exponential temperature schedule        
t0 = 1                      # Initial temperature
t = t0    

while t > 0.005 and cost > 0:

    # Calculate temperature
    t = t0 * math.pow(alpha, step)
    step += 1
        
    # Get random neighbor
    neighbor = board.neighbor()
    new_cost = neighbor.cost()

    # Test neighbor
    if new_cost < cost:
        board = neighbor
        cost = new_cost
    else:
        # Calculate probability of accepting the neighbor
        p = math.exp(-(new_cost - cost)/t)
        if p >= random.random():
            board = neighbor
            cost = new_cost

    print("Iteration: ", step, "    Cost: ", cost, "    Temperature: ", t)

print("--------Solution-----------")
board.show()          

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------