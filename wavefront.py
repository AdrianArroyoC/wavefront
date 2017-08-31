from reportlab.pdfgen import canvas

class Agente:
    def __init__(self, ambiente, xFinal, yFinal, valor, finalizado, marcado):
        self.ambiente = ambiente
        self.xFinal = xFinal
        self.yFinal = yFinal
        self.valor = valor
        self.finalizado = finalizado
        self.marcado = marcado
        self.ca = canvas.Canvas("wavefront.pdf")
        self.valores = []
        self.direccion = []

    def imprimir(self):
        for a in self.ambiente:
            print(a)

    def imprimirPDF(self):
        espacio = 700
        for a in self.ambiente:
            self.ca.drawString(100,espacio,str(a))
            espacio = espacio - 15
        self.ca.save()

    def recorrerAmbiente(self):
        self.marcado = 0
        for x in range(1, len(self.ambiente)-1):
            for y in range(1, len(self.ambiente[x])-1):
                if self.ambiente[x][y] == self.valor:
                    self.revisarMarcar(x+1,y)
                    self.revisarMarcar(x-1,y)
                    self.revisarMarcar(x,y+1)
                    self.revisarMarcar(x,y-1)
        self.valor = self.valor + 1

    def revisarMarcar(self, x, y):
        if self.ambiente[x][y] == 0:
            self.ambiente[x][y] = self.valor + 1
            self.marcado = 1
            if self.xFinal == x and self.yFinal == y:
                self.finalizado = 1
                self.marcado = 0

    def marcarRuta(self, x, y):
        print(self.ambiente[x][y])
        if self.ambiente[x+1][y] == (self.valor -1):
            self.ambiente[x+1][y] = str(self.ambiente[x+1][y]) + "*"
            self.valor = self.valor - 1
            marcarRuta(x+1,y,valor-1)
        if self.ambiente[x-1][y] == (self.valor -1):
            self.ambiente[x-1][y] = str(self.ambiente[x-1][y]) + "*"
            self.valor = self.valor - 1
            marcarRuta(x+1,y,valor-1)
        if self.ambiente[x][y+1] == (self.valor -1):
            self.ambiente[x][y+1] = str(self.ambiente[x][y+1]) + "*"
            self.valor = self.valor - 1
            marcarRuta(x+1,y,valor-1)
        if self.ambiente[x+1][y] == (self.valor -1):
            self.ambiente[x+1][y] = str(self.ambiente[x+1][y]) + "*"
            self.valor = self.valor - 1
            marcarRuta(x+1,y,valor-1)
        if self.ambiente[x][y] == 1:
            self.ambiente[x][y] = "1*"
            self.imprimir()


def introducirCoordenadas(ambiente, mensaje):
        y = int(input("Introduce la posicion x " + mensaje + ": "))
        x = int(input("Introduce la posicion y " + mensaje + ": "))
        if ambiente[y][x] == 0: 
            return [y,x]
        else:
            print("Posicion incorrecta, intenta de nuevo...")
            introducirCoordenadas(ambiente, mensaje)

def main():
    ambiente = [[-1,-1,-1,-1,-1,-1,-1],
            [-1, 0, 0, 0, 0, 0,-1],
            [-1, 0, 0,-1,-1, 0,-1],
            [-1, 0, 0, 0,-1, 0,-1],
            [-1, 0, 0, 0,-1, 0,-1],
            [-1,-1,-1,-1,-1,-1,-1]]
    c = introducirCoordenadas(ambiente, "inicial")
    yFinal = c[0]
    xFinal = c[1]
    c = introducirCoordenadas(ambiente, "meta")
    yInicial = c[0]
    xInicial = c[1]
    if yFinal == yInicial and xFinal == xInicial:
        print("Coordenadas de inicio y fin iguales, fin del programa")
    else:
        ambiente[yInicial][xInicial] = 1
        agente = Agente(ambiente, xFinal, yFinal, 1, 0, 1)
        while agente.finalizado == 0 and agente.marcado == 1:
            agente.recorrerAmbiente()
            print("")
            agente.imprimir()
        agente.imprimirPDF()
        #while agente.valor != 1:
            #agente.marcarRuta(yFinal, xFinal)
        #print("")
        #print("Programa finalizado")

if __name__ == "__main__":
    main()