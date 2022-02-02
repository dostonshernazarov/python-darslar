# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 12:48:59 2022

@author: User
"""
nom = input('Davlat nomini kiriting:').lower()


davlatlar = {
    'o\'zbekiston':{'aholi':35000000,\
                    'hudud':448978,\
                    'pul':'so\'m',\
                    'poytaxt':'toshkent'
                    },\
    'rossiya':{'aholi':145000000,\
               'hudud':17089246,\
               'pul':'publ',\
               'poytaxt':"moskva"
              },\
    'aqsh':{'aholi':328000000,\
            'hudud':9631418,\
            'pul':"dollar",\
            'poytaxt':'vashington'
            }
    }
if nom in davlatlar:
    info=davlatlar[nom]   
    print(f"\n{nom.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi:{info['hudud']}"
          f"\nAholisi:{info['aholi']}"
          f"\nPul birligi:{info['pul']}")
else:
    print('Bunday davlat haqida ma\'lumot yo\'q')
#for davlat, info in davlatlar.items():
   # if davlat.lower()=='aqsh':
       # davlat=davlat.upper()
    #else:
        #davlat=davlat.capitalize()
    #print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
          #f"\nHududi:{info['hudud']}"
          #f"\nAholisi:{info['aholi']}"
          #f"\nPul birligi:{info['pul']}")
          
     
    
    
    