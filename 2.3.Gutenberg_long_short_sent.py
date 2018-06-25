from nltk.corpus import gutenberg

hamlet_sents = gutenberg.sents('shakespeare-hamlet.txt')
print(hamlet_sents) # prints out the introduction

print() # prints out a blank string 

print(hamlet_sents[19]) # finds one particular sentence by its number in a text

print() # prints out a blank string 

longest_sent = max(len(s) for s in hamlet_sents) # prints out a number of the longest sentence

shortest_sent = min(len(s) for s in hamlet_sents) # prints out a number of the shortest sentence

print(longest_sent)
print(shortest_sent)

print([s for s in hamlet_sents if len(s) == longest_sent])
print([s for s in hamlet_sents if len(s) == shortest_sent]) # may print out some "shortest sentences"
