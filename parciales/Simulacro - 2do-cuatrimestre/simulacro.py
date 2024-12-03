from queue import Queue as Cola

# Ejercicio 1
def pertenece(elem: str, coleccion: dict):
  claves: list[str] = coleccion.keys()
  for i in claves:
    if i == elem:
      return True
  return False   
# [('juan', 'jabon', 30), ('mario', 'detergente', 15),('juan', 'shampoo', 27)]
# -> {
#     'juan': [('jabon', 30),('shampoo', 27)]
#     'mario': [('detergente', 15)]
#    }
def gestion_ventas(ventas_empleado_producto: list[tuple[str, str, int]]) -> dict[str, list[tuple[str,int]]]:
  res: dict[str,list[tuple[str,int]]] = {}
  for e,p,c in ventas_empleado_producto:
    venta: tuple[str,int] = (p,c)
    if not pertenece(e, res):
      res[e] = [venta]
    else:
      lista: list[tuple[str,int]] = res[e]
      lista.append(venta)
  print(ventas_empleado_producto)
  return res

# Ejercicio 2
def cantidad_digitos_impares(numeros: list[int]) -> int:
  copia: list[int] = numeros.copy()
  copia = separar_en_digitos(copia)
  contador: int = 0
  for num in copia:
    if num % 2 == 1:
      contador += 1
  return contador

def separar_en_digitos(numeros: list[int]) -> list[int]:
  copia: list[str] = []
  res: list[int] = []
  for num in numeros:
    copia.append(str(num))
  for c in copia:
    for digito in c:
      res.append(int(digito))
  return res 

# Ejercicio 3
def reordenar_cola_primero_numerosas(carpetas: Cola[tuple[str,int]], umbral:int) -> Cola[tuple[str,int]]:
  copia: Cola[tuple[str,int]] = copiar_cola(carpetas)
  lista: list[tuple[str,int]] = []
  colamenores = Cola()
  colamayores = Cola()
  res: Cola[tuple[str,int]] = Cola()
  while not(copia.empty()):
    lista.append(copia.get())
  for i in range (len(lista)):
    if lista[i][1] <= umbral:
      colamenores.put(lista[i])
    elif lista[i][1] > umbral:
      colamayores.put(lista[i])
  while not(colamayores.empty()):
    res.put(colamayores.get())
  while not(colamenores.empty()):
    res.put(colamenores.get())
  return res 

def copia_cola(carpetas: Cola[tuple[str,int]]) -> Cola[tuple[str,int]]:
  res: Cola[tuple[str,int]] = Cola()
  copia: Cola[tuple[str,int]] = carpetas
  while not(copia.empty()):
    elem = copia.get()
    res.put(elem)
  while not(res.empty()):
    elem = res.get()
    copia.put(elem)
  return copia

# Ejercicio 4
def maximo(columna: list[int]) -> int:
  res: int = 0
  for n in columna:
    if n > res:
      res = n
  return res 

def obtener_columna(matriz: list[list[int]], columna: int) -> list[int]:
  res: list[int] = []
  for f in matriz:
    res.append(f[columna])
  return res

def obtener_columnas(matriz: list[list[int]]) -> list[list[int]]:
  columnas: list[list[int]] = []
  for f in range(len(matriz)):
    columna: list[int] = obtener_columna(matriz, f)
    columnas.append(columna)
  return columnas

def matriz_cuasi_decreciente(matriz: list[list[int]]) -> bool:
    res: bool = True 
    columnas: list[list[int]] = obtener_columnas(matriz)
    maximo_columna_i: int = maximo(columnas[0])
    col_actual: int = 1

    while (res and col_actual < len(columnas)):
      maximo_col_i_mas_1: int = maximo(columnas[col_actual])
      res = (maximo_columna_i > maximo_col_i_mas_1)
      col_actual += 1
      maximo_columna_i = maximo_col_i_mas_1

    return res

a = [[1,2,3],[4,3,2],[5,4,2]]
print(matriz_cuasi_decreciente(a))
print(a)

# [[1,2,3]
#  [4,3,2]
#  [5,4,2]]