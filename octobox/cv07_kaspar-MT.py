# -*- coding: utf-8 -*-
"""
Created on Thu Apr 02 14:31:56 2015

@author: student
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import struct, os, math, cv2
from operator import itemgetter
from decimal import Decimal as d

clear = lambda: os.system('cls')
clear()
plt.close('all')

""" ------------- Aritmeticke kodovani a dekodovani ---------------- """
vstup=[]
nvstupu =0
with open('Cv07_Aritm_data.bin', 'rb') as f:    
    byte=0    
    while byte != "":
        try:
            vstup.append(struct.unpack('B', f.read(1))[0]) 
            if not vstup[nvstupu]:
                break
            byte = vstup[nvstupu]      
            nvstupu = nvstupu + 1
        except:
            break            
f.close()
print "vstup pro Aritmeticke kodovani = ", vstup[0:] 

cetnost = np.zeros(shape=(max(vstup),2))
for a in range(0, max(vstup)):
    cetnost[a][0] = a + 1
for i in range(0, len(vstup)):
    cetnost[vstup[i]-1][1] = cetnost[vstup[i]-1][1] + 1
#print "cetnosti = ",cetnost
for q in range(0, len(cetnost)):
    cetnost[q][1] = round((cetnost[q][1])/len(vstup), 2)
#print "cetnosti hodnot = \n",cetnost

intervaly = np.zeros(shape=(max(vstup),2))
pom = 0
for q in range(0, len(intervaly)):
    intervaly[q][0] = pom
    pom += cetnost[q][1]
    intervaly[q][1] = pom    
print "intervaly = \n",intervaly
    
i = [0,1]

dolni = 0
horni = 1
r=0.6
t=0.9
dolni = dolni+(r*(horni - dolni))
horni=dolni+(t*(horni - dolni)) +0

dolni = 0
horni = 1

for q in range(0, len(vstup)):

    d2=dolni
    dolni += intervaly[vstup[q]-1][0] * (horni - dolni)
    horni = d2 + (intervaly[vstup[q]-1][1] * (horni - d2))

cislo = dolni
print "Výsledek kódování = ", cislo

vystup = []
dolni = 0
horni = 1
k = cislo

for q in range(0, len(vstup)):

    k = round((cislo - dolni) / (horni - dolni),10)

    for a in range(0, len(intervaly)):
        if (k >= round(intervaly[a][0], 10) and k < round(intervaly[a][1], 10)):

            vystup.append(a+1)
            break

    d2 = dolni
    dolni += intervaly[a][0] * (horni - dolni)
    horni = d2 + (intervaly[a][1] * (horni - d2))

#print "vstup  = ",vstup
print "vystup = ",vystup
