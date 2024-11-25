from queue import Queue as Cola

# 1
def torneo_de_gallinas(estrategias: dict[str,str]) -> dict[str,int]:
  res: dict[str,int] = {}
  for jugador in estrategias.items():
    if jugador not in res.keys():
      res[jugador[0]] = 0
      for contrincante in estrategias.items():
        if jugador != contrincante:
          if jugador[1] == "me desvio siempre" and contrincante[1] == "me la banco y no me desvio":
            res[jugador[0]] -= 15
          elif jugador[1] == "me desvio siempre" and contrincante[1] == "me desvio siempre":
            res[jugador[0]] -= 10
          elif jugador[1] == "me la banco y no me desvio" and contrincante[1] == "me la banco y no me desvio":
            res[jugador[0]] -= 5
          elif jugador[1] == "me la banco y no me desvio" and contrincante[1] == "me desvio siempre":
            res[jugador[0]] += 10
  return res

# 2
def reordenar_cola_priorizando_vips(filaClientes: Cola[tuple[str,str]]) -> Cola[str]:
  res: Cola[str] = Cola()
  copia_clientes: Cola[tuple[str,str]] = copiar_cola(filaClientes)
  clientes_vip: Cola[tuple[str,str]] = Cola()
  clientes_comun: Cola[tuple[str,str]] = Cola()

  while not copia_clientes.empty():
    elem = copia_clientes.get()
    if elem[1] == "vip":
      clientes_vip.put(elem)
    elif elem[1] == "comun":
      clientes_comun.put(elem)

  while not clientes_vip.empty():
    cliente = clientes_vip.get()
    res.put(cliente[0])
  while not clientes_comun.empty():
    cliente = clientes_comun.get()
    res.put(cliente[0])

  return res           

def copiar_cola(c: Cola[tuple[str,str]]) -> Cola[tuple[str,str]]:
  res: Cola[tuple[str,str]] = Cola()
  copia: Cola[tuple[str,str]] = Cola()
  while not c.empty():
    elem = c.get()
    res.put(elem)
    copia.put(elem)
  while not copia.empty():
    c.put(copia.get())    
  return res

# 3
def cuantos_sufijos_son_palindromos(texto: str) -> int:
  contador: int = 0
  sufijo: str = ''
  for i in range(len(texto)-1, -1,-1):
    sufijo = texto[i] + sufijo
    if es_palindromo(sufijo) == True:
      contador += 1
  return contador  

def es_palindromo(palabra: str) -> bool:
  for i in range(len(palabra)):
    indice: int = len(palabra) - 1 - i 
    if palabra[i] != palabra[indice]:
      return False
  return True  

#def cuantos_sufijos_son_palindromos(texto: str) -> int:    [Primera version, no tan buena]
#  contador: int = 0
#  sufijos: list[str] = obtener_sufijos(texto)
#  for sufijo in sufijos:
#    if es_palindromo(sufijo):
#      contador += 1
#  return contador      

#def obtener_sufijos(t: str) -> list[str]:
#  sufijos: list[str] = []
#  palabra: str = t 
#  sufijo: str = ''
#  for i in range(len(palabra)-1, -1, -1):
#    sufijo = palabra[i] + sufijo
#    sufijos.append(sufijo)
#  return sufijos 

# 4
def quien_gano_el_tateti_facilito(tablero: list[list[chr]]) -> int:
  cuadrado: list[list[chr]] = transponer(tablero)
  
  if tateti(cuadrado, "X") and tateti(cuadrado, "O"):
    return 3
  elif tateti(cuadrado, "X"):
    return 1
  elif tateti(cuadrado, "O"):
    return 2
  else:
    return 0

def tateti(m: list[list[chr]], ficha: str) -> bool:
  contador: int = 0
  for fila in m:
    for cuadrado in fila:
      if cuadrado == ficha:       
        contador += 1
        if contador == 3:
          return True
      else:
        contador = 0    
    contador = 0        
  return False 

def transponer(tablero: list[list[str]]) -> list[list[chr]]:
  res: list[list[str]] = []
  columna: list[str] = []
  for i in range(len(tablero)):
    for fila in tablero:
      columna.append(fila[i])
    res.append(columna)
    columna = []    
  return res  
 