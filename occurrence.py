

def find_pattern(genome, pattern):
    positions = []
    for i in range(0, len(genome) - len(pattern) +1):
        if genome[i: i+len(pattern)] == pattern:
           positions += [i]
    return positions

