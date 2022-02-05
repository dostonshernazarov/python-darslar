# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:54:40 2022

@author: User
"""

ism = input("Ismingizni yozing:")
t_yil=int(input('Tug\'ulgan yilingizni yozing:'))


def yosh_hisobla(tugulgan_yil, joriy_yil=2022):
    """Foydalanuvchining tug\'ulga yili kiritilsa,
    yoshini hisoblab beruvchi funksiya"""
    print(f"{ism.title()} hozir {joriy_yil-tugulgan_yil}yoshda")
    
yosh_hisobla(t_yil)