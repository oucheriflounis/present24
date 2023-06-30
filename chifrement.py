import cadencement as cad
# S-Box utilisée pour la substitution non-linéaire
Sbox = {
    '0x0' :0xc,
    '0x1' :0x5,
    '0x2' :0x6,
    '0x3' :0xB,
    '0x4' :0x9,
    '0x5' :0x0,
    '0x6' :0xa,
    '0x7' :0xd,
    '0x8' :0x3,
    '0x9' :0xe,
    '0xa' :0xf,
    '0xb' :0x8,
    '0xc' :0x4,
    '0xd' :0x7,
    '0xe' :0x1,
    '0xf' :0x2
}

#tableau de permutation 
pos_permu = [0, 6, 12, 18, 1, 7, 13, 19, 2, 8, 14, 20, 3, 9, 15, 21, 4, 10, 16, 22, 5, 11, 17, 23]


#fonction change en hex


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


def chiffrement(etat, cle):
    etat = bin(int(etat,16))[2::].zfill(24)

    for _ in range(20-len(cle)):
        cle += '0'

    cle = hex(int(cle,16))[2::].zfill(20)


    cle = bin(int(cle,16))[2::].zfill(80)

    sous_cles = cad.cadencement(cle)

    #print('Tour i | Etat   | Sous-cle Ki')
    for i in range(10):
        #Etat ← Etat ⊕ K_i
        #print('{} | {} | {}'.format(i+1, hhhhh(etat)[2::].zfill(6) , hhhhh(sous_cle[i])[2::].zfill(6)))
        etat = xor_chiff(list(etat),"".join(sous_cles[i]))
        

        #Substitution de l'état
        etat = substitution_chiff(etat, Sbox)
        

        # permutation de l'état
        etat = permutation(etat, pos_permu)
        etat = "".join(etat)
        
       
    #print('{} | {} | {}'.format('11 ', hhhhh(etat)[2::].zfill(6) , hhhhh(sous_cle[10])[2::].zfill(6)))
    etat = xor_chiff(list(etat),"".join(sous_cles[10]))
    c = hex(int(etat,2))
    return ''.join(c)


"""
#main
 # nombre en base 16

msg_1 = 'ffffff'
msg_2 = '000000'
msg_3 = 'f955b9'

cle_1 = '000000'
cle_2 = 'ffffff'
cle_3 = 'd1bd2d'

cle = cle_1
etat = msg_2



etat = bin(int(etat,16))[2::].zfill(24)



for _ in range(20-len(cle)):
    cle += '0'

cle = hex(int(cle,16))[2::].zfill(20)


cle = bin(int(cle,16))[2::].zfill(80)



chiffrer =''.join(chiffrement(etat,cle))
print('chiffrer' ,chiffrer)
"""
