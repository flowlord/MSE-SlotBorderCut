# -*- coding: utf-8 -*-
"""
    INPUT --> A --> B --> C --> output

    I) Bloc A
        Le texte est légèrement modifié.

    II) Bloc B
        Chaque caractère est substitué.

    II) Bloc C
        Complexifie le code après la substitution.
"""

from pyperclip import copy
from parametre import*
from random import randint,choice
from subdiv import change_place,change_place_ins

try:
    from keylib import listkey,getRandomKey
except ModuleNotFoundError:
    from keylib_generator import gen_lib_cle
    gen_lib_cle(randint(nombre_cle[0],nombre_cle[1]))
    from keylib import listkey,getRandomKey


def check_word(text):
    """
    vérifie si un mot est dans la list de mot
    """

    text = text.split(' ')

    v = []

    for element in text:
        if element in liste_mots:
            v = v + [0]
        else:
            v = v + [1]

    if 1 in v:
        return False
    else:
        return True


def check_char(msg):
    """
    vérifie si un caratère est dans la variable caractere_sub
    
    """
    msg = list(msg)
    
    v = []
    
    for ch in msg:
        if ch not in caractere_sub:
            v = v + [0]
    
    return 0 in v


def milieu(char):
    """
    abcd --> nombre de carcatères --> 4 --> 4/2 ---> 2
    """
    return int(len(char)/2)


"""
    I) Bloc A
        Le text est légèrement modifier.
"""


def complex(plain_text):
    """ 
        Modifie légèrement le text
        example:
            hello word ---> rowdl lehol
    """
    
    plain_text =  plain_text[::-1]
    
    return plain_text


def decomplex(coded_text):
    """ 
        Remet le text dans me bon sens
        example:
            rowdl lehol ---> hello world
    """
    coded_text =  coded_text[::-1]
    return coded_text

#-----------------------------------------------------------------------------------------

"""
    II) Bloc B
        Chaque carcatère est subtitué.
"""

def cipher(plain_text):
    """
    Je prend une clé au hazard et subtitue les caractères
    """
    plain_text = plain_text.lower()
    reversed_key = choice([True,False])
    key = getRandomKey()
    
    if reversed_key is True:
        key.reverse()

    for letter in range(nbr_lettre_sub):
        plain_text = plain_text.replace(caractere_sub[letter],key[letter][1])
        
    return plain_text


def deconfuse(code):
    """
    Enlève les carcatères du groupe b
    """
    new_text = ""
    for element in code:
        if element not in groupe_b:
            new_text = new_text + element  
    return new_text


def decipher_basic_reverse(coded_msg):
    """
    Déchiffre le message avec une clé inverser
    """
    for key in listkey:
        key.reverse()
        for element in range(nbr_lettre_sub):
            coded_msg = coded_msg.replace(key[element][1],caractere_sub[element])
    
    coded_msg = decomplex(coded_msg)
    coded_msg = change_place_ins(coded_msg)
    
    return coded_msg


def decipher(coded_msg):
    """
    Essaie déchiffrer le message
    """
    original_code = coded_msg
    
    for key in listkey:
        for element in range(nbr_lettre_sub):
            coded_msg = coded_msg.replace(key[element][1],caractere_sub[element])
    
    coded_msg = decomplex(coded_msg)
    
    if check_word(coded_msg) is False:
        return decipher_basic_reverse(original_code)
    else:
    	coded_msg = change_place_ins(coded_msg)
    	return coded_msg

#-----------------------------------------------------------------------------------------

"""
    II) Bloc C
        Complexifie le code après la subtitution.
"""


def chaos(plain_text,x):
    """
        Ajoute de manière aléatoire un caractère du groupe_b
        dans le code dans une position au hazard x fois.
    """
    plain_text = list(plain_text)
    
    for _ in range(x):
        getRandCharac = choice(groupe_b)
        pos = randint(0,len(plain_text))
        
        plain_text.insert(pos, getRandCharac)

    plain_text = ''.join(plain_text)
    return plain_text

#-----------------------------------------------------------------------------------------

def mse_cipher(msg):
    plain_text = change_place(msg)
    print(plain_text,'\n\n')
    
    coded  = complex(msg)
    coded = cipher(coded)
    coded = chaos(coded,randint(fa,fb))

    copy(coded)
    return coded


def mse_decipher(coded_msg):
    msg = deconfuse(coded_msg)
    msg = decipher(msg)
    
    msg = change_place_ins(msg)

    return msg



