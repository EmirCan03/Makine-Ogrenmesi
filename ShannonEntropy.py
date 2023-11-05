# Naive Bayes yöntemi hakkında araştırma

# girilen metnin shannon entropy değerini hesaplayarak bit şekline dönüştürünüz

import math

s=input("Ad soyad Giriniz : ")

s=s.replace(" ","")

liste = []

for i in s:
  liste.append(i)

print(liste)
k = set(liste)
print(k)

d={}

for i in k:
    adet = liste.count(i)       # girilen harften kaç tane var
    oran = adet/len(liste)
    d.update({i:oran})

print(d)

shannon = 0

for i in d:
    v = d[i]
    shannon += v*math.log2(v)           #Shannon Entropy formulü

shannon*=-1

print(shannon)

bs = math.ceil(shannon)             # bit sayısını yukarı yuvarlıyoruz
print("Bit Sayısı : ",bs)

dk = list(k)

b=[]

for i in range(int(math.pow(2,bs))):           # 2'nin üssü bs kadar döngü
    a=bin(i)[2:]                            #10'luk tabanda verilen sayıyı 2'lik tabana çevirir
    b.append(a)

dk.sort()   #sıralar
print(dk)
print(b)

for i in range (len(b)):
    for j in range (bs - len(b[i])):
        b[i]="0"+b[i]                   # kaç tane eksik 0 varsa ekler

print(b)

coded = ""

for i in liste:
    coded += b[dk.index(i)]

print(coded)