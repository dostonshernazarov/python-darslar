# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 15:47:09 2022

@author: User
"""

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    
    if float(qiymat)<0:
        print('Bu sonning ildizi xato')
        continue
       
    elif qiymat=='exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")