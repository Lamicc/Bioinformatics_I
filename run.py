from pattern_count import patterncount
from frequent_words import  most_frequent, frequentwords, \
fast_most_frequent, fast_frequentwords, find_most_fword_by_sorting, \
frequent_words_with_mismatches, frequent_words_with_mismatches_by_sorting,\
frequent_words_with_mismatches_complement
from reverse_complement import findreverse
from occurrence import find_pattern
from P_to_N import pattern_to_number, number_to_pattern, p_to_n_modify, n_to_p_modify
from computing_frequencies import computingfrequencies
from find_oric import plot_skew, find_min_skew
from hamming_distance import compute_hd,approximate_pattern_matching, \
distance_between_pattern_and_strings, median_string
from neighbor import immediate_neighbors,neighbors
from motif import motif_enumeration
from profile import profile_most_probable, greedy_motif_search, randomized_motif_search, \
    find_consensus, score

import cmath

text = ""
genome = ""
k = 15
t = 20

pattern = ""

text_dna =""

dna = text_dna.split()


def standard_conversion(list):
    for i in range(0,list.__len__()):
        list[i] = str(list[i])
    stri = " ".join(list)
    return stri


#bm = randomized_motif_search(dna,k,t)[:]
#sco = score(bm,find_consensus(bm))

while 1:
    m = randomized_motif_search(dna,k,t)
    s = score(m,find_consensus(m))
    if s < 64:
        print(m)
        print("\n".join(map(str,m)))
        #print(find_consensus(m))
        print(s)
        break



#print("\n".join(map(str, randomized_motif_search(dna,k,t))))


#c = frequent_words_with_mismatches_complement(text,k,d)
#answer = " ".join(c)
#print(answer)
#print( (-1 * (0.25 * cmath.log(0.25,2)+0*cmath.log(0.25,2)+0.25*cmath.log(0.5,2)+0.5 * cmath.log(0.25,2))))

#li = list(set(l))
#total = len(li)

#print(standard_conversion(p))