from hamming_distance import compute_hd
import random

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
        count = A[i]
        nuco = "A"
        if C[i] > count:
            count = C[i]
            nuco = "C"
        if G[i] > count:
            count = G[i]
            nuco = "G"
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
    A = [1] * k
    C = [1] * k
    G = [1] * k
    T = [1] * k
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
    #profile with Laplace’s Rule
    for i in range(k):
        A[i] = A[i]/(2*t)
        C[i] = C[i]/(2*t)
        G[i] = G[i]/(2*t)
        T[i] = T[i]/(2*t)
    return [A,C,G,T]

def pr(pattern,prof):
    p = 1
    for i in range(0,pattern.__len__()):
        if pattern[i] == "A":
            p *= prof[0][i]
        elif pattern[i] == "C":
            p *= prof[1][i]
        elif pattern[i] == "G":
            p *= prof[2][i]
        else:
            p *= prof[3][i]
    return p

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

def randomized_motif_search(dna,k,t):
    motifs = []
    for i in range(t):
        index = random.randrange(0,len(dna[i])-k+1,1)
        motifs.append(dna[i][index:index+k])
    best_motifs = motifs[:]
    #print(score(best_motifs,find_consensus(best_motifs)))
    while 1:
        prof = profile(motifs)
        for i in range(t):
            motifs[i] = profile_most_probable(dna[i],k,prof)
        if score(motifs,find_consensus(motifs)) < score(best_motifs,find_consensus(best_motifs)):
            #print(score(motifs,find_consensus(motifs)))
            best_motifs = motifs[:]
        else:
            return best_motifs

def Random(values,probabilityDistribution):
    wheel = [0]*(len(probabilityDistribution)+1)
    s = sum(probabilityDistribution)
    """normalization in case where probabilityDistribution is not normalized """
    if s!=1:
        probabilityDistribution = [(1.*x)/s for x in probabilityDistribution]
    """creating the roulette wheel """
    for i, prob in enumerate(probabilityDistribution):
        wheel[i+1] = wheel[i] + prob
    """spinning the wheel """
    r = random.random()
    result = 0
    for i in range(len(wheel)-1):
        if r > wheel[i] and r < wheel[i+1]:
            result = values[i]
    return result

def gibbs_sampler(dna, k, t, N):
    motifs = []
    for i in range(t):
        index = random.randrange(0,len(dna[i])-k+1,1)
        motifs.append(dna[i][index:index+k])
    best_motifs = motifs[:]
    for j in range(1,N+1):
        i = random.randint(0,t-1)
        mo = motifs[:i] + motifs[i+1:]
        prof = profile(mo)
        p_rand = []
        for e in range(0,len(dna[i])-k+1):
            p_rand.append(pr(dna[i][e:e+k],prof))
        v = [int(rint) for rint in range(len(dna[i])-k+1)]
        position = Random(v,p_rand)
        motifs[i] = dna[i][position:position+k]
        if score(motifs,find_consensus(motifs)) < score(best_motifs,find_consensus(best_motifs)):
            best_motifs = motifs[:]
    return best_motifs





































