from modelos.Dispositivo import Dispositivo
from modelos.util import crear_dispositivos, buscar_dispositivo


class Principal:
    """
    Esta clase correra todo el proyecto.
    """
    ##Vamos a solicitarle datos al usuario
    # procesdor_ = input("Por favor digite la velocidad del procesador del dispositivo: ")
    # ram_ = input("Por favor digite la velocidad de la RAM del dispositivo: ")
    # pantalla_ = input("Por favor digite el tamanio de pantalla del dispositivo: ")
    # peso_ = input("Por favor digite el peso del dispositivo: ")
    #
    # dispositivo_ = Dispositivo(pantalla_, peso_, procesdor_, ram_)
    # print('Las caracterisiticas del Dispositivo son:: Pantalla: {}, Procesador: {},  RAM: {}, Peso: {}'.format(
    #     dispositivo_.pantalla, dispositivo_.procesador, dispositivo_.ram, dispositivo_.peso))
    dispositivos = []

    for x in range(150):
        dispositivos.append(crear_dispositivos())

    # for d in dispositivos:
    #     print('La Marca es: {}, Pantalla: {}, Procesador: {},  RAM: {}'.format(d.marca,
    #                                                                            d.pantalla, d.procesador, d.ram)
    #           )
    dispositivos_=[]

    for d in dispositivos:
        dispositivos_.append(d.to_dict())

    print(dispositivos_)
    # invocamos la funcion que simulara la busqueda
    buscar_dispositivo(dispositivos_)

