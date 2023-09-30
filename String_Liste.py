# İçerisine girilen string ifadedeki kelimelerin hepsini bir listeye atan fonksiyon yazın.

def list_maker(sentence):
    new_word_list = sentence.split()
    print(new_word_list)

list_maker(sentence= "Python ile stringi listeye dönüstürme")

# İçerisine iki tane string değer alan ve bu string ifadelerin içerisinde ortak harfleri ve bu ortak harflerin kaçartane kullanıldığını belirleyen fonksiyon yazın.

def common_char(str1, str2):
    count = 0
    for char in str1:
        if char in str2:
            counter1 = str1.count(char)
            counter2 = str2.count(char)
            print(char, counter1, counter2)

common_char("Anahtar", "araba")
common_char("deniz", "beniz")




