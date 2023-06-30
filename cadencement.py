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


# fonction de substitution qui prend en entrée 4bits
# et qui donne en sortie 4bits
def substitution(l_cle , Sbox):
    
    tmp = "".join(l_cle)
    tmp = hex(int(tmp,2))
    
    tmp = hex(Sbox[tmp])
    
    tmp = bin(int(tmp,16))[2:].zfill(4)
    assert len(tmp) == 4
    return list(tmp)


def new_xor(l_cle, val):
    x_tab = []
    
    for i in range(len(l_cle)):
        x_tab.append(str(int(l_cle[i])^int(val[i])))
    
    return x_tab


# fonction xor 
def xor(l_cle,val):
    
    l_cle = "".join(l_cle)
    l_cle = int(l_cle , 2)
    val = "".join(val)
    val = int(val , 2)
  
    l_cle = l_cle ^ val
    l_cle = bin(l_cle)[2::].zfill(5)
    
    return list(l_cle)




#fonction qui implémente l'algorithme de cadencement de clé
def cadencement(cle):

    for _ in range(20-len(cle)):
        cle += '0'

    cle = hex(int(cle,16))[2::].zfill(20)
    cle = bin(int(cle,16))[2::].zfill(80)


    liste_cle = []
    master_key = list(cle)
    for j in range(1,12):

        tmp = master_key[40:64]
       
        
        liste_cle.append(tmp)
        """print( j,' | ',hhhhh(tmp)[2::].zfill(6))"""

        #partie rotation
       
        master_key = rotation(master_key)
        
        #partie substitution
        #l = master_key[0:4]
        
        l = substitution(master_key[0:4] , Sbox)
        master_key[0:4]= l

        #partie xor
        #l = master_key[60:65]
        
        val = bin(j)[2::].zfill(5)
        val = list(val)
        l = new_xor(master_key[60:65],val)
          
        master_key[60:65] = l
       
        # liste de sous clés
       

        

    return liste_cle



cle = '000000'
for _ in range(20-len(cle)):
    cle.join('0')
cle = hex(int(cle,16))[2::].zfill(20)


cle = bin(int(cle,16))[2::].zfill(80)

sous_cle = cadencement(cle)
