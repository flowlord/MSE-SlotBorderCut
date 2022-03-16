from pyperclip import copy
from gen_init import*
from random import randint,choice
from keylib import listkey,getRandomKey
from subdiv import change_place,change_place_ins


def cipher(plain_text):

	plain_text = change_place(plain_text)

	print(plain_text,'\n\n')

	plain_text = plain_text.lower()
	key = getRandomKey()


	for letter in range(nbr_letter_sub):
		plain_text = plain_text.replace(charac_sub[letter],key[letter][1])
	 

	copy(plain_text)
	return plain_text


def decipher(coded_msg):
    original_code = coded_msg
    
    for key in listkey:
        for element in range(nbr_letter_sub):
            coded_msg = coded_msg.replace(key[element][1],charac_sub[element])
    
    
    return coded_msg

   
def chaos(plain_text,x):
    """Add randomly characters from group_b to plain_text
      in a randomly chosen position, x times.
    """
    plain_text = list(plain_text)
    
    for _ in range(x):
        getRandCharac = choice(group_b)
        pos = randint(0,len(plain_text))
        
        plain_text.insert(pos, getRandCharac)

    plain_text = ''.join(plain_text)
    return plain_text


def deconfuse(code):
    """
    create a new character string without the 
    characters that are in anti_pat
    """
    new_text = ""
    for element in code:
        if element not in group_b:
            new_text = new_text + element  
    return new_text


def mse_cipher(msg):
    coded = cipher(msg)
    coded = chaos(coded,randint(900,1500))
    
    return coded


def mse_decipher(coded_msg):
    msg = deconfuse(coded_msg)
    msg = decipher(msg)
    msg = change_place_ins(msg)

    return msg


example_sentences = ['meeting tonight for speak','hello world','see you at night','where do you live',
			'What do you do','see you soon','see you next week','see you on monday',
			'see you tomorrow','have a good weekend','i will do that later',
			'i can talk to you','we can see each other','im afraid im busy then',
            'you can help me do my homework','they are there','so far so good']


m = mse_cipher("have a good weekend")
print(m,'\n\n')
print(mse_decipher(m))


