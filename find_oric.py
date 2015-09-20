
def plot_skew(genome):
    skew = [0]
    for i in range(0,genome.__len__()):
        if genome[i] == "G":
            skew.append(skew[i]+1)
        elif genome[i] == "C":
            skew.append(skew[i]-1)
        else:
            skew.append(skew[i])
    return skew

def find_min_skew(list):
    min_skew = []
    for i in range(0,len(list)):
        if list[i] == min(list):
            min_skew.append(i)
    return min_skew



