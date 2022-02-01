# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 14:42:38 2022

@author: User
"""

minu = {'osh':15000,\
 'shashlik':8000,\
 'non':3000,\
 'sho\'rva':12000,\
 'norin':20000,\
 'somsa':10000,\
 'manti':8000,\
 'lavash':25000,\
}
                 
print("3 ta taom buyurtma bering")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-buyurtmani kiriting:"))
    
for buyurtma in buyurtmalar:
    if buyurtma in minu:
        print(f"{buyurtma} {minu[buyurtma]} so\'m")
else:
    print(f"Bizda {buyurtma} yo\'q")
    
    
