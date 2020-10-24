class Camion:           #####DEFINO CLASE CAMION
    __conductor = ''
    __patente = ''
    __marca = ''
    __tara= 0


    def __init__(self, id, conductor="", patente="", marca="", tara=0):
        self.__id = id
        self.__conductor = conductor
        self.__patente = patente
        self.__marca = marca
        self.__tara = tara

    def getConductor (self):
        return self.__conductor

    def getID(self):
        return self.__id

    def getPatente(self):
        return self.__patente

    def getMarca(self):
        return self.__marca

    def getTara(self):
        return self.__tara
