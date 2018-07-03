from nltk.corpus import wordnet as wn

# The pairing of a synset with a word is called a lemma. 

print(wn.synsets("funny")) # 1.prints different synsets for "funny"
print()

print(wn.synset("amusing.s.02").lemmas()) # 2.prints all the lemmas for one synset
print()

print(wn.lemma("amusing.s.02.comic")) # 3.looks up a particular lemma

print(wn.lemma("amusing.s.02.comic").synset()) # 4.gets the synset corresponding to a lemma
print()

print(wn.lemma("amusing.s.02.comic").name()) # 5.gets the "name" of a lemma.
