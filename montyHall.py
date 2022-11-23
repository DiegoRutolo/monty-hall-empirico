import random

class Puerta():
    def __init__(self, contenido):
        self.contenido = contenido
        self.elegida = False
    
    def __str__(self):
        #return "<{}>".format("COCHE" if self.contenido else "CABRA")
        return "<{}>".format(self.contenido)

class Concurso:
    puertas = []

    def __init__(self, log=False):
        self.log = log

        self.puertas.append(Puerta(False))
        self.puertas.append(Puerta(False))
        self.puertas.append(Puerta(True))
        random.shuffle(self.puertas)

        self.eleccion = None

        if self.log:
            print("Se crean las puertas {}".format(self.getTexto()))
    
    def getTexto(self):
        txt = "[{}, {}, {}]".format(self.puertas[0], self.puertas[1], self.puertas[2])
        return txt
    
    def elegir(self, num):
        for i in range(len(self.puertas)):
            if num == i:
                self.eleccion = self.puertas[i]
                self.puertas[i].elegida = True
                if self.log:
                    print("Elige la puerta {}".format(i))
            else:
                self.puertas[i].elegida = False
    
    def revelar(self):
        for i in range(len(self.puertas)):
            if (not self.puertas[i].elegida) and (not self.puertas[i].contenido):
                if self.log:
                    print("Se revela la puerta {}".format(i))
                return i
    
    def conclusion(self):
        return self.eleccion.contenido

def jugar(cambiar, log=False):
    concurso = Concurso(log=log)
    
    opt1 = random.randint(0, 2)
    concurso.elegir(opt1)
    revelada = concurso.revelar()
    
    if cambiar:
        if log:
            print("Decide cambiar de puerta")
        puertas = [0, 1, 2]
        puertas.remove(revelada)
        puertas.remove(opt1)
        concurso.elegir(puertas[0])
    
    gana = concurso.conclusion()
    if log:
        print("El resultado final es {}".format("COCHE" if gana else "CABRA"))
    return gana



if __name__ == "__main__":
    numIteraciones = 8

    # Manteniendo
    cuenta1 = {
        True: 0,
        False: 0
    }

    for i in range(numIteraciones):
        result = jugar(False)
        cuenta1[result] += 1
    
    print(cuenta1)

    # Cambiando
    cuenta2 = {
        True: 0,
        False: 0
    }

    for i in range(numIteraciones):
        result = jugar(True, log=True)
        cuenta2[result] += 1

    print(cuenta2)