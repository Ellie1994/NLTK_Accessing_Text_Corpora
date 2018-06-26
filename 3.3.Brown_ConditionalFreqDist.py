import nltk
from nltk.corpus import brown
from nltk.probability import ConditionalFreqDist


cond_freq_dist = ConditionalFreqDist(
    (g,w)
    for g in brown.categories()
        
    for w in brown.words(categories=g))

genres = ["government","fiction","mystery","science_fiction","adventure"]
modal_verbs = ["may","can","could","should","must","might","will"]

print(cond_freq_dist.tabulate(conditions=genres,samples=modal_verbs))

# Conditional frequency distributions are used to record the number of times each sample occurred.
# Conditional frequency distributions are typically constructed by repeatedly running an experiment under a variety of conditions.


## output:
#             may    can  could should   must  might   will 
#    government    153    117     38    112    102     13    244 
#       fiction      8     37    166     35     55     44     52 
#       mystery     13     42    141     29     30     57     20 
#science_fiction      4     16     49      3      8     12     16 
#     adventure      5     46    151     15     27     58     50 
##
