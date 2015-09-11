
from pattern_count import patterncount

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
