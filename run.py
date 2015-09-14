from pattern_count import patterncount
from frequent_words import  most_frequent, frequentwords
from reverse_complement import findreverse
from occurrence import find_pattern
from P_to_N import pattern_to_number, number_to_pattern
from computing_frequencies import computingfrequencies


text=""
pattern = "AGT"
genome = ""
k = 6
t = 20


def standard_conversion(list):
    for i in range(0,list.__len__()):
        list[i] = str(list[i])
    str = " ".join(list)
    return str
