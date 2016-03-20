# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:23:22 2015

@author: petr
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import struct, os, math, cv2

clear = lambda: os.system('cls')
clear()
plt.close('all')


vstup=[]
nvstupu =0
with open('Cv05_LZW_data.bin', 'rb') as f:    
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

#print "pocet nactenych dat =", nvstupu             
print "vstupni data =",vstup [0:]
 
slovnik=[]
slovnik.append(1)
slovnik.append(2)
slovnik.append(3)
slovnik.append(4)
slovnik.append(5) 
naslezenaFraze = 0
novaFraze = 0
vystupKomprese = []
for i in range(0, len(vstup)):
    naslezenaFraze = int(str(novaFraze) + str(vstup[i]))
    if naslezenaFraze in slovnik:
        novaFraze = naslezenaFraze + 0 
    else:
        vystupKomprese.append(slovnik.index(novaFraze)+1)
        slovnik.append(int(naslezenaFraze))   
        novaFraze = vstup[i]
        if i == len(vstup)-1:
            vystupKomprese.append(slovnik.index(novaFraze)+1)
        
#print "slovnik pro kompresi: ", slovnik [0:]
print "zkomprimovana data = ", vystupKomprese [0:]  
print "kompresni pomer = ", 100 * len(vystupKomprese)/len(vstup),"%"

#----------------------------------------------------------------------
slovnik2=[]
slovnik2.append(1)
slovnik2.append(2)
slovnik2.append(3)
slovnik2.append(4)
slovnik2.append(5)
naslezenaFraze2 = 0
novaFraze2 = 0
predchoziFraze = 0
vystupDekomprese = []

for i in range(0, len(vystupKomprese)):
    velikostSlovniku2 = len(slovnik2)
    if vystupKomprese[i] < velikostSlovniku2 or vystupKomprese[i] == velikostSlovniku2:     
        a = predchoziFraze        
        predchoziFraze = slovnik2[vystupKomprese[i]-1] + 0        
        vystupDekomprese.append(predchoziFraze)
        if i != 0:
            slovnik2.append(int(str(a) + str(vystupDekomprese[i])[0]))
    else:
        prvniZnak = str(vystupDekomprese[i-1])
        novaFraze2 = (int(str(predchoziFraze) + prvniZnak[0]))
        vystupDekomprese.append(novaFraze2)       
        if i != 0:
            slovnik2.append(int(str(vystupDekomprese[i]) + str(vystupDekomprese[i])[0]))   
            
#print "slovnik pro dekompresi: ", slovnik2 [0:] 
dekomprese = ""   
for k in range(len(vystupDekomprese)-1, -1,-1):
    dekomprese = str(vystupDekomprese[k]) + str(dekomprese)
print "dekomprimovana data = " + " ".join(dekomprese)


"""
tab = [[] for i in range(n)]
tab[i]=......
tab[i][j]

out:1 3 15

nelze pouzit appedn s inegrem


# pokud zmenim A, NEzmeni se B, bez [] by se zmenilo
A = B + []


hodnot 23
posledni ... 10 4 5 5 2 21
10. je 6
"""
