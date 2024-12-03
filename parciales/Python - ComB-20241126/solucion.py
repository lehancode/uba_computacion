from queue import Queue as Cola
from typing import TypeVar
T = TypeVar('T')

# Ejercicio 1
def subsecuencia_mas_larga(v: list[int]) -> tuple[int,int]:
  longitud: int = 0
  indice: int = 0
  indice_actual: int = 0
  longitud_actual: int = 1

  for i in range(len(v)-1):
    if abs(v[i] - v[i+1]) != 1:
      if longitud_actual > longitud:
        longitud = longitud_actual
        indice = indice_actual  
      indice_actual = i + 1
      longitud_actual = 1
    else:
      longitud_actual += 1
  if longitud_actual > longitud:
    longitud = longitud_actual
    indice = indice_actual

  return (longitud, indice)    

# Ejercicio 2
def mejor_resultado_de_ana(examenes: Cola[list[bool]]) -> list[int]:
  examenes_copia: Cola[list[bool]] = Cola()
  res: list[int] = []

  while not examenes.empty():
    examen = examenes.get()
    examenes_copia.put(examen)
    res.append(cantidad_respuestas_correctas(examen))
  
  while not examenes_copia.empty():
    examenes.put(examenes_copia.get())
  
  return res 

def cantidad_respuestas_correctas(examen: list[bool]) -> int:
  verdaderas: int = 0
  falsas: int = 0

  for respuesta in examen:
    if respuesta == True:
      if verdaderas < (len(examen) / 2):
        verdaderas += 1
    if respuesta == False:
      if falsas < (len(examen) / 2):
        falsas += 1
  
  return verdaderas + falsas 

# Ejercicio 3
def cambiar_matriz(A: list[list[int]]) -> None:
    maximo_elemento: int = len(A) * len(A[0])
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = (A[i][j] % maximo_elemento) + 1
            
# Ejercicio 4
def palabras_por_vocales(texto: str) -> dict[int,int]:
  vocales_palabras: dict[int,int] = {}
  contador: int = 0
  es_palabra: bool = False

  for char in texto:
    if char != ' ':
      if pertenece(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'], char): 
        contador += 1
        es_palabra = True 
      else:
        es_palabra = True 
    else:
      if es_palabra:
        if pertenece(list(vocales_palabras.keys()), contador):
          vocales_palabras[contador] += 1
        else:
          vocales_palabras[contador] = 1
      es_palabra = False 
      contador = 0

  if len(texto) != 0 and es_palabra:
    if pertenece(list(vocales_palabras.keys()), contador):
      vocales_palabras[contador] += 1
    else:
      vocales_palabras[contador] = 1
  
  return vocales_palabras

def pertenece(l: list[T], objeto: T) -> bool:
  for elem in l:
    if objeto == elem:
      return True 
  return False 
