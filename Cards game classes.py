import random

class Carta:
    def __init__(self, numero, palo) -> None:
        palosAccepted = ["picas","treboles","diamantes","corazones"]
        if(palo.lower() in palosAccepted):   
            self.palo = palo
            self.numero = numero
        else:
            raise "Palo no válido para la carta"
        

    def __str__(self) -> str:
        return f"Carta {self.numero} de {self.palo.capitalize()}"


class Baraja:
    def __init__(self, listaCartas):
        self.listaCartas = listaCartas 
        if(len(self.listaCartas>52)):
            raise "Hay más de 52 cartas en la baraja"

    def __str__(self):
        for i in range(len(self.listaCartas)):
            print(self.listaCartas[i])
        return ""

    def barajar(self):
        random.shuffle(self.listaCartas)
        return self.listaCartas
    
    def repartir(self,numero):
        repartidas = random.sample(self.listaCartas, k = numero)
        self.listaCartas = [carta for carta in self.listaCartas if carta not in repartidas]
        return repartidas
    
    def añadirCartas(self, cartasAñadidas):
        self.listaCartas += cartasAñadidas
        



if __name__ == "__main__":
    # print(Carta(1, "TREboLES"))
    baraja = Baraja([Carta(num, palo)  for palo in ["picas","corazones","treboles","diamantes"] for num in range(1,14)])
    
    baraja.barajar()
    print("BARAJAMIENTO \n")
    print(baraja)
    print("Se reparten las cartas: ")
    repartir1 = baraja.repartir(50)
    for carta in repartir1:
        print(carta)
    print("Nueva baraja \n")
    print(baraja)
    print("Añadimos una carta")
    baraja.añadirCartas([repartir1[0]])
    print("Nueva baraja \n")
    print(baraja)




