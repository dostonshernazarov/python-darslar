# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 12:48:59 2022

@author: User
"""

davlatlar = {
    'O\'zbekiston':{'aholi':35000000,\
                    'hudud':448978,\
                    'pul':'so\'m',\
                    'poytaxt':'toshkent'
                    },\
    'Rossiya':{'aholi':145000000,\
               'hudud':17089246,\
               'pul':'publ',\
               'poytaxt':"moskva"
              },\
    'AQSH':{'aholi':328000000,\
            'hudud':9631418,\
            'pul':"dollar",\
            'poytaxt':'vashington'
            }
    }
     
for davlat, info in davlatlar.items():
    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi:{info['hudud']}"
          f"\nAholisi:{info['aholi']}"
          f"\nPul birligi:{info['pul']}")
          
     
    
    
    