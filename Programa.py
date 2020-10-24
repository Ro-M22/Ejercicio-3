from ManejadorCosecha import ManejadorCosecha
from ManejadorCamiones import ManejadorCamiones


def zero(mc,mcam):
    print("\t\t\t  >>>>  Adiós  <<<<")


def one(mc,mcam):
    m=int(input('\n\t >> Ingrese el número de camión (0 a 9): '))
    arreglo=mc.getCosechaCamion(m)
    suma=0
    for dia in arreglo:
        suma+=dia
    print('\n\t -Kilos descargados: {0}'.format(suma))
    print("\t -Por el camión: ", mcam.getCamion(m).getMarca())
    input('\n \t--> Presione enter para continuar')
    print('\n\n---------------------------------------------------------------')

def two(mc,mcam):
    m=int(input('\n\t >>Ingrese el día a consultar (0 a 9):'))
    print('\n\n \t  Patente    Conductor   Cantidad de Kilos')
    for i in range(len(mcam.getCamiones())):
        print("\t %7s  %12s   %8d " % (mcam.getCamion(i).getPatente(), mcam.getCamion(i).getConductor(), mc.getCosechaDia(i,m)-mcam.getCamion(i).getTara()))

    input('\n \t--> Presione enter para continuar')
    print('---------------------------------------------------------------')



switcher = {
    0: zero,
    1: one,
    2: two
}

def switch(argument,mc,mcam):
    func = switcher.get(argument, lambda x,y: print("\t\t\t  \tOpción incorrecta\n-----------------------------------------------------\n "))
    func(mc,mcam)

if __name__ == '__main__':

    mc = ManejadorCosecha()
    mcam = ManejadorCamiones()

    mc.testCosecha()
    mcam.testCamiones()

    bandera = False                                     # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print('\n\n\t\t############################')
        print("\t\t# 0- Salir                 #")
        print("\t\t# 1- Consulta por Camión   #")
        print("\t\t# 2 -Consulta por Día      #")
        print('\t\t############################')
        opcion= int(input("\n\t\t>>Ingrese una opción: "))
        print('\n\n-----------------------------------------------------')
        switch(opcion,mc,mcam)
        bandera = int(opcion) == 0                       # Si lee el 0 cambia la bandera a true y sale del menú