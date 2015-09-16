
def symbol_to_number(s):
    if s == "A":
        return 0
    elif s == "C":
        return 1
    elif s == "G":
        return 2
    elif s == "T":
        return 3
    else:
        print("Wrong symbol! Check the genome please.")
        return -1

def number_to_symbol(n):
    if n == 0:
        return "A"
    elif n == 1:
        return "C"
    elif n == 2:
        return  "G"
    elif n == 3:
        return "T"
    else:
        print("Wrong number!")
        return "ERROR"

def last_symbol(pattern):
    return pattern[-1]

def prefix(pattern):
    return pattern[0:-1]

def p_to_n_modify(pattern):
    if len(pattern) == 0:
        return 0
    symbol = last_symbol(pattern)
    p = prefix(pattern)
    return 4 * p_to_n_modify(p) + symbol_to_number(symbol)


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


def n_to_p_modify(index, k):
    if k == 1:
        return number_to_symbol(index)
    prefixindex = int(index/4)
    r = index % 4
    symbol = number_to_symbol(r)
    prefixpattern = n_to_p_modify(prefixindex, k-1)
    return prefixpattern + symbol


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




