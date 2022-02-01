# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 14:42:38 2022

@author: User
"""

davlatlar = {
    'aqsh':'vashington',\
    'fransiya':'parij',\
    'hindiston':'pekin',\
    'rossiya':'moskva',\
    'italiya':'rim'
    }
    
an = input('Qaysi davlat poytaxtini bilishni istaysiz?: ').lower()

country = davlatlar.get(an)
if country==None:
    print('Bunday malumot yo\'q')
else:
    print(f"{an.upper()}ning poytaxti {country.title()}")
#print('Dunyo davlatlari:')
#for davlat in sorted(davlatlar):
 #   print(davlat.title())
    
#print('Davlat poytaxtlari:')
#for poytaxt in sorted(davlatlar.values()):
 #   print(poytaxt.title())