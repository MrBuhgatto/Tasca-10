#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Joc del MasterMind versió reduïda

import random

#Generem un codi aleatori de 4 xifres entre 0 i 9
codi = "".join(list(map(lambda x: str(x), random.sample(range(0, 9), 4))))
print(""" Això és el teu primer Mastermind
       	Has d'adivinar un número de 4 xifres diferents.
       	""")
latevaproposta = input("Introduexi un codi de 4 xifres: ")
#Bucle fins que s'endevini el codi
intents = 0
while latevaproposta != codi:
    intents += 1
    encerts = 0
    coincidencies = 0
    #Verifiquem els encerts i coincidències en la proposta
    for i in range(4):
        if latevaproposta[i] == codi[i]:
            encerts += 1
        elif latevaproposta[i] in codi:
            coincidencies += 1
    print("La teva proposta (", latevaproposta, ") te", encerts, "encerts i", coincidencies, "coincidències.")
    #Sol·licitem una nova proposta
    latevaproposta = input("Torna a introduir un codi de 4 xifres: ")
print("Felicitats! Has endevinat el codi en ", intents, "intents.")
