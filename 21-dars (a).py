# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:53:05 2022

@author: User
"""

def talabalar(ism, familiya, **malumotlar):
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar

print(talabalar('doston', 'shernazarov', t_yil=2001, kurs=3))  
        
