# Ucgen Türü Belirleme
sayi1 = float(input("Birinci sayiyi giriniz: "))
sayi2 = float(input("İkinci sayiyi giriniz: "))
sayi3 = float(input("Ucüncü sayiyi giriniz: "))

if sayi1 != 0 and sayi2 != 0 and sayi3 != 0:
    if sayi1 == sayi2 == sayi3:
        print("Eskenar Ucgen")
    elif sayi1 == sayi2 != sayi3 or sayi2 == sayi3 != sayi1 or sayi1 == sayi3 != sayi2:
        print("İkizkenar Ucgen")
    elif sayi1 != sayi2 != sayi3:
        print("Cesitkenar Ucgen")
else:
    print("Üçgen belirtmez")