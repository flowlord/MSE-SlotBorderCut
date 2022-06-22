#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MSE (multiple substitution encryption)

version Border Slot Cut using subdiv (https://github.com/flowlord/subdiv8)

Créer le 16 mars 2022

@author: FLOW LORD

Follow my twitter: https://twitter.com/flowlord_

version: BSC 1
version name: NARVAL

site web: https://solarissoftwarebulares.fun/

Attention:
-----------------
ouvrir le fichier keylib.py peut faire bugger votre IDE !
supprimer le dossier __pycache__ avant de regénèrer vos clés
"""


from MSE import mse_cipher,mse_decipher

example_phrase = ['meeting tonight for speak','rendez vous ce soir pour parler','hello world','on se voit ce soir','ou habitez vous',
			'que faites vous','a bientot','à la semaine prochaine','je peux te parler','on peut se voir','jusqu ici tout va bien']

def chiffrer_plusieurs_messages(liste):
	for message in liste:
		print(mse_cipher(message),'\n')


def déchiffrer_plusieurs_messages(liste):
	for message in liste:
		print(mse_decipher(message),'\n')


def demo():
	print('Text chiffré:\n')
	message = mse_cipher('meeting tonight for speak')
	print(message,'\n\n')

	print('Texte déchiffré:\n')
	print(mse_decipher(message))

demo()


