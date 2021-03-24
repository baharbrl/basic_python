#PYTHON401
#OOP
#CLASS TANIMI
class veribilimci(): #sinif tanimi
    print("bu bir sinif tanimi")

class veribilimci():
    bolum= " "               #sinifa ozellikler tanimladik
    sql= "evet"
    deneyim_yili= 0
    bildigi_diller= []
veribilimci().sql ="hayir"    
veribilimci().sql    

ali = veribilimci()         #sinifi orneklendirdik
ali.sql   
ali.bildigi_diller.append("python")
ali.bildigi_diller

veli = veribilimci()
veli.bildigi_diller       #python cikti bunu istemeyiz bir sey eklenmedi

#ornek ozellikleri

class veribilimci():
    bildigi_diller= ["R", "PYTHON"]
    bolum = " "
    sql = " "
    deneyim_yili = 0
    def __init__(self):           #her bir ornek degisik ozelliklerden olusur bilgisi
        self.bildigi_diller= []
        self.bolum = " "
ayse = veribilimci()
sena = veribilimci()
ayse.bildigi_diller                #bos olmasi gereken budur, ornek ozll bunu der.
sena.bildigi_diller 
ayse.bildigi_diller.append("R")      
ayse.bildigi_diller    
sena.bildigi_diller.append("python")
sena.bildigi_diller
veribilimci.bildigi_diller

#ornek metodlari
class veribilimci():
    calisanlar = []
    bolum = " "
    def __init__(self):                #ornek ozelligi
        self.bildigi_diller= []
        self.bolum = " "
    def dil_ekle(self, yeni_dil):       #metod olusturma
        self.bildigi_diller.append(yeni_dil) 
ala = veribilimci()
ala.bildigi_diller    
ala.bolum
ala.dil_ekle("R")
ala.bildigi_diller
ala.bolum= "istatistik"
ala.bolum
veribilimci.bolum

#miras yapilari
class employees():
    def __init__(self):    #her bir ornek degisik ozelliklerden olusur bilgisi
        self.firstname = " "
        self.lastname = " "
        self.address= " "
class datascience (employees): #miras kullandik
    def __init__(self):
        self.programming= " "
veribilimci1 = datascience() 
veribilimci1.address
class marketing (employees):
    def __init__(self):
        self.storytelling= " "
mar1= marketing()
mar1.

#Fonksiyonel programlama FP

#Yan etkisiz fonk pure func bagimsizlik
A= 10
def impure_sum(b):
    return b+A
def pure_sum (a,b):
    return a+b
impure_sum(6) #Aya bagli degisince degisir
pure_sum(4,6)

#LAMBDA
new_sum = lambda a,b: a+b
new_sum(6, 8)

sirasiz_list = [("a",5),("b",6),("d",1)]
sorted(sirasiz_list , key=lambda x:x[1])

#vektorel operations with fp
import numpy as np
a= np.array([1,2,3,4])
b= np.array([2,3,4,5])
a*b

#map: fonksiyonu istenen vektorde calistirir
liste = [1,2,3,4,5]        
list(map(lambda x:x*10 , liste))        
#filter: kosul arar, saglayanlari geri doner
liste = [1,2,3,4,5]    
list(filter(lambda x:x%2==0, liste))
#reduce : indirgeme yapar tek deger doner
from functools import reduce
liste = [1,2,3,4,5]   
reduce(lambda a,b : a+b , liste)

#MODUL OLUSTURMA
import hesapmodulu
hesapmodulu.yeni_maas(1000)

import hesapmodulu as hm
hm.yeni_maas(2000)

from hesapmodulu import yeni_maas
yeni_maas(3000)

import hesapmodulu as hm
hm.maaslar

#Hatalar
a=10
b="2"
a/b
try:
    print(a/b)
except TypeError:
    print("sayi ve str carpilmaz")






















