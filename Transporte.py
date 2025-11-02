'''
Created on 1 nov 2025

@author: Gerard (US)
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional, Tuple
import random

class Periodicidad(Enum):
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    MONTHLY = 'MONTHLY'

@dataclass(frozen=True)
class Transporte:
    # Propiedades básicas
    al1: int
    al2: int
    fecha: datetime
    preparacion: int
    duracion: int
    periodicidad: Periodicidad
    # Propiedades secundarias
    dia_semana: Optional[int] = None
    dia_mes: Optional[int] = None

    # Métodos de factoría
    @staticmethod
    def of(al1: int, al2: int, fecha: datetime, preparacion: int, duracion: int, periodicidad: Periodicidad, dia_semana: Optional[int] = None, dia_mes: Optional[int] = None) -> Transporte:
        return Transporte(al1, al2, fecha, preparacion, duracion, periodicidad, dia_semana, dia_mes)

    @staticmethod
    def parse(line: str) -> Transporte:
        parts = line.strip().split(',')
        al1 = int(parts[0])
        al2 = int(parts[1])
        fecha = datetime.strptime(parts[2], '%Y-%m-%d %H:%M')
        # Si hay duración, la toma; si no, usa valor por defecto (60)
        if len(parts) == 5:
            preparacion = int(parts[3])
            periodicidad = Periodicidad(parts[4])
            duracion = 60
            dia_semana = None
            dia_mes = None
        elif len(parts) == 6:
            preparacion = int(parts[3])
            duracion = int(parts[4])
            periodicidad = Periodicidad(parts[5])
            dia_semana = None
            dia_mes = None
        elif len(parts) == 7:
            preparacion = int(parts[3])
            duracion = int(parts[4])
            periodicidad = Periodicidad(parts[5])
            dia_semana = int(parts[6]) if periodicidad == Periodicidad.WEEKLY else None
            dia_mes = int(parts[6]) if periodicidad == Periodicidad.MONTHLY else None
        elif len(parts) == 8:
            preparacion = int(parts[3])
            duracion = int(parts[4])
            periodicidad = Periodicidad(parts[5])
            dia_semana = int(parts[6]) if periodicidad == Periodicidad.WEEKLY else None
            dia_mes = int(parts[7]) if periodicidad == Periodicidad.MONTHLY else None
        else:
            raise ValueError('Formato de línea inválido para Transporte')
        return Transporte(al1, al2, fecha, preparacion, duracion, periodicidad, dia_semana, dia_mes)

    # Otros métodos
    @staticmethod
    def random() -> Transporte:
        al1 = random.randint(1, 100)
        al2 = random.randint(1, 100)
        fecha = datetime.now().replace(minute=0, second=0, microsecond=0) + timedelta(days=random.randint(0, 30), hours=random.randint(0, 23))
        preparacion = random.randint(10, 180)
        duracion = random.randint(30, 300)
        periodicidad = random.choice(list(Periodicidad))
        dia_semana = random.randint(0, 6) if periodicidad == Periodicidad.WEEKLY else None
        dia_mes = random.randint(1, 28) if periodicidad == Periodicidad.MONTHLY else None
        return Transporte(al1, al2, fecha, preparacion, duracion, periodicidad, dia_semana, dia_mes)

    def siguiente_fecha_disponible(self, f: datetime) -> Tuple[datetime, datetime]:
        if self.periodicidad == Periodicidad.DAILY:
            return self._siguiente_diaria(f)
        elif self.periodicidad == Periodicidad.WEEKLY:
            return self._siguiente_semanal(f)
        elif self.periodicidad == Periodicidad.MONTHLY:
            return self._siguiente_mensual(f)
        else:
            raise ValueError('Periodicidad desconocida')

    def _siguiente_diaria(self, f: datetime) -> Tuple[datetime, datetime]:
        base = f + timedelta(minutes=self.preparacion)
        salida = self.fecha.replace(year=base.year, month=base.month, day=base.day)
        if salida <= base:
            salida += timedelta(days=1)
        llegada = salida + timedelta(minutes=self.duracion)
        return salida, llegada

    def _siguiente_semanal(self, f: datetime) -> Tuple[datetime, datetime]:
        if self.dia_semana is None:
            raise ValueError('dia_semana debe estar definido para periodicidad WEEKLY')
        base = f + timedelta(minutes=self.preparacion)
        days_ahead = (self.dia_semana - base.weekday() + 7) % 7
        salida = self.fecha.replace(year=base.year, month=base.month, day=base.day) + timedelta(days=days_ahead)
        if salida <= base:
            salida += timedelta(weeks=1)
        llegada = salida + timedelta(minutes=self.duracion)
        return salida, llegada

    def _siguiente_mensual(self, f: datetime) -> Tuple[datetime, datetime]:
        if self.dia_mes is None:
            raise ValueError('dia_mes debe estar definido para periodicidad MONTHLY')
        base = f + timedelta(minutes=self.preparacion)
        year, month = base.year, base.month
        salida = self.fecha.replace(year=year, month=month, day=self.dia_mes)
        if salida <= base:
            month += 1
            if month > 12:
                month = 1
                year += 1
            salida = self.fecha.replace(year=year, month=month, day=self.dia_mes)
        llegada = salida + timedelta(minutes=self.duracion)
        return salida, llegada

    def __str__(self) -> str:
        return f"{self.al1},{self.al2},{self.fecha.strftime('%Y-%m-%d %H:%M')},{self.preparacion},{self.periodicidad.name}"
    
    
if __name__ == '__main__':
    print('of:', Transporte.of(1, 2, datetime(2025, 11, 2, 9, 0), 120, 180, Periodicidad.WEEKLY, dia_semana=2))
    print('parse:', Transporte.parse('23,44,2018-02-27 16:58,158,WEEKLY'))
    print('random:', Transporte.random())
    # Llamada a siguiente_fecha_disponible y muestra en consola
    transporte = Transporte.of(1, 2, datetime(2025, 11, 2, 9, 0), 120, 180, Periodicidad.WEEKLY, dia_semana=2)
    fecha_referencia = datetime(2025, 11, 1, 10, 0)
    salida, llegada = transporte.siguiente_fecha_disponible(fecha_referencia)
    print('siguiente_fecha_disponible:', salida, llegada)