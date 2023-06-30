import genere_liste
import multiprocessing
import chifrement as chiff
import dechifferement as dechiff



def calcul_lm(m, i):
    
    return (chiff.chiffrement(m,i), i)

def calcul_lc(c, i):
    
    return (dechiff.dechiffrement(c,i), i)

def listes(liste_m,liste_c):
    """
    Je calcule en parallèle les liste lm et lc avec 4 processus, 2 pour chaque liste 
    """


    pool = multiprocessing.Pool(5) # Créer une piscine de 5 processus
    lm1 = pool.starmap(calcul_lm, liste_m[:2**23])
    lc1 = pool.starmap(calcul_lc, liste_c[:2**23]) 
    lm2 = pool.starmap(calcul_lm, liste_m[2**23::])
    lc2 = pool.starmap(calcul_lc, liste_c[2**23::])
    pool.close()
    pool.join()
    lm = lm1 + lm2
    lc = lc1 + lc2

    lm.sort() # Trier lm
    lc.sort() # Trier lc



    return lm, lc


def recherche_commun(lm, lc):
    i, j = 0, 0
    collision = 0

    k1_k2_retourner = []
    n = 2**24
    while(i < n and j < n):
        if lc[i][0] < lm[j][0]:
            i += 1
        elif lm[j][0] < lc[i][0]:
            j += 1
        else:
            collision += 1
        
            k1_k2_retourner.append((lm[j][1], lc[i][1]))
            print(f"Clé secrète trouvée: (cle1, cle2): ({lm[j][1]}, {lc[i][1]})")
  
            # cas où plusieurs éléments à la suite d'une même liste sont égaux
            if j+1 < n and lm[j+1][0] == lc[i][0]:
                j += 1
            elif i+1 < n and lm[j][0] == lc[i+1][0]:
                i += 1
            else:
                i += 1
                j += 1  
    print(f"recherche terminée avec {collision} collision")
    return k1_k2_retourner


if __name__ == '__main__':
    m = 'e0eab1'
    c = '1e40e2'

    liste_m = genere_liste.genere_m(m)
    liste_c = genere_liste.genere_c(c)

    lm, lc =listes(liste_m,liste_c)

    print(recherche_commun(lm,lc))
