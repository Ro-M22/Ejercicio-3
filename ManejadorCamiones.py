import csv

from Camion import Camion

class ManejadorCamiones:
    #__listaCamiones = []

    def __init__(self):
        self.__listaCamiones = []

    def agregarCamion(self, unCamion):
        self.__listaCamiones.append(unCamion)       ###Agrego camion a la lista

    def buscarCamion(self, numero):                                         #METODO PARA BUSCAR UN CAMION
        for indice, camion in enumerate(self.__listaCamiones):              #VARIABLE INDICE GUARDA JUSTAMENTE ESO
            if camion.getID() == numero:   ###################MODIFICADO
                #Si el numero de camion es el mismo que busco
                return indice                                               #Retorna el indice


    def getCamion(self, numero):                                            #DEVUELVE SOLO UN CAMION DE LA LISTA
        return self.__listaCamiones[numero]

    def getCamiones(self):
        return self.__listaCamiones                                         #DEVUELVE TODOS LOS CAMIONES EN FORMA DE LISTADO


    def borrarCamion(self, numero):                                         #Elimino un camion
        indice = self.buscarCamion(numero)                              #Guardo en indice el camion a borrar
        if indice != None:                                                  #si el indicie es disitinto a nada
            self.__listaCamiones.pop(indice)                                #Saco de la lista el indice
            return indice                                                   #devuelvo el indice que saque


    def __str__(self):                                                      #construye el listado en pantalla
        s = ""
        for camion in self.__listaCamiones:
            s += str(camion) + '\n'
        return s


    def testCamiones(self):
        archivo = open('Camiones.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            id = int(fila[0])
            nombre = fila[1]
            patente = fila[2]
            marca = fila[3]
            tara = int(fila[4])
            unCamion = Camion(id, nombre, patente, marca, tara)
            self.agregarCamion(unCamion)



