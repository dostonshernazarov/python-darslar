# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 14:42:38 2022

@author: User
"""

dictionary = {
    'title':'so\'zning birinchi harfini katta qilib yozadi',\
    'lower':'harfni kichik qilib yozadi',\
    'upper':'harfni katta qilib yozadi',\
    'float':'o\'nlik son qilib yozadi',\
    'intiger':'birlik son qilib yozadi',\
    'if':'agarda tarjimasini beradi',\
    'elif':'aks holda, agarda degani',\
    'else':'aks holda degani',\
    'string':'matn ko\'rinishida chiqaradi',\
    'lstrip':'chao tarafga matnni suradi',\
    'rstrip':'o\'ng tarafga matnni suradi',\
 }
word = input('Kalit so\'z kiriting:').lower()
#print(dictionary.get(word))
tarjima = dictionary.get(word)

if tarjima==None:
    print('Bunday so\'z mavjud emas')
    
else:
    print(f"{word.lower()} so'zining vazifasi {tarjima} ")