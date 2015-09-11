

def findreverse(text):
    rev_text = ""
    for i in text:
        if i == "A":
            rev_text += "T"
        elif i == "T":
            rev_text += "A"
        elif i == "C":
            rev_text += "G"
        else:
            rev_text += "C"
    rev_complement = ""
    for i in rev_text:
        rev_complement = i + rev_complement
    return rev_complement



