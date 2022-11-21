import random

class Puerta():
    def __init__(self, contenido):
        self.contenido = contenido
        self.elegida = False
    
    def __str__(self):
        return "<{}>".format("COCHE" if self.contenido else "CABRA")

class Concurso:
    puertas = []

    def __init__(self):
        self.puertas.append(Puerta(False))
        self.puertas.append(Puerta(False))
        self.puertas.append(Puerta(True))
        random.shuffle(self.puertas)

        self.eleccion = None

        print("Se crean las puertas {}".format(self.getTexto()))
    
    def getTexto(self):
        txt = "[{}, {}, {}]".format(self.puertas[0], self.puertas[1], self.puertas[2])
        return txt
    
    def elegir(self, num):
        for i in range(len(self.puertas)):
            if num == i:
                self.eleccion = self.puertas[i]
                self.puertas[i].elegida = True
                print("Elige la puerta {}".format(i))
            else:
                self.puertas[i].elegida = False
    
    def revelar(self):
        for i in range(len(self.puertas)):
            if (not self.puertas[i].elegida) and (not self.puertas[i].contenido):
                print("Se revela la puerta {}".format(i))
                return i
    
    def conclusion(self):
        return self.eleccion.contenido

def jugar(cambiar):
    concurso = Concurso()
    
    opt1 = random.randint(0, 2)
    concurso.elegir(opt1)
    revelada = concurso.revelar()
    
    if cambiar:
        print("Decide cambiar de puerta")
        puertas = [0, 1, 2]
        puertas.remove(revelada)
        puertas.remove(opt1)
        concurso.elegir(puertas[0])
    
    gana = concurso.conclusion()
    print("El resultado final es {}".format("COCHE" if gana else "CABRA"))

if __name__ == "__main__":
    jugar(True)
