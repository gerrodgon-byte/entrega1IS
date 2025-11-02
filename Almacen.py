'''
Created on 1 nov 2025

@author: Gerard (US)
'''

from dataclasses import dataclass
from random import random, choice, randint


# Clase auxiliar para las coordenadas
@dataclass(frozen=True)
class Coordenadas2D:
    """
    Representa coordenadas geográficas en dos dimensiones.
    - latitud: float
    - longitud: float
    """
    latitud: float
    longitud: float

    def __str__(self):
        return f"{self.latitud},{self.longitud}"
    
    
# Diseñamos la clase Almacen

@dataclass(frozen=True)
class Almacen:
    
    # Propiedades básicas
    
    codigo: int
    nombre: str
    ciudad: str 
    coordenadas: Coordenadas2D
    
    # Métodos de factoría
    
    @staticmethod 
    def of (codigo:int, nombre:str, ciudad:str, latitud:float, longitud:float) -> 'Almacen':
        return Almacen(codigo, nombre, ciudad, Coordenadas2D(latitud, longitud))

    @staticmethod 
    def parse (linea: str) -> 'Almacen':
        lista = linea.strip().split(",")
        codigo = lista[0]
        nombre = lista[1]
        ciudad = lista[2]
        latitud = float(lista[3])
        longitud = float(lista[4])
        return Almacen.of(codigo, nombre, ciudad, latitud, longitud)
    
    @staticmethod 
    def random() -> 'Almacen':
        codigos = randint(100, 999)
        nombres = ['Prendas', 'Electrodomésticos', 'Herramientas', 'Juguetes', 'Papelería']
        ciudades = {
            'Sevilla': (37.38283, -5.97317),
            'Madrid': (40.4168, -3.7038),
            'Barcelona': (41.3851, 2.1734),
            'Valencia': (39.4699, -0.3763),
            'Bilbao': (43.2630, -2.9350),
            'Granada': (37.1773, -3.5986),
            'Zaragoza': (41.6488, -0.8891)
        }
        ciudad = choice(list(ciudades.keys()))
        nombre = choice(nombres)
        latitud, longitud = ciudades[ciudad]
        return Almacen.of(codigos, nombre, ciudad, latitud, longitud)
    
    # Propiedades secundarias: Representación como cadena
    
    def __str__(self) -> str:
        return f"{self.codigo},{self.nombre},{self.ciudad},{self.coordenadas.latitud},{self.coordenadas.longitud}"

if __name__ == '__main__':
    # Llamada a los métodos y muestra en consola
    print('of:', Almacen.of(101, 'Prendas', 'Sevilla', 37.38283, -5.97317))
    print('parse:', Almacen.parse('102,Electrodomésticos,Madrid,40.4168,-3.7038'))
    print('random:', Almacen.random())
    almacen = Almacen.of(103, 'Juguetes', 'Valencia', 39.4699, -0.3763)
    print('str:', str(almacen))