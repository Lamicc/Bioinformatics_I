from pattern_count import patterncount
from frequent_words import  most_frequent, frequentwords
from reverse_complement import findreverse
from occurrence import find_pattern
from P_to_N import pattern_to_number, number_to_pattern

text = ""
pattern = "ATGCAA"
genome = ""
k = 9
t = 20
#print(most_frequent(genome,k))
#print(patterncount(genome,pattern))
#print(frequentwords(genome,k,t))

#print(genome)

#for i in find_pattern(genome,pattern):
#    print(i)

#print(pattern_to_number(pattern))

#print(4096+1024+256+16*3+4*3+1)
print(number_to_pattern(5437,7))