# NChatlani - Python script to determine how many words in a list are
# anagrams of each other

f = open('words.txt')

anagram_d = {}


for line in f:
    # Loop through word list and create a tuple out of the alphabetically
    # sorted word
    line = line.strip()
    key_word = tuple((sorted(line)))
    
    # If the sorted word is not in the word list, add it as a key to the 
    # dictionary and append the unsorted word to the list of anagrams for it
    if key_word not in anagram_d:
        anagram_d[key_word] = []
        anagram_d[key_word].append(line)
    else:
        #If the sorted word is in the dictionary, just append the word
        anagram_d[key_word].append(line)

#Print the list of anagrams for every entry that has more than one word
for key_word in anagram_d:
    if len(anagram_d[key_word]) > 1:
        print anagram_d[key_word]
