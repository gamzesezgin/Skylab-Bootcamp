# Hesap Makinesi
sayi1 = float(input("Birinci sayiyi giriniz: "))
sayi2 = float(input("İkinci sayiyi giriniz: "))
sembol = islem_isareti = input("+ - * veya / giriniz: ")

if sembol == '+':
    print(sayi1 + sayi2)
elif sembol == '-':
    print(sayi1 - sayi2)
elif sembol == '*':
    print(sayi1 * sayi2)
elif sembol == '/':
    if sayi2 == 0:
        print("Tanimsiz. Lütfen sayi2'ye yeni bir deger giriniz!")
    else:
        print(sayi1 / sayi2)