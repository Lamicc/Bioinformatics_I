from P_to_N import pattern_to_number, number_to_pattern

def computingfrequencies(text, k):
    frequencyArray = []
    for i in range(0, pow(4, k)):
        frequencyArray.append(0)
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i+k]
        j = pattern_to_number(pattern)
        frequencyArray[j] += 1

    return frequencyArray
