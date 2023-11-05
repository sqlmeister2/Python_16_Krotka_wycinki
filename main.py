#TUPLE krotki tworzymy w nawiasach okrągłych
#może przechowywać mieszane typy danych jak lista
krotka = (2, 4, 8, 16, 32, 64, 128)

#wyswietlanie
print(krotka)
print(krotka[0])
print(krotka[6])

#roznice miedzy lista a krotka
# krotka[0] = 1 #nie da się przypisywac elementów, nie da się jej całej modyfikowac

print("ELEMENTÓW w krotce ", krotka.count(2))
print("Index: ", krotka.index(64))
print(len(krotka))

#Wycinki pozwalaja nam wyciac cześc elementow kolekcji
#dla list i dla krotek
print("\nWycinki: ")
print(krotka[0:2])
print(krotka[2:5])
print(krotka[2:100]) #nie ma błędu

#z minusem liczenie elementow od konca
print("---")
print(krotka[-4:-2])

#uwzglednienie skoku
print(krotka[0:7:2]) # trzeci parametr to skok
print(krotka[2:]) # pobieramy kolekcje do samego konca
print(krotka[:4])

#odwrócenie kolejności wyswietlania
print(krotka[:4:-1]) # odpowiada za to ujemny parametr skoku
print(krotka[:4:-2])

print("----")
print(2 in krotka)

#dodana inna krotka do krotki
krotka = krotka + (10, 20)
print(krotka)

#Tworzenie krotki  z listy i mozna z krotki na liste
my_list = [10,4, 6, 88, 46, 2, 0]
my_tuple = tuple(my_list)
print(my_tuple)

print(max(my_tuple))

#redukcja
print(sum(my_tuple))

a = my_tuple[0]
print(a)
a, b, c, d, e, f, g = my_tuple
print(e)

print("---")
tax = (4, 7, 8, 23, 8)
print(tax[-1])
print(tax.index(8))
print(tax.count(8))
print(max(tax))

