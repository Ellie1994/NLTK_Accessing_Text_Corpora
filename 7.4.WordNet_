from nltk.corpus import wordnet as wn

# Given a concept like "bird", we can look at the more specific words describing "bird": the hyponyms.

birds = wn.synset("bird.n.01")
types_birds = birds.hyponyms()


hyponyms = sorted(lemma.name() for synset in types_birds for lemma in synset.lemmas())

print(hyponyms) # prints out hyponyms for "bird"

# dont't mix up the "hyponym" and the "hypernym"! https://www.mytutor.co.uk/answers/7824/A-Level/English-Language/what-is-the-difference-between-a-hyponym-and-a-hypernym
