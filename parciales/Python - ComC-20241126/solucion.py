from queue import LifoQueue as Pila
import math
from typing import TypeVar

T = TypeVar('T')

def pertenece(cadena: list[T], elem: T) -> bool:
  for i in cadena:
    if i == elem:
      return True
  return False

# Ejercicio 1
def multiplos_de_primos(v: list[int]) -> dict[int,int]: # dificultad facil 
  primos: int = obtener_primos(maximo(v))
  res_total: dict[int,int] = {}

  for p in primos:            #creo dict con primos
    res_total[p] = 0
  
  for p in primos:
    for num in v:
      if num % p == 0:        #veo por cada primo, todos los numeros en v que son divisibles por este
        res_total[p] += 1
  
  res: dict[int,int] = {}      #elimino los primos que no dividen a nadie
  for p in res_total.keys():
    if res_total[p] > 0:          
      res[p] = res_total[p] 

  return res    
    
def obtener_primos(n: int) -> dict[int,int]: # criba de eratostenes
  es_primo: list[bool] = [True] * (n+1)
  es_primo[0] = es_primo[1] = False
  primos: list[int] = []

  for p in range(2, int((math.sqrt(n))) + 1):
    if es_primo[p]:
      for multiplo in range(p*p, n + 1, p):
        es_primo[multiplo] = False 

  for i in range(n+1):
    if es_primo[i] == True:
       primos.append(i)
  
  return primos

def maximo(l: list[int]) -> int:
  res: int = 0
  for n in l:
    if n > res:
      res = n
  return res


# Ejercicio 2
def longitud_mas_grande(m: list[list[int]]) -> int:  #[[1,1],[0,1,1,1,1,0]]
  longitud: int = 0
  longitud_actual: int = 0

  for s in m:
    longitud_actual = 0
    for i in range(len(s)):
      if s[i] == 1:
        longitud_actual += 1
      else:
        if longitud_actual > longitud:
          longitud = longitud_actual 
        longitud_actual = 0
    if longitud_actual > longitud:
      longitud = longitud_actual

  return longitud

# Ejercicio 3
def resolver_cuentas(p: Pila[str]) -> list[int]:
  p_copia: Pila[str] = Pila()
  res: list[int] = []

  while not p.empty():
    expresion = p.get()
    p_copia.put(expresion)
    res.append(calcular(expresion))
  
  while not p_copia.empty():
    p.put(p_copia.get())

  return res 

def calcular(s: str) -> int:   # "-3+5-2+10" -> 10
  cuenta: int = 0
  operador: str = '+'
  numero_actual: int = 0

  for char in s:
    if pertenece("0,1,2,3,4,5,6,7,8,9", char):
      numero_actual = numero_actual * 10 + int(char)
    else:
      if operador == '+':
        cuenta += numero_actual
      elif operador == '-':
        cuenta -= numero_actual
      operador = char 
      numero_actual = 0
  
  if operador == '+':
    cuenta += numero_actual
  elif operador == '-':
    cuenta -= numero_actual

  return cuenta

# Ejercicio 4
def dame_el_que_falta(s: list[tuple[int,int]]) -> tuple[int,int]:
    max_elemento: int = int(math.sqrt(len(s))+1)
    print(max_elemento)
    for x in range(1, max_elemento+1):
      for y in range(1, max_elemento+1):
        if not pertenece(s, (x,y)):
          return (x,y)
