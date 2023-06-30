import cadencement as cad

#inversion sbox
Sbox_inv = {
    '0x0' :0x5,
    '0x1' :0xe,
    '0x2' :0xf,
    '0x3' :0x8,
    '0x4' :0xc,
    '0x5' :0x1,
    '0x6' :0x2,
    '0x7' :0xd,
    '0x8' :0xb,
    '0x9' :0x4,
    '0xa' :0x6,
    '0xb' :0x3,
    '0xc' :0x0,
    '0xd' :0x7,
    '0xe' :0x9,
    '0xf' :0xa
}

#inversion tab permu
permu_inv = [0, 4, 8, 12, 16, 20, 1, 5, 9, 13, 17, 21,
             2, 6, 10, 14, 18, 22, 3, 7, 11, 15, 19, 23]




#fonction change en hex
def hhhhh(l_cle):
    tmp = "".join(l_cle)
    
    tmp = hex(int(tmp,2))
    return tmp

# fonction qui permet d'effectuer la rotation d'une liste
# de 61 positions vers la gauche
def rotation(cle):
    b = list(cle)
    b = b[61::] + b[0:61] 
    return b


def xor_chiff(l_cle,val):
    taille  = max(len(l_cle),len(val))
    l_cle = "".join(l_cle)
    l_cle = int(l_cle , 2)
    val = "".join(val)
    val = int(val , 2)
  
    l_cle = l_cle ^ val
    l_cle = bin(l_cle)[2::].zfill(taille)
    return l_cle


def substitution_chiff(l_cle , Sbox):
    tmp = "".join(l_cle)
    tmp = hex(int(tmp,2))[2::].zfill(6)
    tmp = list(tmp)
    
    
    for i in range(len(tmp)):
        res = tmp[i]
        res = hex(int(res,16))
        tmp[i] = hex(Sbox[res])[2::]
    
    tmp = "".join(tmp)
    tmp = bin(int(tmp,16))[2::].zfill(24)
    
    
    
    return tmp


# permutation bit a bit selon la table P(i)
def permutation(etat, pos_permu):
    etat_tmp =['0']*24
    for i in range(24):
        t = pos_permu[i]
        etat_tmp[t] = etat[i]
    return etat_tmp



def dechiffrement(etat, cle):
    etat = bin(int(etat,16))[2::].zfill(24)



    for _ in range(20-len(cle)):
        cle += '0'

    cle = hex(int(cle,16))[2::].zfill(20)


    cle = bin(int(cle,16))[2::].zfill(80)





    sous_cles = cad.cadencement(cle)

    
    # Etat ← Etat ⊕ K_11
    etat = xor_chiff(etat, "".join(sous_cles[10]))
    
    for i in range(9, -1, -1):
        #print('{} | {} | {}'.format(i+1, hhhhh(etat)[2::].zfill(6) , hhhhh(sous_cle[i])[2::].zfill(6)))

        # substitution et permutation inverse
        etat = permutation(etat, permu_inv)        
        etat = substitution_chiff(etat, Sbox_inv)
        # Etat ← Etat ⊕ K_i
        etat = xor_chiff(etat, "".join(sous_cles[i]))
    
    m = hex(int(etat,2))
    return ''.join(m)



"""

#main
 # nombre en base 16

cle_1 = '000000'
cle_2 = 'ffffff'
cle_3 = 'd1bd2d'

c1 = 'bb57e6'
c2 = '739293'
c3 = '1b56ce'
c4 = '47a929'

cle = cle_1
etat = c1



etat = bin(int(etat,16))[2::].zfill(24)



for _ in range(20-len(cle)):
    cle += '0'

cle = hex(int(cle,16))[2::].zfill(20)


cle = bin(int(cle,16))[2::].zfill(80)






sous_cle = cad.cadencement(cle)
#print('sous cles ; \n',sous_cle)


dechiffrer = ''.join(dechiffrement(etat, sous_cle))
print('dechiffrer', dechiffrer)
"""
