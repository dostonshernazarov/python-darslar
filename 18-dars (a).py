# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 11:56:23 2022

@author: User
"""

mahsulotlar = {
    'telefon':2000000,\
    'apple':15000000,\
    'hp':10000000,\
    'airpots':200000,\
 }
    
while True:
    nom = input('Mahsulot nomini kiriting:')
    narh = input(f"{nom}ning narhini kiriting:")
    narh=int(narh)
    savol=input('Yana mahsulotlar kiritasizmi?(ha\yo\'q):')
    mahsulotlar[nom]=narh
    if savol !='ha':
        break
print('Raxmat')