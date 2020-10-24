import csv

class ManejadorCosecha:
    #__listaCosecha = []                             #DEFINO LA LISTA VACIA

    def __init__(self):
        self.__listaCosecha = []                    #CONSTRUCTOR DE LA LISTA

    def agregarCosecha(self, unaCosecha):           #AGREGO ELEMENTO A LA LISTA COSECHA
        self.__listaCosecha.append(unaCosecha)

    def getCosechaDia(self, camion, dia):           #BUSCO EN LA LISTA LA COSECHA ESPECIFICA POR DIA
        return self.__listaCosecha[camion][dia]

    def getCosechaCamion(self, camion):             #BUSCO EN LA LISTA UN CAMION ESPECIFICO
        return self.__listaCosecha[camion]

    def getCosecha(self):                           #RETORNA TODOS LOS VALORES DE LA LISTA
        return self.__listaCosecha

    def __str__(self):                              #Metodo que crea el listado en pantalla
        s = ""
        for camion in self.__listaCosecha:
            s += str(camion) + '\n'
        return s

    def testCosecha(self):                          #Creo instancias a partir de un archivo
        archivo = open('Cosecha.csv')               #Abro el Archivo cosecha.cs
        reader = csv.reader(archivo, delimiter=',') #Especifico el separador
        for fila in reader:                         #Por cada fila en el archivo
            unaCosecha = [int(fila[0]),int(fila[1]),int(fila[2]),int(fila[3]),int(fila[4]),int(fila[5]),int(fila[6]),int(fila[7]),int(fila[8]), int(fila[9])]

            self.agregarCosecha(unaCosecha)         #CREO LAS INSTANCIAS EN LA LISTA
