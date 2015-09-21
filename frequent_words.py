
from pattern_count import patterncount, patterncount_with_mismatchs
from computing_frequencies import computingfrequencies
from P_to_N import number_to_pattern, p_to_n_modify, n_to_p_modify
from neighbor import neighbors
from hamming_distance import approximate_pattern_matching

def most_frequent(text, k):
    frequent_patterns = []
    count = []
    for i in range(0, len(text) - k + 1):
        pattern = text[i : i+k]
        count_number = patterncount(text, pattern)
        count += [count_number]
    maxcount = max(count)
    for i in range(0, len(text) - k):
        if count[i] == maxcount:
            frequent_patterns.append(text[i: i+k])
    frequent_patterns = sorted(set(frequent_patterns))
    return frequent_patterns

def frequentwords(text, k, min):
    frequent_patterns = []
    count = []
    for i in range(0, len(text) - k + 1):
        pattern = text[i : i+k]
        count_number = patterncount(text, pattern)
        count += [count_number]
    for i in range(0, len(text) - k):
        if count[i] >= min:
            frequent_patterns.append(text[i: i+k])
    frequent_patterns = sorted(set(frequent_patterns))
    return frequent_patterns

def fast_most_frequent(text, k):
    frequent_patterns = []
    frequency_array = computingfrequencies(text, k)
    maxcount = max(frequency_array)
    for i in range(0, pow(4, k)):
        if frequency_array[i] == maxcount:
            pattern = number_to_pattern(i, k)
            frequent_patterns.append(pattern)

    return frequent_patterns

def fast_frequentwords(text, k, min):
    frequent_patterns = []
    frequency_array = computingfrequencies(text, k)
    for i in range(0, pow(4, k)):
        if frequency_array[i] >= min:
            pattern = number_to_pattern(i, k)
            frequent_patterns.append(pattern)

    return frequent_patterns

def find_most_fword_by_sorting(text,k):
    frequentpatterns = []
    index = []
    count = []
    rep_count = []
    for i in range(0,len(text) -k +1):
        pattern = text[i:i+k]
        index.append(p_to_n_modify(pattern))
        count.append(1)
    sortedindex = sorted(index)
    print(sortedindex)
    rep_count.append(count[0])
    for i in range(1,len(text)- k +1):
        if sortedindex[i] == sortedindex[i-1]:
            rep_count += [rep_count[i-1] + 1]
        else:
            rep_count += [count[i]]
    maxcount = max(rep_count)
    for i in range(0,len(text)-k+1):
        if rep_count[i] == maxcount:
            pattern = n_to_p_modify(sortedindex[i],k)
            frequentpatterns.append(pattern)
    return frequentpatterns

def frequent_words_with_mismatches(text, k, d):
    frequent_patterns = []
    close = []
    for i in range(0, pow(4,k)):
        close.append(0)
        frequent_array = [0]
    for i in range(0,len(text)-k+1):
        neighborhood = neighbors(text[i:i+k],d)
        for pattern in neighborhood:
            index = p_to_n_modify(pattern)
            close[index] = 1
    for i in range(0, pow(4,k)):
        if close[i] == 1:
            pattern = n_to_p_modify(i,k)
            frequent_array.append(len(approximate_pattern_matching(pattern,text,d)))
    max_count = max(frequent_array)
    for i in range(0,pow(4,k)):
        if frequent_array[i] == max_count:
            pattern = n_to_p_modify(i,k)
            frequent_patterns.append(pattern)
    return frequent_patterns












