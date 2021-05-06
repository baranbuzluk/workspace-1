#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 19:03:45 2018

@author: sadievrenseker
"""


import pandas as pd
import matplotlib.pyplot as plt
import random
import math

veriler = pd.read_csv('Ads_CTR_Optimisation.csv')

#   Random selection
#   BEGIN
N = 10000
d = 10 
toplam = 0
secilenler = []
for n in range(0,N):
    ad = random.randrange(d)
    secilenler.append(ad)
    odul = veriler.values[n,ad] # verilerdeki n. satır = 1 ise odul 1
    toplam = toplam + odul
    
    
plt.hist(secilenler)
plt.show()

# END



#   UCB
#   BEGIN
N = 10000
d = 10 
#Ri(n)
oduller = [0]*d
#Ni(n)
tiklamalar = [0]*d 
toplam = 0
secilenler = []
for n in range(0,N):
    ad = 0 #secilen ilan
    max_ucb = 0
    for i in range(0,d):
        if tiklamalar[i]>0:
            ortalama = oduller[i] / tiklamalar[i]
            delta = math.sqrt(3/2* math.log(n)/tiklamalar[i])
            ucb = ortalama + delta
        else:
            ucb= N*10
            
        if max_ucb < ucb:
            max_ucb = ucb
            ad = i
    secilenler.append(ad)
    tiklamalar[ad] = tiklamalar[ad] + 1
    odul = veriler.values[n,ad] # verilerdeki n. satır = 1 ise odul 1
    oduller[ad] = oduller[ad] + odul
    toplam = toplam + odul
    
    
print(f"Toplam Odul: {toplam}")

# END




#   Thompson algoritmasi
#   BEGIN
N = 10000
d = 10 
#Ri(n)
oduller = [0]*d
#Ni(n)
tiklamalar = [0]*d 
toplam = 0
secilenler = []
birler = [0]*d 
sifirlar = [0]*d 
for n in range(0,N):
    ad = 0 #secilen ilan
    max_th = 0.0
    for i in range(0,d):
        rasbeta = random.betavariate( birler[i]+1 , sifirlar[i]+1)
        if rasbeta>max_th :
            max_th = rasbeta
            ad = i
        secilenler.append(ad)
        odul = veriler.values[n,ad]
        if odul == 1:
            birler[ad] = birler[ad]+1
        else:
            sifirlar[ad] = sifirlar[ad]+1
            
    toplam = toplam + odul
    
print(f"Toplam Odul: {toplam}")

# END




