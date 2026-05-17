import random
import matplotlib.pyplot as plt

random.seed(42)

v1 = [1, 0, 0, 0, 0, 4, 4, 2, 0, 1, 1]
v2 = [0, 1, 0, 0, 0, 3, 0, 2, 2, 1, 0]
v3 = [0, 0, 1, 0, 0, 2, 0, 1, 1, 1, 1]
v4 = [0, 0, 0, 1, 1, 0, 0, 0, 4, 3, 0]

baza_wektorow = [v1, v2, v3, v4]

def generujMacierz():
    macierz = []
    for i in range(4):
        wiersz = []
        for j in range(10):
            wiersz.append(random.randint(0,4))
        macierz.append(wiersz)
    return macierz

def wyswietl_obraz(macierz):
    obraz = []
    for i in range(len(macierz)):
        wiersz = []
        for j in range(len(macierz[0])):
            wiersz.append(macierz[i][j] / 4.0)
        obraz.append(wiersz)
    plt.imshow(obraz, cmap='gray', vmin=0, vmax=1)
    plt.show()

def generujwspolczynniki():
    listalist = []
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    lista = [i, j, k, l]
                    listalist.append(lista)
    return listalist

def generujZBazy(baza):
    wspolczynniki = generujwspolczynniki()
    wszystkie = []
    for i in range(len(wspolczynniki)):
        nowe_slowo = []
        for j in range(11):
            liczba = (wspolczynniki[i][0]*baza[0][j] + wspolczynniki[i][1]*baza[1][j] + 
                      wspolczynniki[i][2]*baza[2][j] + wspolczynniki[i][3]*baza[3][j]) % 5
            nowe_slowo.append(liczba)
        wszystkie.append(nowe_slowo)
    return wszystkie

def zakoduj_wektor(v, G):
    zakodowanyWektor = []
    for j in range(len(G[0])):
        suma = 0
        for i in range(len(v)):
            suma += v[i] * G[i][j]
        zakodowanyWektor.append(suma % 5)
    return zakodowanyWektor

def kanal(v):
    nowy_v = []
    for i in range(len(v)):
        randomowa = random.randrange(0,100)
        if(randomowa < 5):
            element = (v[i] + 3) % 5
            nowy_v.append(element)
        else:
            nowy_v.append(v[i])
    return nowy_v

def odleglosc_Hamminga(v1,v2):
    suma = 0
    for i in range(len(v1)):
        if(v1[i] != v2[i]):
            suma = suma + 1
    return suma

def szukanieWektorow(v, C):
    minimalna = len(v) + 1
    wektory = []
    for i in range(len(C)):
        if odleglosc_Hamminga(v, C[i]) < minimalna:
            minimalna = odleglosc_Hamminga(v, C[i])
    for i in range(len(C)):
        if odleglosc_Hamminga(v, C[i]) == minimalna:
            wektory.append(C[i])
    return wektory

def minimizeHammingDistance(C, B, v):
    wektory = szukanieWektorow(v,C)
    randomowy = random.randint(0,len(wektory) - 1)
    w = wektory[randomowy]
    r = [w[0], w[1], w[2], w[3]]
    return r

def podpunkt_g(lista_kolumn):
    odtworzona_macierz = []
    for i in range(4):
        nowy_wiersz = []
        for j in range(10):
            nowy_wiersz.append(lista_kolumn[j][i])
        odtworzona_macierz.append(nowy_wiersz)
    return odtworzona_macierz

def main():
    
    C = generujZBazy(baza_wektorow)
    
    # PODPUNKT A: Generowanie macierzy
    print("\n[Podpunkt a] \n")
    oryginalna_wiadomosc = generujMacierz()
    for wiersz in oryginalna_wiadomosc:
        print(wiersz)
        
    # PODPUNKT B: Wyświetlanie obrazu
    print("\n[Podpunkt b] \b")
    
    wyswietl_obraz(oryginalna_wiadomosc)
    
    odkodowane_kolumny = []
    poprawne_kolumny = 0
    
    for j in range(10):
        print(f"\n>> Przetwarzanie kolumny nr {j+1}:")
        
        v = [oryginalna_wiadomosc[i][j] for i in range(4)]
        print(f"   Oryginalny wektor v:  {v}")
        
        # PODPUNKT D: 
        zakodowany = zakoduj_wektor(v, baza_wektorow)
        print(f"   [Podpunkt d]: {zakodowany}")
        
        # PODPUNKT E: 
        zaszumiony = kanal(zakodowany)
        if zaszumiony != zakodowany:
            print(f"   [Podpunkt e] Error:      {zaszumiony}")
        else:
            print(f"   [Podpunkt e] Jest dobrze:  {zaszumiony}")
            
        # PODPUNKT F: 
        odkodowany_r = minimizeHammingDistance(C, baza_wektorow, zaszumiony)
        print(f"   [Podpunkt f] Odkodowany wektor r: {odkodowany_r}")
        
        odkodowane_kolumny.append(odkodowany_r)
        
        # PODPUNKT H:
        if v == odkodowany_r:
            poprawne_kolumny += 1
            print("     Zgodny")
        else:
            print("     Niezgodny")

    # PODPUNKT G: 
    print("\n[Podpunkt g] Odtworzona macierz:")
    odtworzona_wiadomosc = podpunkt_g(odkodowane_kolumny)
    for wiersz in odtworzona_wiadomosc:
        print(wiersz)
    
    # PODPUNKT H poprawne kolumny: 
    print(f"\n[Podpunkt h]")
    print(f"Kolumny przesłane bezbłędnie: {poprawne_kolumny} / 10")
    
    # PODPUNKT I: 
    print("\n[Podpunkt i] (obraz)")
    wyswietl_obraz(odtworzona_wiadomosc)
    
if __name__ == "__main__":
    main()