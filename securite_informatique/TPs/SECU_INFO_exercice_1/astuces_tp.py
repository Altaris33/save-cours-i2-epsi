#!/usr/bin/python2.7
# le compteur n'est pas incrémenté, donc erreur d'implémentation
# faiblesse: car il n'y a pas la clé
# fichier texte avec chaque ligne chiffrée
# elles sont chiffrée les unes à la suite des autres (boucle for)
    # on vérifie que la ligne n'est pas vide
    # on chiffre et on écrit la ligne chiffrée en sortie
    # une ligne chiffré = la ligne en clair
    # chercher dans la version de la lib Cipher et examiner le prototype de la function utilisée
    # erreur sur le compteur (counter = nonce), on passe une valeur fixe au lieu d'un iterable
    # CTR : chiffrement symétrique par bloc avec AES sur 128 bits: 
        # on xor le bloc de texte crypté avec un key: on obtient le keystream (résultat), en chiffrant le compteur avec la clé au préalable
        # chaque bloc fera 4 characters (AES 128), pour chaque ligne lue
        # c'est toujours le même compteur qui est utilisé (erreur)
        # en sortie du chiffrement on obtient toujours le même résultat -> chaque bloc en clair (texte clair) est XORé avec la même clé (keystream)
            # propriété du XOR(Boole) -> P1 xor k = C1, P2 xor k = C2 = P1 xor C1, P2 xor c2... donc => P1 = P2 xor C2 xor C1. On a techniquement plus besoin de la clé. Attaque au clair choisi
            # on peut donc renseigner un P2 et chercher à déduire P1

# -> cyberchef (outil en ligne pour conversion & encodage)            
            # 1 octet = 2 characters -> 4 octets = 8 characters
            # Exemple: fe 45 e4 32
            # on décode le crypté en base 64 puis on converti en hexa
            # essayer de faire correspondre pour la ligne n+1 un mot de la ligne précédente et dégager toute la phrase
# executer le script python avec deux argument: nomDuScript nomDuFichierAEncoder


# Fichier décrypté trouvé: The jargon file contains a bunch of...             