#PYTHON301
#FONKSIYONLAR
def kare_al (x) :
    print("girilen sayi:" + str(x) + ",sayinin karesi:" + str(x**2))
    kare_al(5)

def carpma_yap (x, y) :
    print(x*y)
carpma_yap(2,3)

def carpma (x, y=1):
    print(x*y)
carpma_yap(y = 6, x = 2)

def direk_hesap (isi , nem , sarj) :
    return((isi + nem)/sarj)
cikti = direk_hesap(30, 40, 70)*9
print(cikti)

x = []
def eleman_ekle (y) :
    x.append(y)
    print("eklenen eleman:" + str(y))
eleman_ekle(10)
x

#KARAR KONTROL YAPILARI 
sinir = 5000
magaza_adi = input("mazaga adi nedir?")
gelir = int(input("geliri giriniz:" ))
if gelir > sinir :
    print("tebrikler" + magaza_adi + " promosyon kazandiniz!")
elif gelir < sinir :
    print("uyari! dusuk gelir:" + str(gelir))
else :
    print("takibe devam")

#DONGULER
maaslar =[10,20,30,40,50]
for i in maaslar:
    print(i)

maaslar =[10,20,30,40,50]
def yeni_maas (x) :
    print(x*20/100 + x)
for i in maaslar:
    yeni_maas(i)

maaslar =[1000,2000,3000,4000,5000]
def maas_alt (x) :
    print(x*20/100 + x)
def maas_ust (x) :
    print(x*10/100 + x)
for i in maaslar :
    if i <= 3000 :
        maas_alt(i)
    else :
        maas_ust(i)

maaslar =[1000,2000,3000,4000,5000]
for i in maaslar :
    if i == 3000 :
        print("kes")
        break
    print(i)

maaslar =[1000,2000,3000,4000,5000]
for i in maaslar :
    if i == 3000 :
        print("kes")
        continue
    print(i)

sayi = 1
while sayi < 10 :
    sayi += 1
    print(sayi)





