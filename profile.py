
def profile_most_probable(text,k,A,C,G,T):
    most_p = 0
    A = A.split()
    for i in range(0,A.__len__()):
        A[i] = float(A[i])
    C = C.split()
    for i in range(0,C.__len__()):
        C[i] = float(C[i])
    G = G.split()
    for i in range(0,G.__len__()):
        G[i] = float(G[i])
    T = T.split()
    for i in range(0,T.__len__()):
        T[i] = float(T[i])
    for i in range(0,len(text)-k+1):
        pattern = text[i:i+k]
        profile = 1
        for j in range(0,pattern.__len__()):
            if pattern[j] == "A":
                profile *= A[j]
            elif pattern[j] == "C":
                profile *= C[j]
            elif pattern[j] == "G":
                profile *= G[j]
            else:
                profile *= T[j]
        if profile > most_p:
            most_p = profile
            pmp = pattern
    return pmp



