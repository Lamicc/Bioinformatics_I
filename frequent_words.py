
from pattern_count import patterncount
from computing_frequencies import computingfrequencies
from P_to_N import number_to_pattern

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



