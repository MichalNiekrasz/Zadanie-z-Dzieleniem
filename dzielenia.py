#Tym razem Kuba wykreśla razem z Basią wielokrotności liczb od 2 do a (włącznie). Napisz program,
#który wczyta liczby a i b (a < b) i wypisze liczby, które nie zostały wykreślone w przedziale [a, b].
#Na przykład dla a = 7 i b = 41, uczniowie będą wykreślać z przedziału [7, 41] wielokrotności 2, 3, 4, 5, 6 i 7.
#Ci sprytniejsi 2, 3, 5 i 7.

#Wejście
#dwie liczby z zakresu od 2 do 1000 w kolejnych liniach

#Wyjście
#liczby oddzielone spacją

def checkIfDivisible(v,b):
    #sprawdza czy v można podzielić przez b
    c = v//b
    if((c*b)==v):
        return True
    else:
        return False

def ladnieWypiszListe(text):
    #wypisuje liste w konsoli w pożądanym formacie
    papiez = ""
    for i in range(len(text)):
        papiez = papiez + str(text[i]) + " "
    print(papiez)


a = int(input("podaj a: "))
b = int(input("podaj b: "))
c = 213769420

#przypisuje do listy liczby a>x>1
dzielniki = list()

for i in range(int(a)):
    c = a
    c = c - i
    if c < 2:
        break
    dzielniki.append(c)

#przypisuje do listy liczby pomiędzy a i b
podane_liczby = list()
for i in range((b+1)-a):
    x = a
    x = x + i
    podane_liczby.append(x)

#print(podane_liczby)
#print(dzielniki)

#przypisuje do poniższej listy liczby z listy "podane_liczby" które nie są podzielne przez żaden element z listy "dzielniki"
liczbyNiepodzielnePrzezPosiadaneDzielniki = list()

for i in range(len(podane_liczby)):
    for j in range(len(dzielniki)):
        if checkIfDivisible(podane_liczby[i],dzielniki[j]):
            isDivisible = True
            break
        continue
    if not isDivisible:
        liczbyNiepodzielnePrzezPosiadaneDzielniki.append(podane_liczby[i])
    else:
        isDivisible = False
            
ladnieWypiszListe(liczbyNiepodzielnePrzezPosiadaneDzielniki)