from P_to_N import p_to_n_modify,n_to_p_modify

def compute_hd(pattern1,pattern2):
    hamming_distance = 0
    if len(pattern1) != len(pattern2):
        print("Pleace inmput equal length patterns!")
        return 0
    else:
        for i in range(0, pattern1.__len__()):
            if pattern1[i] != pattern2[i]:
                hamming_distance += 1
    return hamming_distance

def approximate_pattern_matching(pattern, text, d):
    positions = []
    for i in range(0, len(text)- len(pattern)+1):
        if text[i : i+len(pattern)]  == pattern:
            positions.append(i)
        elif compute_hd(text[i : i+len(pattern)],pattern) <= d:
            positions.append(i)
    return positions

def distance_between_pattern_and_strings(pattern,dna):
    k = len(pattern)
    distance = 0
    for text in dna:
        hamming_distance = float('inf')
        for i in range(0,len(text)-k +1):
            pattern_II = text[i:i+k]
            if hamming_distance > compute_hd(pattern,pattern_II):
                hamming_distance = compute_hd(pattern,pattern_II)
        distance += hamming_distance
    return distance

def median_string(dna,k):
    distance = float('inf')
    for i in range(0,pow(4,k)):
        pattern = n_to_p_modify(i,k)
        if distance > distance_between_pattern_and_strings(pattern,dna):
            distance = distance_between_pattern_and_strings(pattern,dna)
            median = pattern
    return median

