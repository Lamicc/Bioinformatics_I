
def symbol_to_number(s):
    if s == "A":
        n = 0
    elif s == "C":
        n = 1
    elif s == "G":
        n = 2
    elif s == "T":
        n = 3
    else:
        print("Wrong symbol! Check the genome please.")
    return n


def pattern_to_number(pattern):
    index = []
    rmargin= len(pattern)-1

    for i in range(0, len(pattern)):
        order = rmargin - i
        index += [symbol_to_number(pattern[i]) * pow(4, order)]

        '''
        if pattern[i] == "A":
            index += [0 * pow(4,order)]
        elif pattern[i] == "C":
            index += [1 * pow(4,order)]
        elif pattern[i] == "G":
            index += [2 * pow(4, order)]
        else:
            index += [3 * pow(4, order)]
        '''
    number = sum(index)
    return number



def number_to_pattern(number, k):
    pattern = ""
    total = number

    for i in range(0,k):

        if total >= 3 * pow(4, k-i-1):
            pattern += "T"
            total -= 3 * pow(4, k-i-1)
            #print(total)
        elif total >= 2 * pow(4, k-i-1):
            pattern += "G"
            total -= (2 * pow(4, k-i-1))
            #print(total)
        elif total >= 1 * pow(4, k-i-1):
            pattern += "C"
            total -= (1 * pow(4, k-i-1))
            #print(total)
        else:
            pattern += "A"


    return pattern




