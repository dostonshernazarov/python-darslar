# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:14:47 2022

@author: User
"""

son0=int(input("Son kiriting:"))

def sonni_aniqla(son):
    """ Kiritilgan sonning juft yoki toqligini aniqlaydiga funsiya"""
    if son%2==0:
        print(f"{son0} juft son")
    else:
        print(f"{son0} toq son")
        
sonni_aniqla(son0)