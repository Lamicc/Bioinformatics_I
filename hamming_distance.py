
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

