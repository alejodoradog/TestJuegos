


SopaLetras = ["SOL",
              "UNO",
              "NUT"]
Palabra = "SOL"
Longitud=len(Palabra)
print(Palabra[0])

Posi = []
LetraActual = ""

Hor = False
Ver = False

def EncontrarLetra(LetraBuscada,SopaLetras):
    for i in range(len(SopaLetras)):
        for j in range(len(SopaLetras[i])):
            LetraActual = SopaLetras[i][j]
            if LetraActual == LetraBuscada:
                Posiciones = [i,j]
                break
        if LetraActual == LetraBuscada:
                Posiciones = [i,j]
                break
    return Posiciones
    
print(EncontrarLetra("N",SopaLetras))


for letra in range(0,Longitud-1):
    Posi = EncontrarLetra(Palabra[letra],SopaLetras)
    if Palabra[letra+1] == SopaLetras[Posi[0]+1][Posi[1]]:
        print("La palabra es vertical")
        Ver = True
    elif Palabra[letra+1] == SopaLetras[Posi[0]][Posi[1]+1]:
        print("La palabra es horizontal")
        Hor = True
    else:
        print("La palabra no está")
        Hor = False
        Ver = False


if Ver == True:
    EncontrarLetra(Palabra[0],SopaLetras)
    print(f"La letra {Palabra[0]} está en la posición {Posi}")
    for i in range(1,Longitud):
        print(f"La letra {Palabra[i]} está en la posición {[Posi[0],Posi[1]+i]}")

if Hor == True:
    EncontrarLetra(Palabra[0],SopaLetras)
    print(f"La letra {Palabra[0]} está en la posición {Posi}")
    for i in range(1,Longitud):
        print(f"La letra {Palabra[i]} está en la posición {[Posi[0]+i,Posi[1]]}")











    
