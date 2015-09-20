from hamming_distance import compute_hd

def patterncount(text, pattern):
    count = 0
    for i in range(0, len(text)-len(pattern)+1):
        if text[i : i+len(pattern)]  == pattern:
            count = count + 1
    return count

def patterncount_with_mismatchs(text, pattern,d):
    count = 0
    for i in range(0, len(text)-len(pattern)+1):
        if text[i : i+len(pattern)]  == pattern:
            count = count + 1
        elif compute_hd(text[i : i+len(pattern)],pattern) <= d:
            count = count + 1
    return count