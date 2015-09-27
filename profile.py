from hamming_distance import compute_hd

def profile_most_probable(text,k,prof):
    most_p = 0
    pmp = text[:k]
    A = prof[0]
    C = prof[1]
    G = prof[2]
    T = prof[3]
    """
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
    """
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

def find_pmp(motifs):
    pmp = ""
    t = len(motifs)
    k = len(motifs[0])
    A = [0] * k
    C = [0] * k
    G = [0] * k
    T = [0] * k
    for i in range(0,t):
        for j in range(0,k):
            if motifs[i][j] == "A":
                A[j] += 1/t
            elif motifs[i][j] == "C":
                C[j] += 1/t
            elif motifs[i][j] == "G":
                G[j] += 1/t
            else:
                T[j] += 1/t
    most_prob = 0
    for i in range(0,t):
        prob = 1
        for j in range(0,k):
            if motifs[i][j] == "A":
                prob *= A[j]
            elif motifs[i][j] == "C":
                prob *= C[j]
            elif  motifs[i][j] == "G":
                prob *= G[j]
            else:
                prob *= T[j]
        if prob > most_prob:
            most_prob = prob
            pmp = motifs[i]
    return  pmp

def find_consensus(motifs):
    t = len(motifs)
    k = len(motifs[0])
    A = [0] * k
    C = [0] * k
    G = [0] * k
    T = [0] * k
    for i in range(0,t):
        for j in range(0,k):
            if motifs[i][j] == "A":
                A[j] += 1
            elif motifs[i][j] == "C":
                C[j] += 1
            elif motifs[i][j] == "G":
                G[j] += 1
            else:
                T[j] += 1
    consensus = ""
    nuco = ""
    for i in range(0,k):
        count = 0
        if A[i] > count:
            count = A[i]
            nuco = "A"
        if C[i] > count:
            count = C[i]
            nuco = "C"
        if G[i] > count:
            count = G[i]
            nuco = "C"
        if T[i] > count:
            nuco = "T"
        consensus += nuco
    return consensus

def score(motifs,consensus):
    score = 0
    for motif in motifs:
        score += compute_hd(motif,consensus)
    return score

def profile(motifs):
    #print(motifs)
    t = len(motifs)
    k = len(motifs[0])
    A = [0] * k
    C = [0] * k
    G = [0] * k
    T = [0] * k
    for i in range(0,t):
        for j in range(0,k):
            if motifs[i][j] == "A":
                A[j] += 1/t
            elif motifs[i][j] == "C":
                C[j] += 1/t
            elif motifs[i][j] == "G":
                G[j] += 1/t
            else:
                T[j] += 1/t
    return [A,C,G,T]

def greedy_motif_search(dna,k,t):
    best_motif = []
    motif = ["" for n in range(t)]
    for text in dna:
        best_motif.append(text[0:k])
    for i in range(0,len(dna[0])-k+1):
        mf = dna[0][i:i+k]
        motif[0] = mf
        for j in range(1,t):
            prof = profile(motif[:j])
            p_m_p = profile_most_probable(dna[j],k,prof)
            motif[j] = p_m_p
        if score(best_motif,find_consensus(best_motif)) > score(motif,find_consensus(motif)):
            best_motif = motif[:]
    return best_motif





























