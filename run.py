from pattern_count import patterncount
from frequent_words import  most_frequent, frequentwords
from reverse_complement import findreverse
from occurrence import find_pattern


text = ""
pattern = ""
genome = ""
k = 9
t = 20
#print(most_frequent(genome,k))
#print(patterncount(genome,pattern))
print(frequentwords(genome,k,t))

#print(genome)

#for i in find_pattern(genome,pattern):
#    print(i)