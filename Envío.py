'''
Created on 1 nov 2025

@author: Gerard (US)
'''


from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from .Transporte import Transporte

@dataclass(frozen=True)
class Envio:
    
    # Propiedades protegidas
    
    _codigo: int = field(init=False, repr=False)
    _fecha_peticion: datetime
    _al1: int
    _al2: int
    _transporte: Optional[Transporte] = None
    _fecha_de_salida: Optional[datetime] = None
    _fecha_de_llegada: Optional[datetime] = None

    # Variable de clase para autogenerar códigos únicos
    _codigo_counter: int = 0

    def __post_init__(self):
        # Asignación de código único
        object.__setattr__(self, '_codigo', self._get_next_codigo())

    @classmethod
    def _get_next_codigo(cls):
        cls._codigo_counter += 1
        return cls._codigo_counter

    # Getters para acceder a las propiedades protegidas
    @property
    def codigo(self):
        return self._codigo
    @property
    def fecha_peticion(self):
        return self._fecha_peticion
    @property
    def al1(self):
        return self._al1
    @property
    def al2(self):
        return self._al2
    @property
    def transporte(self):
        return self._transporte
    @property
    def fecha_de_salida(self):
        return self._fecha_de_salida
    @property
    def fecha_de_llegada(self):
        return self._fecha_de_llegada

    # Método de factoría
    @staticmethod
    def of(fecha_peticion: datetime, al1: int, al2: int, transporte: Optional[Transporte] = None, fecha_de_salida: Optional[datetime] = None, fecha_de_llegada: Optional[datetime] = None) -> 'Envio':
        return Envio(
            _fecha_peticion=fecha_peticion,
            _al1=al1,
            _al2=al2,
            _transporte=transporte,
            _fecha_de_salida=fecha_de_salida,
            _fecha_de_llegada=fecha_de_llegada
        )

    # Otro método
    @staticmethod
    def Envios(fecha: datetime, almacenes: List[int]) -> List['Envio']:
        envios = []
        for i in range(len(almacenes) - 1):
            al1 = almacenes[i]
            al2 = almacenes[i + 1]
            # Se asume transporte válido (puedes ajustar la lógica si tienes una función para obtenerlo)
            envio = Envio.of(fecha, al1, al2)
            envios.append(envio)
        return envios

    def __str__(self):
        transporte_str = f", Transporte: {self.transporte}" if self.transporte else ""
        return (f"Envio(Codigo: {self.codigo}, FechaPeticion: {self.fecha_peticion}, "
                f"AlmacenOrigen: {self.al1}, AlmacenDestino: {self.al2}, "
                f"FechaSalida: {self.fecha_de_salida}, FechaLlegada: {self.fecha_de_llegada}{transporte_str})")

if __name__ == '__main__':
    print('***********')
    print('Creación de un envío con of():')
    fecha_peticion = datetime(2025, 9, 29, 10, 0, 0)
    envio1 = Envio.of(fecha_peticion, 1, 2)
    print(f'Fecha petición: {envio1.fecha_peticion}')
    print(f'Almacén origen: {envio1.al1}')
    print(f'Almacén destino: {envio1.al2}')
    print(f'Transporte asociado: {envio1.transporte}')
    print(f'Fecha de salida: {envio1.fecha_de_salida}')
    print(f'Fecha de llegada: {envio1.fecha_de_llegada}')
    print('***********')
    print('Creación de una cadena de envíos con envios():')
    almacenes = [1, 2, 3, 4]
    print(f'La lista de almacenes es: {almacenes} y la fecha de petición es la misma que el envío que se creó anteriormente.')
    envios = Envio.Envios(fecha_peticion, almacenes)
    for idx, envio in enumerate(envios, 1):
        fecha_pet = envio.fecha_peticion if idx == 1 else None
        print(f'Envio {idx}: al1={envio.al1}, al2={envio.al2}, fecha_peticion={fecha_pet}, salida={envio.fecha_de_salida}, llegada={envio.fecha_de_llegada}')