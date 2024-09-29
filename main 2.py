Boy = 180    #cm cinsinden giriniz
Kilo = 60    #kg cinsinden giriniz
VKI = Kilo/((Boy/100)**2)

if Boy<=0 or Kilo<=0 :
    print("Hatalı değer")

elif VKI<18.5 :
    print("Zayıf")
    print(VKI)

elif 18.5<=VKI<25 :
    print("İdeal")
    print(VKI)
    
elif 25<=VKI<30 :
    print("Kilolu")
    print(VKI)
    
elif 30<=VKI<40 :
    print("obez")
    print(VKI)
    
else :
    print("Morfin obez")
    print(VKI)