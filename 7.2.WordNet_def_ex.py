from nltk.corpus import wordnet as wn

print(wn.synsets("language"))
# prints out the synonymous sets for "language"
print()

# If we are interested in the single meaning that is common to all words of e.g. the synset "speech.n.02". Synsets also come with a definition and examples methods:

print(wn.synset("speech.n.02").definition())
print()
print(wn.synset("speech.n.02").examples())

# with the number of "speech.n.02" you can change the outputed example. Try "speech.n.01", "speech.n.03", "speech.n.04". The programm will access different synonymous sets for "speech".
