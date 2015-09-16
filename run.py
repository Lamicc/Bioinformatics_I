#from pattern_count import patterncount
from frequent_words import  most_frequent, frequentwords, fast_most_frequent, fast_frequentwords, find_most_fword_by_sorting
from reverse_complement import findreverse
from occurrence import find_pattern
#from P_to_N import pattern_to_number, number_to_pattern, p_to_n_modify, n_to_p_modify
from computing_frequencies import computingfrequencies


text="AAGCAAAGGTGGG"
#pattern = "GTGTCCAAGTCCGACTCCAC"
genome = ""
k = 2
#t = 18


def standard_conversion(list):
    for i in range(0,list.__len__()):
        list[i] = str(list[i])
    str = " ".join(list)
    return str

#l = fast_frequentwords(text,k,t)
#answer = " ".join(l)
#li = list(set(l))
#total = len(li)

print(fast_most_frequent(text,k))
print(find_most_fword_by_sorting(text,k))
#print(text[0:3])
