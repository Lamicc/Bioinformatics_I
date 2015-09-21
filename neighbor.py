from hamming_distance import compute_hd

def immediate_neighbors(pattern):
    neighborhood = [pattern]
    for i in range(0, pattern.__len__()):
        if pattern[i] == "A":
            for s in "CGT":
                new_pattern = pattern[:i] + s + pattern[i+1:]
                neighborhood.append(new_pattern)
        elif pattern[i] == "C":
            for s in "AGT":
                new_pattern = pattern[:i] + s + pattern[i+1:]
                neighborhood.append(new_pattern)
        elif pattern[i] == "G":
            for s in "ACT":
                new_pattern = pattern[:i] + s + pattern[i+1:]
                neighborhood.append(new_pattern)
        elif pattern[i] == "T":
            for s in "ACG":
                new_pattern = pattern[:i] + s + pattern[i+1:]
                neighborhood.append(new_pattern)
    return neighborhood

def suffix(pattern):
    return pattern[1:]

def neighbors(pattern,d):
    if d == 0:
        return pattern
    elif len(pattern) == 1:
        return ["A","C","G","T"]
    neighborhood = []
    suffix_neighbors = neighbors(suffix(pattern),d)
    for text in suffix_neighbors:
        if compute_hd(suffix(pattern), text) < d:
            for n in "ACGT" :
                neighborhood.append(n+text)
        else:
            neighborhood.append(pattern[0]+text)
    return neighborhood




