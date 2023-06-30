def genere_m(m): 
    l = []
    for i in range(2**(24)):
        l.append((m,hex(i)[2::].zfill(6)))
    return l

def genere_c(c): 
    l = []
    for i in range(2**(24)):
        l.append((c,hex(i)[2::].zfill(6)))
    return l
