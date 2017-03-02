# NChatlani, JContino
# Python Script to create as many words as possible from a 4x4 letter grid

# UNFINISHED - infinite loop in BST, possible that return state not being reached 

from copy import deepcopy

f = open('words.txt')

word_dict = {}

# Fill dictionary with all words as keys, 'brains' as the value to compare
# for new words
for line in f:
    line = line.strip()
    
    if line not in word_dict:
        word_dict[line] = []
        word_dict[line].append(tuple(line))
    else:
        word_dict[line].append(tuple(line))
        
# State object which keeps track of the letters visited, as well of a list of 
# previously visited positions on the grid
class State(object):
    
    def __init__(self, location, letter):
        
        self.location = []
        self.letter = letter
        self.word = []
        self.word.append(letter)
        self.history = [location]
        
    def __str__(self):
        print self.word
        
# Initlialize 4x4 grid with letters

grid = [['u', 'n', 't', 'h'],
        ['g', 'a', 'e', 's'],
        ['s', 'r', 't', 'r'],
        ['h', 'm', 'i', 'a']]
        
        
# Breadth-First Search starts here        
def BST(state, i, j):
    
    # Initialize the state queue, the dict of visited states
    state_queue = [state]
    
    #Run the solver while states are still in the queue
    while (len(state_queue)):
        
        #If a valid word has been created, print it
        if tuple(state.word) in word_dict:
            print state
        
        # If all 16 letters in the grid have been visited, end this BST
        if len(state.history) == 16:
            return
        
        # Check letter in 8 directions around current state's letter
        for k in range(-1, 1):
            for l in range(-1, 1):
                i += k
                j += l
                
                # If new grid location is within the grid and has not been
                # previously visited, create a new state, append the old state's
                # values and append the new state to the queue
                if i > 0 and i < 3 and j > 0 and j < 3:
                    if [i,j] not in state.history:
                        new_state = deepcopy(state)
                        new_state.history.append([i, j])
                        new_state.letter = new_state.word[len(new_state.word)]
                        new_state.location = [i,j]
                        new_state.word.append(grid[i][j])
                        state_queue.append(new_state)


# Run a Breadth-First-Search for each position in the letter grid                        
for i in range(0, 3):
    for j in range(0, 3):
        state = State([i,j], grid[i][j])
        BST(state, i, j)
                        
            
    
        
                    
            