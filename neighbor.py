
def immediate_neighbors(pattern):
    neighborhood = [pattern]
    for i in range(1, pattern.__len__()):
        if pattern[i] == "A":
            for s in "CGT":
                new_pattern = pattern.pop()
                new_pattern.append(s)
                neighborhood.append(new_pattern)
        elif pattern[i] == "C":
            for s in "AGT":
                new_pattern = pattern
                new_pattern.append(s)
                neighborhood.append(new_pattern)
        elif pattern[i] == "G":
            for s in "ACT":
                new_pattern = pattern
                new_pattern.append(s)
                neighborhood.append(new_pattern)
        else:
            for s in "ACG":
                new_pattern = pattern
                new_pattern.append(s)
                neighborhood.append(new_pattern)
    return neighborhood

