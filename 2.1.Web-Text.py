# 2.Web-Text 
# Project Gutenberg represents established literature. It is important to consider less formal language as well. NLTK's small collection of web text includes content from a Firefox discussion forum, conversations overheard in New York, the movie script of Pirates of the Carribean, personal advertisements, and wine reviews #

import nltk
from nltk.corpus import webtext
for files in webtext.fileids():
    print(files, webtext.raw(files)[:11], "...")

wine = nltk.corpus.webtext.words("wine.txt")
print("the number of words in 'wine.txt' is: " + str(len(wine)))

# you should convert "len" into a "str" so python can combine two strings.
