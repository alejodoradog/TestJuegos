import random
import unittest

def Juego(TirarDado,dado):
    dado = 0
    print(f"Actualmente estás en la posición {dado}")

    PosicionActual = 0
    Posiciones = []
    for p in range(1,26):
        Posiciones.append(p)
    print(Posiciones)

    Escaleras = [3,6,9,10]
    Serpientes = [14,19,22,24]
    print(ProcessLookupErrortual)
    while(PosicionActual<25):
        TirarDado= input("Presione 'A' y enter para arrojar el dado: ")
        if(TirarDado!="A"):
            while(TirarDado!="A"):
                TirarDado= input("Presione 'A' y enter para arrojar el dado: ")
                dado = random.randint(1,6)
            print(f"Tu dado ha arrojado {dado}")
            PosicionActual = PosicionActual + dado
        else:
            dado = random.randint(1,6)
            print(f"Tu dado ha arrojado {dado}")
            PosicionActual = PosicionActual + dado
        if(PosicionActual in Escaleras):
            if(PosicionActual == 3):
                PosicionActual = 11
            elif(PosicionActual == 6):
                PosicionActual = 17
            elif(PosicionActual == 9):
                PosicionActual = 18
            else:
                PosicionActual = 12
            print(f"Avanzas a la posición {PosicionActual}")
        elif(PosicionActual in Serpientes):
            if(PosicionActual == 14):
                PosicionActual = 4
            elif(PosicionActual == 19):
                PosicionActual = 8
            elif(PosicionActual == 22):
                PosicionActual = 20
            else:
                PosicionActual =16
            print(f"Desciendes a la posición {PosicionActual}")
        else:
            print(f"Tu nueva posición es {PosicionActual}")
    return PosicionActual

#Test unitario:

class TestJuego(unittest.TestCase):
    def test_subir_escalera(self):
        dado = 0
        PosicionActual = 0  # Empezamos en la posición 0
        Escaleras = [3, 6, 9, 10]  # Agregamos una escalera en la posición 3  
        dado = 3
        PosicionActual += dado
        if PosicionActual in Escaleras:
            if PosicionActual == 3:
                PosicionActual = 11  # Subir a la posición 11 al subir la escalera en la posición 3
            elif PosicionActual == 6:
                PosicionActual = 17
            elif PosicionActual == 9:
                PosicionActual = 18
            else:
                PosicionActual = 12
        self.assertEqual(PosicionActual, 12)  # Verificamos que llegue a la posición 12 después de subir la escalera

if __name__ == '__main__':
    unittest.main()


