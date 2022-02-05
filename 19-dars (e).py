# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:19:45 2022

@author: User
"""


def bolinish_alomatlari(son):
    for n in range(2,11):
        if son%n==0:
            print(f"{son} {n} ga qoldiqsiz bo\'linadi")
        else:
            print(f"{son} hech qanday songa bo\'linmaydi")
            
bolinish_alomatlari(11)

    