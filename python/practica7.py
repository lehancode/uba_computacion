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
def CerosEnPosicionesPares(s: list[int]) -> list[int]:
  for i in range(len(s)):
    if s[i] % 2 == 0:
      s[i] = 0
  return s

# 2)
def CeroEnPosicionesPares2(s: list[int]) -> list[int]: # con una lista vacia
  s_impar: list[int] = []
  for i in range(len(s)):
    if s[i] % 2 == 0:
      s_impar.append(0)
    else:
      s_impar.append(s[i])
  return s_impar

def CeroEnPosicionesPares2v2(s:list[int]) -> list[int]: # con copy -> menos codigo
  s_impar: list[int] = s.copy()
  for i in range(len(s)):
    if s[i] % 2 == 0:
      s_impar[i] = 0
  return s_impar

# 3)
def es_vocal(letra: chr) -> bool: # con funcion auxiliar xq sino me lastimo
  vocales: list[chr] = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
  for i in range(len(vocales)):
    if letra == vocales[i]:
      return True
  return False

def sin_vocales(cadena: str) -> str:
  salida: str = ""
  for i in range(len(cadena)):
    if not(es_vocal(cadena[i])):
      salida += cadena[i]
  return salida

# 4) este es casi lo mismo ..
def pertenece3(list: list[chr], letra: chr) -> bool: #pertenece3, muchos pertenece 
  for i in range(len(list)):
    if letra == list[i]:
      return True
  return False  

def reemplaza_vocales(s: str) -> str:
  res: str = ""
  for i in range(len(s)):
    if pertenece3(["a", "e", "i", "o", "u"], s[i]):
      res += "-"
    else:
      res += s[i]
  return res 

# 5)
def da_vuelta_str(s: str) -> str:
  res: str = ""
  iterador: int = len(s) - 1
  for i in range(len(s)):
    res += s[iterador]
    iterador -= 1
  return res 

# 6)
def pertenece4(list: str, letra: chr) -> bool: #pertenece4, muchos pertenece 
  for i in range(len(list)):
    if letra == list[i]:
      return True
  return False  

def eliminar_repetidos(s: str) -> str:
  res: str = ""
  for i in range(len(s)):
    if not(pertenece3(res, s[i])):
      res += s[i]
  return res 

# Ejercicio 3
def resultadoMateria(notas: list[int]) -> int:
  total_notas: int = 0
  for i in range(len(notas)):
    if notas[i] < 4:
      return 3 
    total_notas += notas[i]
  promedio: float = (total_notas) / len(notas) # nota mental: // -> division entera / -> division 
  if promedio >= 7:
    return 1
  elif promedio >= 4 and promedio < 7:
    return 2
  else:
    return 3

# Ejercicio 4
def saldo_actual(cuenta: list[(chr,int)]) -> int:
  saldo: int = 0
  for i in range(len(cuenta)):
    if cuenta[i][0] == "I":
      saldo += cuenta[i][1]
    else:
      saldo -= cuenta[i][1]
  return saldo

# Ejercicio 5
def pertenece(lista: list[int], e: int) -> bool:
  for i in range(len(lista)):
    if e == lista[i]:
      return True
  return False

def pertenece_a_cada_uno_version_1(s: list[list[int]], e: int, res: list[bool]) -> None:
  res.clear()
  for i in range(len(s)):
    res.append(pertenece(s[i], e))
  return 

def pertenece_a_cada_uno_version_3(s: list[list[int]], e: int) -> list[bool]:
  res: list[bool] = []
  for i in range(len(s)):
    res.append(pertenece(s[i], e))
  return res
# La version 2 tiene un cambio en cuanto a la longitud del asegura pero el segundo asegura hace que sea
# irrelevante cual elegir, luego el 3 en vez de tomar una secuencia de bool devuelve una.

# Ejercicio 6
# 1)
def es_matriz(s:list[list[int]]) -> bool:
  i: int = 0
  if len(s) == 0 or len(s[0]) == 0:
    return False
  while i < len(s):
    if len(s[0]) != len(s[i]):
      return False
    else:
      i += 1
  return True

