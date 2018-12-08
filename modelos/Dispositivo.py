from pymysql import connect

conn = connect(host="localhost", user="root", password="adminadmin", db="REGISTRO_DISPOSITIVO")

class Dispositivo:

    def __init__(self, alto, bajo, peso, procesador, ram):
        self.alto = alto
        self.bajo = bajo
        self.peso = peso
        self.procesador = procesador
        self.ram = ram





