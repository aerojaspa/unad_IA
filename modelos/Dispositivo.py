"""
from pymysql import connect

conn = connect(host="localhost", user="root", password="adminadmin", db="REGISTRO_DISPOSITIVO")
"""


class Dispositivo(object):
    """Con esta clase creamos dispositivos al azar"""
    def __init__(self, pantalla, peso, procesador, ram, marca=""):
        self.pantalla = pantalla
        self.peso = peso
        self.procesador = procesador
        self.marca = marca
        self.ram = ram

    ##para poder usar dataframe se debe retornar el objeto como diccionario
    def to_dict(self):
        return {
            'procesador': self.procesador,
            'ram': self.ram,
            'pantalla': self.pantalla,
            'peso': self.peso,
            'marca': self.marca
        }





