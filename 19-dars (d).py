# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:19:45 2022

@author: User
"""

x=int(input("'x' ning qiymatini kiriting:"))
y=int(input("'y' ning qiymatini kiriting"))

def sonni_aniqla(son1, son2):
   """ 'x' soninong 'y'inchi darajasini hisoblaydiga funksiya """
   print(f"{son1} ning {son2} inchi darajasi{son1**son2} ga teng")
   
sonni_aniqla(x, y)