# 2)
def filas_ordenadas(m: list[list[int]], res: list[bool]) -> None:
  for i in range(len(res)):
    res[i] = ordenados(m[i]) 
  return res # TEORICAMENTE, no deberia poner nunca return por la especificación pero lo estoy dejando por comodidad

# 3)
def columna(m: list[list[int]], c: int) -> list[int]:
  res: list[int] = []
  for i in range(len(m)):
    res.append(m[i][c])
  return res

# 4)
def columnas_ordenadas(m: list[list[int]]) -> list[bool]:
  res: list[bool] = []
  for c in range(len(m[0])):
    res.append(ordenados(columna(m,c)))
  return res 

# 5)
def transponer(m: list[list[int]]) -> list[list[int]]:
  transpuesta: list[list[int]] = []
  for i in range(len(m[0])):
    transpuesta.append(columna(m, i))
  return transpuesta

# 6)
def verticales(m: list[list[chr]], letra: chr) -> bool:
  vertical: list[list[int]] = transponer(m)
  contador: int = 0
  for fila in range(len(m)):
    for i in range(len(m)):
      if vertical[fila][i] == letra:
        contador += 1
    if contador == 3:
      return True 
    else:
      contador = 0
  return False
    
def horizontales(m:list[list[chr]], letra: chr) -> bool:
  contador: int = 0
  for fila in range(len(m)):
    for i in range(len(m)):
      if m[fila][i] == letra:
        contador += 1
    if contador == 3:
      return True
    else:
      contador = 0
  return False

def diagonales(m:list[list[chr]], letra: chr) -> bool: # para esta de la forma mas imbecil
  return (m[0][0] == m[1][1] == m[2][2] == letra) or (m[0][2] == m[1][1] == m[2][0] == letra)

def quien_gana_tateti(m: list[list[chr]]) -> int:
  if verticales(m, "O") or horizontales(m, "O") or (diagonales(m, "O")):
    return 0
  elif verticales(m, "X") or horizontales(m, "X") or (diagonales(m, "X")):
    return 1
  else:
    return 2
  
# 7) te la debo maestro

# Ejercicio 7
# 1)
def nombres() -> list[str]:
  lista: list[str] = []
  nombre: str = "nombre"
  while (nombre != "listo"):
    nombre = input("Ingrese el nombre: ")
    if nombre == "" or nombre == "listo":
      break
    lista.append(nombre)
  return lista 

# 2)
def historial_SUBE() -> list[(chr,int)]:
  saldo: int = 0
  historial: list[(chr,int)] = []
  operacion: chr = ''
  while operacion != 'X':
    operacion: chr = input("Ingrese una opción ('C': Cargar, 'D': Descontar, 'X': Finalizar): ")
    if operacion == 'C':
      monto: int = int(input("Ingrese un monto: "))
      saldo += monto 
      historial.append(('C', saldo))
    elif operacion == 'D':
      monto: int = int(input("Ingrese un monto: "))
      saldo -= monto
      historial.append(('D', saldo))
  print("Su saldo actual es de " + str(saldo) + "pesos")
  return historial 

# 3) te la debo

# 4)
def tieneMayuscula(contraseña: str) -> bool:  
  for letra in contraseña:
    if ('A' <= letra <= 'Z') or letra == 'Ñ':
      return True
  return False

def tieneMinuscula(contraseña: str) -> bool:
  for letra in contraseña:
    if ('a' <= letra <= 'z') or letra == 'ñ':
      return True
  return False

def tieneDigit(contraseña: str) -> bool:
  for letra in contraseña:
    if '0' <= letra <= '9':
      return True
  return False

def fortaleza(contraseña: str) -> str:
  if len(contraseña) < 5:
    return "ROJA"
  elif tieneDigit(contraseña) and tieneMayuscula(contraseña) and tieneMinuscula(contraseña):
    return "VERDE"
  else:
    return "AMARILLA"
