from neighbor import neighbors
from pattern_count import patterncount_with_mismatchs

def motif_enumeration(dna, k, d):
    patterns = []
    for slice in dna:
        for i in range(0,len(slice)-k +1):
            neighborhood = set(neighbors(slice[i:i+k],d))
            for pattern in neighborhood:
                count = 0
                for slice_II in dna:
                    if patterncount_with_mismatchs(slice_II,pattern,d) > 0:
                        count += 1
                if count >= len(dna):
                    patterns.append(pattern)
    patterns = set(patterns)
    return patterns







