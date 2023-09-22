# Tamkare Sayıları Belirleme

sayi1 = float(input("Birinci sayiyi giriniz: "))
sayi2 = float(input("İkinci sayiyi giriniz: "))

i = 1
def kare(i,my_list):
    while i ** 2 < sayi2:
        if sayi1 < i ** 2:
            my_list.append(i ** 2)
        i += 1

my_list = []
kare(i, my_list)
print(my_list)