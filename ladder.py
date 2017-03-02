# NChatlani and JContino
# Python Script to create a word ladder from 'brains' to 'snakes'

from copy import deepcopy

# Open word file and initialize variables
f = open('words.txt')

word_dict = {}
word_hist = []
start_word = 'snakes'
goal_word = 'brains'
alphabet = 'abcdefghijklmnopqrstuvwxyz'


# Fill dictionary with all words as keys, 'brains' as the value to compare
# for new words
for line in f:
    line = line.strip()
    
    if line not in word_dict:
        word_dict[line] = []
        word_dict[line].append(start_word)
    else:
        word_dict[line].append(start_word)

# State object which keeps track of all previously created words
class State(object):
    
    
    def __init__(self, word, words):
        self.words = []
        self.word = word
        self.words.append(word)
        
    def __str__(self):
        for word in self.words:
            print word
        
# word_ladder is a State object which starts with 'brains'. Each created 
# valid word is appended to its word list
word_ladder = State('snakes', word_hist)
word_queue = [word_ladder]

visited = {}

# Breadth-First-Search which cycles each letter of the current word through
# the alphabet, and checks each permutation to see if the word is valid.
while len(word_queue):
    state = word_queue.pop(0)
    
    # Goal state
    if state.word == goal_word:
        print 'completed ladder!'
        print state.words
        exit(0)
        
    visited[state.word] = True
        
    # For each letter in the word, cycle through the alphabet to try making
    # a new word.
    for i in range (len(state.word)):
        for letter in alphabet:
            if state.word[i] != letter:
                new_word = state.word
                new_word = new_word[:i] + letter + new_word[i+1:]
                
                if new_word in word_dict and new_word not in visited:
                    new_state = deepcopy(state)
                    new_state.word = new_word
                    new_state.words.append(new_word)
                    word_queue.append(new_state)