'''
Created on 29 oct 2025

@author: Gerard (US)
'''
from datetime import datetime
import math

def es_fecha_valida(dia:int, mes:int, año:int) -> bool:
    '''Si la fecha es válida dentro del formato adecuado y no es domingo devuelve True,
    en caso contrario devuelve False.'''
    try:
        fecha = datetime(año, mes, dia)
        if fecha.weekday() == 6:  # Domingo es 6
            return False
        return True
    except ValueError:
        return False 
    
    

    
def producto(n:int, k:int) -> int:
    ''' Devuelve el producto de n * (n+1) * ... * (n+k-1), siendo siempre n>=k y ambos enteros positivos. '''
    if k < 0:
        raise AssertionError("k debe ser mayor o igual que 0")
    if n < k:
        raise AssertionError("n debe ser mayor o igual que k")
    resultado = 1
    for i in range(k):
        resultado *= (n + i)
    return resultado
     
     
     
     
def secuencia_geom(a:float, r:float, n:int) -> float:
    '''Devuelve el producto de los primeros n términos de una sucesión geométrica.'''
    if n < 1:
        raise AssertionError("n debe ser mayor o igual que 1")
    producto = 1.0
    for i in range(n):
        producto *= a * (r ** i)
    return producto



def combinatorio(n:int, k:int) -> int:
    '''Devuelve el número combinatorio n k, su valor'''
    if n<k:
        raise AssertionError("n debe ser mayor o igual que k")
    return math.factorial(n) // (math.factorial(n-k) * math.factorial(k))



def SNK(n:int, k:int) -> float:
    '''Devuelve un número resultante de 1/(k!)x(sum[i=0, k-1]((-1)**i)* comb(k+1, i+1)* (k-i)^n)'''
    if k < 0:
        raise AssertionError("k debe ser mayor o igual a 0")
    if n < k:
        raise AssertionError("n debe ser mayor o igual a k")
    suma = 0
    for i in range(k):
        suma += ((-1) ** i) * combinatorio(k+1, i+1) * ((k - i) ** n)
    return suma / math.factorial(k)
    
    
    
if __name__ == '__main__':
    print(es_fecha_valida(15, 3, 2025))
    print(es_fecha_valida(29, 2, 2024))
    print(producto(5, 3))
    print(secuencia_geom(2.4, 3.6, 1))
    print(combinatorio(6, 5))