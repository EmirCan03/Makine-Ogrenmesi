#Basit veri seti üzerinde KNN üzerinde prediction yaptırınız
import math

sl = [5.3,5.1,7.2,5.4,5.1,5.4,7.4,6.1,7.3,6.0,5.8,6.3,5.1,6.3,5.5]
sw = [3.8,3.7,3.0,3.4,3.3,3.9,2.8,2.8,2.9,2.7,2.8,2.3,2.5,2.5,2.4]
tur =["Setosa","Setosa","Virginica","Setosa","Setosa","Setosa","Virginica","Versicolor","Virginica","Versicolor","Virginica","Versicolor","Versicolor","Versicolor","Versicolor"]

l = float(input("Lütfen sepal lenght değerini giriniz : "))
w = float(input("Lütfen sepal weight değerini giriniz : "))
k = int(input("Lütfen K değerini giriniz : "))

di = {}

for i in range(len(sl)):
    lfark = sl[i]-l
    wfark = sw[i]-w
    u = math.sqrt(math.pow(lfark,2)+math.pow(wfark,2))
    di.update({i:u})

print(di)

dis = {k:v for k, v in sorted(di.items(), key=lambda item: item[1]) }
print(dis)      #En küçük değer ne ise onun key değerini al ve yeni dis'e at

for i in dis:
    print(sl[i],"  ",sw[i],"  ",i,"  ",tur[i],"  ",dis[i])

dis_list = list(dis)

k_list = []
for i in range(k):
    k_list.append(tur[dis_list[i]])     #en yakın komşular alınıyor

print(k_list)

versicolor = setosa = virginica = 0    #Sayaç
versicolor = k_list.count("Versicolor")
setosa = k_list.count("Setosa")
virginica = k_list.count("Virginica")

if versicolor>setosa and versicolor>virginica :
    print("Sınıflandırma sonucu = Versicolor")
elif setosa>versicolor and setosa>virginica :
    print("Sınıflandırma sonucu = Setosa")
else:
    print("Sınıflandırma sonucu = Virginica")