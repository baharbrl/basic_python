#PYTHON201
#VERI YAPILARI

#LISTELER
notlar = [10, 20, 30]
type(notlar)
liste = ["a", 19.2, 90, notlar]
len (liste)
type(notlar[0])
tum_liste = [notlar, liste]
#del tum_liste
yeni_liste = ["a", 10, [20,30,40,50]]
yeni_liste
yeni_liste [2][1] #30a ulastim


kisiler = ["ali", "veli", "berkcan","ayse"]
kisiler[1] = "velinin_babasi"
kisiler
kisiler[1] = "veli"
kisiler[0:3] = "alinin_babasi", "velinin_babasi", "berkcanin_babasi"
kisiler
kisiler = ["ali", "veli", "berkcan","ayse"]
kisiler = kisiler + ["kemal"]
kisiler
#del kisiler[2]
kisiler

dir(kisiler) #listeye uygulancak metodlari gosterir
kisiler.append("deniz") #denizi ekledi
kisiler
kisiler.remove("kemal") #kemali sildi
kisiler
kisiler.insert(0,"sevgi") #0.indekse ekledi
kisiler
kisiler.insert(len(kisiler),"bahar") #sonuncu indekse ekler
kisiler
kisiler.pop(3) #3.indeksi sildi
kisiler
kisiler.count("ali") #kac ali var saydi
yedek_kisiler = kisiler.copy() #yedek yapti kopyaladi
kisiler.extend(["a","b",10]) #listeye ekledi
kisiler.index("a") #a kacinci indekste soyler
kisiler.reverse() #tersten yazdi
sayi = [10, 50, 30, 40]
sayi.sort() #siralama yapti
sayi
sayi.clear() #liste icini temizledi bos

#TUPLE
t = ("ali", "veli", 10, 2.5, [1,2,3])
type(t)
type(t[4][0]) #4.indeksin 0.indeksli elemanina ulastim
t[2:4] #2den 4e kadar ulastim
ty = "a", "b"
tx = ("eleman",) #tek elemansa , koy
type(tx)


#DEQUE listenin boyutlusu
from collections import deque
dq= deque(maxlen=3)
dq.append(1)
print(dq)
dq.append(2)
print(dq)
dq.appendleft(3)
print(dq)


#SOZLUK OLUSTURMA
sozluk = {"REG": "regresyon",
          "LOJ" : "lojistik reg",
          "CART" : "class"}
len(sozluk) #3 yazar
sozluk = {"REG": 10,
          "LOJ" : 20,
          "CART" : "class"}
sozluk = {"REG": ["regresyon",10], #sozluk icinde liste
          "LOJ" : ["lojistik reg",20],
          "CART" : ["class",30]}
sozluk["REG"] #degeri cagirir
#sozluk icinde sozluk
sozluk = {"REG": {"RMSE" : 10 ,
                  "MSE" : 20,
                  "SSE" : 30}, 
          
          "LOJ" : {"RMSE" : 10 ,
                  "MSE" : 20,
                  "SSE" : 30},
          
          "CART" : {"RMSE" : 10 ,
                  "MSE" : 20,
                  "SSE" : 30}}
sozluk["REG"]["MSE"] #degeri cagirip ulastim 20ye

sozluk["REG"] = ["BAHAR"] #reg elemani degisti
sozluk
sozluk["GBM"] = "gradient" #eleman ekledi
sozluk
l=[1]
sozluk[l]="yeni"
t = ("tuple",)
sozluk[t]="yeni"
sozluk

#SETLER
s = set() 
l = [1,"a","ali",123 ] 
s = set(l) #listeden set
s

t = ("a","ali")
s = set(t) #tupledan set
s

ali = "uzaya_git"
type(ali)
s = set(ali) #str yi sete cevirdi
s #her karakteri 1defa yazdi

l = ["ali", "ali", "git"]
s = set(l)
s #1ali 1git yazdi
len(s) #2verir

s.add("ile")
s
s.remove("ile")
s
s.discard("ile")

set1 = set([1,3,5])
set2 = set([1,2,3])
set1.difference(set2) #1de olup 2de olmayani verir
set2.difference(set1)
set1 - set2 #1de olup 2de olmayani verir
set1.symmetric_difference(set2) #her 2settede olmayani verir
set1.intersection(set2) #kesisimi verir
set1&set2 #kesisim
set1.union(set2) #birlesim 
set1.intersection_update(set2) #kesismdeki elemanlar set1in oldu, set1 guncellendi
set1
set1.isdisjoint(set2) #kesisimleri bos mu
set1.issubset(set2) #set1 set2nin alt kumesi mi
set2.issuperset(set1) #set2 set1i kapsar mi

#GENERATOR AND YIELD
generator = (x for x in range (1,4))
for i in generator:
    print(i)
def createGenerator():
    liste=range(1,4)
    for i in liste:
        yield i
generator = createGenerator()
for i in generator:
    print(i)
    



