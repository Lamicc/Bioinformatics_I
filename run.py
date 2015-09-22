from pattern_count import patterncount
from frequent_words import  most_frequent, frequentwords, \
fast_most_frequent, fast_frequentwords, find_most_fword_by_sorting, \
frequent_words_with_mismatches, frequent_words_with_mismatches_by_sorting
from reverse_complement import findreverse
from occurrence import find_pattern
from P_to_N import pattern_to_number, number_to_pattern, p_to_n_modify, n_to_p_modify
from computing_frequencies import computingfrequencies
from find_oric import plot_skew, find_min_skew
from hamming_distance import compute_hd,approximate_pattern_matching
from neighbor import immediate_neighbors,neighbors

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"

pattern = ""
genome = ""
k = 4

d =1



def standard_conversion(list):
    for i in range(0,list.__len__()):
        list[i] = str(list[i])
    stri = " ".join(list)
    return stri



c = frequent_words_with_mismatches(text,k,d)

#c = approximate_pattern_matching(pattern,text,d)


answer = " ".join(c)
print(answer)

#p = frequent_words_with_mismatches_by_sorting(text,k,d)


#li = list(set(l))
#total = len(li)

#print(standard_conversion(p))