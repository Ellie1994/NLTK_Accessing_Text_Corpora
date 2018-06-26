import nltk
from nltk.corpus import brown
sci_fi_text = brown.words(categories="science_fiction")

frequency_distribution = nltk.FreqDist(w.lower() for w in sci_fi_text) # The FreqDist class is used to encode “frequency distributions”, which count the number of times that each outcome occurs.

questions = ["why","where","when","who","what"]
for q in questions:
    print(q + ":", frequency_distribution[q], ", ", end=" ")

# We need to include end=' ' in order for the print function to put its output on a single line. 
