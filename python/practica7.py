import math as math

# Ejercicio 1
# 1)
def pertenece(s: list[int], e: int) -> bool:
  for i in range(0, len(s)):
    if e == s[i]:
      return True
  return False

def pertenece2(s: list[int], e: int) -> bool:
  i: int = 0
  while i < len(s):
    if s[i] == e:
      return True
    i += 1
  return False

# 2)
def divide_a_todos(s: list[int], e: int) -> bool:
  for i in range(0, len(s)):
    if not(s[i] % e == 0):
      return False
  return True

# 3)
def suma_total(s: list[int]) -> int:
  total: int = 0
  for i in range(0, len(s)):
    total += s[i]
  return total

# 4)
def maximo(s: list[int]) -> int:
  res: int = s[0]
  for i in range(0, len(s)):
    if s[i] > res:
      res = s[i]
  return res 

# 5)
def minimo(s: list[int]) -> int:
  res: int = s[0]
  for i in range(0, len(s)):
    if s[i] < res:
      res = s[i]
  return res 

# 6)
def ordenados(s: list[int]) -> bool:
  for i in range(0, len(s)-1):
    if s[i] > s[i+1]:
      return False
  return True 

# 7)
def pos_maximo(s: list[int]) -> int:
  if len(s) == 0:
    return -1
  indice: int = 0
  for i in range(1, len(s)):
    if s[indice] < s[i]:
      indice = i
  return indice 
# pos_maximo2 con una variable extra para iterar
def pos_maximo2(s: list[int]) -> int:
  if len(s) == 0:
    return -1
  indice: int = 0
  maximo: int = s[0]
  for i in range(len(s)):
    if s[i] > maximo:
      maximo = s[i]
      indice = i
  return indice

# 8)
def pos_minimo(s: list[int]) -> int:
  if len(s) == 0:
    return -1
  else:
    indice: int = 0
    for i in range(1, len(s)):
      if s[i] <= s[indice]:
        indice = i 
  return indice

# 9)
def longitud_mayor_a_7(seq: list[str]) -> bool:
  for i in range(len(seq)):
    if len(seq[i]) > 7:
      return True
  return False

# 10) 
def es_palindromo(texto: str) -> bool:
  if len(texto) == 0 or len(texto) == 1:
    return True
  else:
    dado_vuelta: str = ""
    for i in range(len(texto)-1, -1, -1):
      dado_vuelta += texto[i]
    if texto == dado_vuelta:
      return True
  return False

# 11)
def tres_num_consecutivos(s: list[int]) -> bool:
  contador: int = 0
  indice: int = 0
  for i in range(1, len(s)):
    if s[i] == s[indice]:
      contador += 1
      indice = i
      if contador == 2:
        return True 
    else:
      contador = 0
      indice = i
  return False 
    
# 12)
def vocales_distintas(s: str) -> bool:
  vocales: list[str] = ["a", "e", "i", "o", "u"]
  contador: int = 0
  for char in range(len(s)):
    for j in range(len(vocales)):
      if s[char] == vocales[j]:
        vocales.pop(j)
        contador += 1
        break
  return contador >= 3

# 13)
def indice_seq_ordenada(s: list[int]) -> int:
  iter: int = 0
  indice_actual: int = 0
  indice_mayor: int = 0
  cantidad_actual: int = 1
  cantidad_mayor: int = 1
  for i in range(1, len(s)):
    if s[i] > s[iter]:
      cantidad_actual += 1
    else:
      if cantidad_actual > cantidad_mayor:
        cantidad_mayor = cantidad_actual
        indice_mayor = indice_actual
      cantidad_actual = 1
      indice_actual = i
    iter += 1
    if cantidad_actual > cantidad_mayor:
      indice_mayor = indice_actual
  return indice_mayor    

# 14)
def cantidad_digitos_impares(s: list[int]) -> int:
  contador: int = 0
  for i in s:
    num: int = i
    while num > 0:
      if (num % 10) % 2 == 1:
        contador += 1
      num = (num // 10)
  return contador

# Ejercicio 2
# 1)