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

clear = lambda: os.system('cls')
clear()
plt.close('all')

""" ------------- RLE kodovani a dekodovani ---------------- """
vstup=[]
nvstupu =0
with open('Cv06_RLE_data.bin', 'rb') as f:    
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
print "vstup pro RLE = ", vstup[0:] 
vystup = []
pocet = 1
for i in range(1, len(vstup)):
    if vstup[i] == vstup[i-1]:
        pocet = pocet + 1
    else:
        vystup.append(int(str(pocet) + str(vstup[i-1])))
        pocet = 1
vystup.append(int(str(pocet) + str(vstup[i-1])))
print "vystup RLE = ",vystup[0:]
    

""" ------------- Huffmanova komprese a dekomprese ---------------- """
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
slovnik = np.array([["1    ", ""], ["2", ""],["3", ""],["4", ""],["5", ""]]) #[[None]*5]*2 #np.zeros(shape=(max(vstup),2))

#for idx,a in enumerate(slovnik):
#    for idy,b in enumerate(a):
#        slovnik[idx][idy] = ''
#print slovnik

print "\nvstup pro  Huff. = ", vstup[0:]   
pocet = 1
cetnost = np.zeros(shape=(max(vstup),2))
for a in range(0, max(vstup)):
    cetnost[a][0] = a + 1
for i in range(0, len(vstup)):
    cetnost[vstup[i]-1][1] = cetnost[vstup[i]-1][1] + 1
#print "cetnosti = ",cetnost
for q in range(0, len(cetnost)):
    cetnost[q][1] = round((cetnost[q][1])/len(vstup), 2)
#print "cetnosti hodnot (indexů) = ",cetnost

cetnost = sorted(cetnost, key=lambda x: x[1], reverse=True)

#print "cetnosti hodnot serazene = ",cetnost

slovnik[0][0] = '1'
for j in range(len(cetnost) - 1, 0, -1):
    for znak in str(cetnost[j][0]).replace(".0", ""):
        slovnik[int(znak)-1][1] = '0%s' % slovnik[int(znak)-1][1]
    for znak in str(cetnost[j-1][0]).replace(".0", ""):
        slovnik[int(znak)-1][1] = '1%s' % slovnik[int(znak)-1][1]

    cetnost[j-1][0] = (int(str(cetnost[j][0]).replace(".0", "") + str(cetnost[j-1][0]).replace(".0", "")))    
    cetnost[j-1][1] = cetnost[j][1] + cetnost[j-1][1]
    cetnost = sorted(cetnost, key=lambda x: x[1], reverse=True)
    #print cetnost
    
print "slovnik = \n", slovnik

vystup = ""
for i in vstup:
    vystup = vystup + slovnik[i-1][1]
print "\nVýsledný řetězec kodovani = " , vystup
print "Kompresni pomer: %.1f %%" % ((float) (len(vystup)/len(vstup)*8))

pomocne = []
for q in range(len(slovnik)):
    pomocne.append(slovnik[q][1])

dekodovani = []
prvek = vystup[0]
for i in range(1, len(vystup)+1):
    if prvek in pomocne:
        dekodovani.append(pomocne.index(prvek) + 1)
        if i < len(vystup):
            prvek = vystup[i]
    else:
        prvek = prvek + vystup[i]

print "Dekodovany retezec = ", dekodovani
"""
1 011
2 010
3 00
4 11
5 10

s = "123456"
print s[::-1]

< 0,7256; 0,7289 )
C = 0,726
"""




