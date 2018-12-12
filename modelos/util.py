import random
import numpy as np
import pandas
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from modelos.Dispositivo import Dispositivo


"""
Este diccionario simplemente define procesadores
por nombre y velocidad en GHz
"""
procesadores = {
    "Snap Dragon": "2.4",
    "Intel": "1.8",
    "Spark": "2.6",
    "A12": "2.6"
}

"""Esta es la lista con las velocidades de ram"""
rams = (2, 4, 6)

"""Esta es la lista de los tamaños de pantalla"""
pantallas = (5.5, 6, 4.5)


"""Esta esa la lista de los pesos mas comunes en gramos"""
pesos = (120, 130, 135, 160, 170)

"""Marcas mas comunes"""
marcas = ("Samsung", "Iphone", "ASUS", "Motorola", "Xiaomi")

def crear_dispositivos():
    pantalla = random.choice(pantallas)
    peso = random.choice(pesos)
    ##procesador = random.choice(procesadores.values())
    procesador, velocidad = random.choice(list(procesadores.items()))
    ram = random.choice(rams)
    marca = random.choice(marcas)
    dispositivo = Dispositivo(pantalla, peso, velocidad, ram, marca)

    return dispositivo

def buscar_dispositivo(dispositivos):
    """"
    Esta funcion es usada para buscar en profundidad un dispositivo
    ya sea en profundidad u horizontal
    """
    data = pandas.DataFrame(dispositivos)
    data.head()
    data.shape
    ## Aca vemos el histograma de los celulares
    plt.hist(data.marca)
    ## Acá eliminamos los repetidos por parca si los hay con características iguales
    data.marca.unique()

    ##Seteamos las colunnas y los predictores y objetivos (targets)
    ##para intentar clasificar los dispositivos en un target por las características
    colnames = data.columns.values.tolist()
    print(colnames)
    #las columnas predictoras son las caracteristicas
    predictors = colnames[1:4]
    #la columna target es la marca
    target = colnames[0]

    ##gneramos un dataset de entrenamiento por medio de una distribución uniforme
    data["is_train"] = np.random.uniform(0, 1, len(data)) <= 0.75

    ##organizamos dos conjuntos para entrenamiento y prueba
    train, test = data[data["is_train"] == True], data[data["is_train"] == False]

    ##Creamos un arbol de decision
    ##clasificando con entropia
    ##diviendo en 20 nodos u observaciones minimas para clasificar
    tree = DecisionTreeClassifier(criterion="entropy", min_samples_split=20, random_state=99)

    ##modelamos el arbol con los datos del conjunto de entrenamiento
    tree.fit(train[predictors], train[target])

    ##por medio de la selección de las variables de predicción clasificamos el dispositivo
    ##Ahora vamos a predecir por medio del arbol
    preds = tree.predict(test[predictors])

    ##para realizar la predicción, usamos pandas cruzando las prediociones y objetivos usando solo las caracteristicas
    ##de los dospositivos
    predicciones = pandas.crosstab(test[target], preds, rownames=["Actual"], colnames=["Predictions"])

    ##La matriz que imprime muestra que dispositivos pudieron ser correctamente clasificados donde las columnas cruzan
    ##de forma absoluta con las filas. Pero como se generan los datos de forma aleatoria, es poco probable que existe
    ##un cruce exacto.
    print(predicciones)









