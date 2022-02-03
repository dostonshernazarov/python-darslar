# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 15:47:09 2022

@author: User
"""

savol = 'Yoshingi nechida:'

while True:
    qiymat=input(savol)
    if qiymat=='exit' or qiymat=='quit':
        break
    yosh = int(qiymat)
    
    if yosh<7:
        narh=2000
        
    elif 7<=yosh<18:
        narh=3000
        
    elif 18<=yosh<65:
        narh=1000
        
    else:
        narh=0
        
    if narh==0:
        print("Sizga chipta bepul")
    else:
        print(f"Chipta narhi {narh} so\'m")