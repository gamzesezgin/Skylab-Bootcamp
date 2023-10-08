# İçerisine girilen string ifadedeki kelimelerin hepsini bir listeye atan fonksiyon yazın.

def kelimeleri_ayir(sentence):
    kelimeler = []
    kelime = ""
    for karakter in sentence:
        if karakter != " ":
            kelime += karakter
        else:
            if kelime:
                kelimeler.append(kelime)
                kelime = ""

    if kelime:
        kelimeler.append(kelime)

    return kelimeler

kelimeler = kelimeleri_ayir("SKY LABE HOSGELDİNİZ MERHABA")
print(kelimeler)

# İçerisine iki tane string değer alan ve bu string ifadelerin içerisinde ortak harfleri ve bu ortak harflerin kaçartane kullanıldığını belirleyen fonksiyon yazın.

def ortak_harfleri_bul(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    ortak_harfler = {}

    for harf in str1:
        if harf.isalpha() and harf in str2:
            if harf in ortak_harfler:
                ortak_harfler[harf][0] += 1
            else:
                ortak_harfler[harf] = [1,0]

    for harf in str2:
        if harf.isalpha() and harf in str1:
            if harf in ortak_harfler:
                ortak_harfler[harf][1] += 1
            else:
                ortak_harfler[harf] = [0,1]

    for harf, (sayi1, sayi2) in ortak_harfler.items():
        print(f"{harf} {sayi1} {sayi2}")

string1 = "Anahtar"
string2 = "araba"

string3 = "deniz"
string4 = "beniz"

ortak_harfleri_bul(string1, string2)
ortak_harfleri_bul(string3, string4)



