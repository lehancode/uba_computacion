from queue import LifoQueue as pila
from queue import Queue as Cola
import random

# Ejercicio 1
# 1)
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> pila[int]:
  p: pila = pila()
  for i in range(cantidad):
    n: int = random.randint(desde,hasta)
    p.put(n)
  return p 

#p = generar_nros_al_azar(10,1,30)
#print(p.queue) 

# 2)
def cantidad_elementos(p: pila) -> int:
  p2: pila = pila()
  cantidad: int = 0
  while not(p.empty()):
    elem = p.get()
    p2.put(elem)
    cantidad += 1
  while not(p2.empty()):
    elem = p2.get()
    p.put(elem)
  return cantidad 

#p = generar_nros_al_azar(4,1,5)
#print(p.queue)
#print(cantidad_elementos(p))
#print(p.queue)

# 3)
def buscar_el_maximo(p: pila[int]) -> int:
  maximo: int = 0
  backup: pila[int] = pila()
  while not(p.empty()):
    elem: int = p.get()
    backup.put(elem)
    if elem > maximo:
      maximo = elem 
  while not(backup.empty()):
    elem: int = backup.get()
    p.put(elem)
  return maximo

#p = generar_nros_al_azar(4,1,100)
#print(p.queue)
#print(buscar_el_maximo(p))
#print(p.queue)

# 4)
def buscar_nota_maxima(p: pila[tuple[str,int]]) -> tuple[str,int]:
  p2: pila[tuple[str,int]] = pila()
  nota_maxima: tuple[str,int] = ("a", 0)
  while not(p.empty()):
    elem: tuple[str,int] = p.get()
    p2.put(elem)
    if elem[1] > nota_maxima[1]:
      nota_maxima = elem 
  while not(p2.empty()):
    elem: tuple[str,int] = p2.get()
    p.put(elem)
  return nota_maxima

'''p = pila()
p.put(("a", 5))
p.put(("b", 10))
p.put(("c", 3))
print(p.queue)
print(buscar_nota_maxima(p))
print(p.queue)'''

# 5)
def esta_bien_balanceada(s: str) -> bool:
  balance: int = 0
  for c in s:
    if c == '(':
      balance += 1
    elif c == ')':
      balance -= 1
    elif balance < 0:
      return False
  if balance != 0:
    return False 
  else:
    return True

# 6)
def evaluar_expresion(s: str) -> float:
  p: pila[chr] = pila()
  for c in s:
    if c == ' ':
      continue 
    if c == '+':
      primero = int(p.get())
      segundo = int(p.get())
      p.put(primero+segundo)
    elif c == '-':
      primero = int(p.get())
      segundo = int(p.get())
      p.put(primero-segundo)
    elif c == '*':
      primero = int(p.get())
      segundo = int(p.get())
      p.put(primero*segundo)
    elif c == '/':
      primero = int(p.get())
      segundo = int(p.get())
      p.put(primero/segundo)
    else:
      p.put(int(c))
  res: float = p.get()
  return res

#print(evaluar_expresion("3 4 + 5 * 2 -"))  

#7)
def intercalar(p1: pila, p2: pila) -> pila:
    nueva_pila: pila = pila()
    while not(p2.empty()):
        nueva_pila.put(p2.get())
        while not(p1.empty()):
            nueva_pila.put(p1.get())
            break 
    intercalado: pila = pila()
    while not(nueva_pila.empty()):
        elem = nueva_pila.get()
        intercalado.put(elem)
    return intercalado

p1 = pila()
p1.put(2)
p1.put(3)
p1.put(5)
p1.put(10)

p2 = pila()
p2.put(4)
p2.put(8)
p2.put(6)
p2.put(11)

#prueba = intercalar(p1, p2)
#print(prueba.queue)

# Ejercicio 2
# 8)
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
  cola_numeros: Cola[int] = Cola()
  for i in range(cantidad):
    num: int = random.randint(desde, hasta)
    cola_numeros.put(num)
  return cola_numeros 

# 9)
def cantidad_elementos2(c: Cola) -> int:
  copia: Cola = Cola()
  cantidad: int = 0
  while not(c.empty()):
    copia.put(c.get())
    cantidad += 1
  while not(copia.empty()):
    c.put(copia.get())
  return cantidad

cola2 = Cola()
cola2.put(1)
cola2.put(5)
cola2.put(103)
cola2.put(57)

b = cantidad_elementos2(cola2)
#print(b)
#print(cola2.queue)

# 10)
def buscar_el_maximo(c: Cola[int]) -> int:
  copia: Cola[int] = Cola()
  maximo: int = 0
  while not (c.empty()):
    n: int = c.get()
    if n > maximo:
       maximo = n 
    copia.put(n)
  while not(copia.empty()):
    c.put(copia.get())
  return maximo 

a = Cola()
a.put(1)
a.put(2)
a.put(3)
a.put(4)

#print(buscar_el_maximo(a))
#print(a.queue

# 11)
def buscar_nota_minima(c: Cola[tuple[str,int]]) -> tuple[str,int]:
  copia: Cola[tuple[str,int]] = Cola()
  res: tuple[str,int] = c.get()
  copia.put(res)

  while not(c.empty()):
    n: tuple[str,int] = c.get()
    if n[1] < res[1]:
      res = n
    copia.put(n)

  while not(copia.empty()):
    c.put(copia.get())

  return res 

a = Cola()
a.put(("a", 5))
a.put(("b", 2))
a.put(("c", 1))
a.put(("d", 10))

#print(buscar_nota_minima(a))
#print(a.queue)

# 12)
def intercalar(c1: Cola, c2: Cola) -> Cola:
  res: Cola = Cola()

  while not c1.empty():
    res.put(c1.get())
    while not c2.empty():
      res.put(c2.get())
      break
  
  return res

z = Cola()
z.put(0)
z.put(3)
z.put(2)
z.put(5)

x = Cola()
x.put(15)
x.put(42)
x.put(30)
x.put(-5)

# print(intercalar(z,x).queue)

# 13)
def armar_secuencia_de_bingo() -> Cola[int]:
  res: Cola = Cola()
  lista: list[int] = list(range(0,99))
  random.shuffle(lista)

  for i in range(0,99):
    res.put(lista[i])

  return res 

def crear_carton() -> list[int]:
  carton: list[int] = []
  lista: list[int] = list(range(0,99))
  random.shuffle(lista)

  for i in range(0,12):
    carton.append(lista[i])

  return carton

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
  cant_jugadas: int = 0
  copia_bolillero: Cola[int] = Cola()
  jugadas_por_marcar: int = len(carton)

  print(bolillero.queue)
  print(carton)
  while not bolillero.empty():
    copia_bolillero.put(bolillero.get())
  
  while jugadas_por_marcar != 0:
    num: int = copia_bolillero.get()
    if num in carton:
      cant_jugadas += 1
      jugadas_por_marcar -= 1
      bolillero.put(num)
    else:
      cant_jugadas += 1
      bolillero.put(num)

  print(cant_jugadas)    
  return cant_jugadas

#jugar_carton_de_bingo(crear_carton(), armar_secuencia_de_bingo())

# 14)
def n_pacientes_urgentes(c: Cola[tuple[int,str,str]]) -> int:
  copia: Cola[tuple[int,str,str]] = Cola()
  pacientes_prioridad: int = 0

  while not c.empty():
    paciente = c.get()
    copia.put(paciente)
    if 1 <= paciente[0] <= 3:
      pacientes_prioridad += 1
  
  while not copia.empty():
    c.put(copia.get())
  
  return pacientes_prioridad


c: Cola = Cola()
c.put([9, "a", "ad"])
c.put([10, "b", "bd"])
c.put([2, "c", "cd"])
c.put([1, "d", "d"])
c.put([3, "e", "ed"])
c.put([5, "f", "fd"])
#print(c.queue)
#print(n_pacientes_urgentes(c))
#print(c.queue)

# 15)
def atencion_a_clientes(c: Cola[tuple[str,int,bool,bool]]) -> Cola[tuple[str,int,bool,bool]]:
  copia: Cola[tuple[str,int,bool,bool]] = Cola()  # de aca restauramos c
  copia_aux: Cola[tuple[str,int,bool,bool]] = Cola() # de aca clasificamos
  res: Cola[tuple[str,int,bool,bool]] = Cola() # resultado ordenado
  clientes_prioridad: Cola[tuple[str,int,bool,bool]]  = Cola()
  clientes_preferenciales: Cola[tuple[str,int,bool,bool]]  = Cola()
  clientes_sin_prioridad: Cola[tuple[str,int,bool,bool]]  = Cola()

  while not c.empty():
    cliente = c.get()
    copia.put(cliente)
    copia_aux.put(cliente)

  while not copia_aux.empty():
    cliente = copia_aux.get()
    if cliente[3] == True:
      clientes_prioridad.put(cliente)
    elif cliente[2] == True:
      clientes_preferenciales.put(cliente)
    else:
      clientes_sin_prioridad.put(cliente)

  while not clientes_prioridad.empty():
    res.put(clientes_prioridad.get())
  
  while not clientes_preferenciales.empty():
    res.put(clientes_preferenciales.get())

  while not clientes_sin_prioridad.empty():
    res.put(clientes_sin_prioridad.get())

  while not copia.empty():
    c.put(copia.get())    

  return res.queue

# Ejercicio 3
# 16)
def obtener_palabras(texto: str) -> list[str]:
  palabras: list[str] = []
  palabra_actual: str = ''

  for letra in texto:
    if letra == ' ' or letra == '\n':
      if letra != '':
        palabras.append(palabra_actual)
        palabra_actual = ''
    else:
      palabra_actual += letra
  if palabra_actual != '':
    palabras.append(palabra_actual)

  return palabras
        
def agrupar_por_longitud(nombre_archivo: str) -> dict:
  archivo = open(nombre_archivo, 'r')
  palabras: list[str] = obtener_palabras(archivo.read())
  archivo.close()
  res: dict[int,int] = {}

  for palabra in palabras:
    longitud = len(palabra)
    if longitud != 0:
      if longitud not in res.keys():
        res[longitud] = 1
      else:
        res[longitud] += 1

  return res 

#print(agrupar_por_longitud("texto.txt"))

# 17)
#[("juan", 4), ("maria", 10), ("juan", 10)]

def calcular_promedio_por_estudiante(notas: list[tuple[str, float]]) -> dict[str,float]:
  promedios: dict[str,float] = {}
  cantidad_notas: dict[str,float] = {}

  for estudiante in notas:
    if estudiante[0] not in promedios.keys():
      promedios[estudiante[0]] = estudiante[1]
      cantidad_notas[estudiante[0]] = 1
    else:
      promedios[estudiante[0]] +=  estudiante[1]
      cantidad_notas[estudiante[0]] += 1

  for notas in cantidad_notas:
    promedios[notas] /= cantidad_notas[notas]

  return promedios

#print(calcular_promedio_por_estudiante([("juan", 6.3), ("maria", 10), ("juan", 10)]))

# 18)
def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
  archivo = open(nombre_archivo, "r")
  palabras: list[str] = obtener_palabras(archivo.read())
  archivo.close()
  apariciones_palabras: dict[str, int] = {}
  mas_frecuente: str = ''
  apariciones: int = 0

  for palabra in palabras: # cuento palabras
    if palabra not in apariciones_palabras.keys():
      apariciones_palabras[palabra] = 1
    else:
      apariciones_palabras[palabra] += 1

  for palabra in apariciones_palabras: # veo cual es la que mas veces aparece
    if apariciones_palabras[palabra] > apariciones:
      apariciones = apariciones_palabras[palabra]
      mas_frecuente = palabra 

  return mas_frecuente

#print(la_palabra_mas_frecuente("texto.txt"))

# 19)
historiales: dict[str,pila[str]] = {}

def visitar_sitio(historiales: dict[str, pila[str]], usuario: str, sitio: str) -> None:
  if usuario not in historiales.keys():
    historiales[usuario] = pila() 
  historiales[usuario].put(sitio)

def navegar_atras(historiales: dict[str,pila[str]], usuario: str) -> None:
  if usuario in historiales.keys():
    historial: pila = historiales[usuario]
    if not historial.empty():
      sitio_actual = historial.get()
      sitio_anterior = historial.get()
      historial.put(sitio_actual)
      historial.put(sitio_anterior)

visitar_sitio(historiales, "martin", "facebook.com")
visitar_sitio(historiales, "franco", "instagram.com")
visitar_sitio(historiales, "franco", "youtube.com")
visitar_sitio(historiales, "martin", "pinterest.com")
#(historiales)
#print("franco: ", historiales["franco"].queue)
#print("martin: ", historiales["martin"].queue)

navegar_atras(historiales, "martin")
#print("hacia atras <--")
#print("martin: ", historiales["martin"].queue)

visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario1", "facebook.com")
#print("1: ", historiales["Usuario1"].queue)
navegar_atras(historiales, "Usuario1")
visitar_sitio(historiales, "Usuario2", "youtube.com")

#print("1: ", historiales["Usuario1"].queue)
#print("2: ", historiales["Usuario2"].queue)

# 20)
inventario: dict[str,dict[str,float|int]] = {} #{"Nombre": {"Precio": precio, "Cantidad": cantidad}}

def agregar_producto(inventario: dict[str,dict[str,float|int]], nombre: str, precio: float, cantidad: int) -> None:
  inventario[nombre] = {"Precio": precio, "Cantidad": cantidad}

#agregar_producto(inventario, "Bermuda", 15313.25, 16)
#agregar_producto(inventario, "Pantalon", 35000, 10)
#print(inventario)

def actualizar_stock(inventario: dict[str,dict[str,float|int]], nombre: str, cantidad: int) -> None:
  inventario[nombre]['Cantidad'] += cantidad

#actualizar_stock(inventario, "Bermuda", 5)
#actualizar_stock(inventario, "Pantalon", 10)
#print(inventario)

def actualizar_precios(inventario: dict[str,dict[str,float|int]], nombre: str, precio: float) -> None:
  inventario[nombre]["Precio"] = precio

#actualizar_precios(inventario, "Bermuda", 1000)
#actualizar_precios(inventario, "Pantalon", 550)
#print(inventario)

def calcular_valor_inventario(inventario: dict[str,dict[str,float|int]]) -> float:
  valor_inventario: float = 0
  for producto in inventario.values():
    valor_inventario += producto["Precio"] * producto["Cantidad"]
  return valor_inventario


agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalon", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
valor_total = calcular_valor_inventario(inventario)
#print("Valor total del inventario:", valor_total) # Deberia imprimir 2100.0
#print(calcular_valor_inventario(inventario))
#print(inventario)

# Ejercicio 4 ARCHIVOS
# 21) 
# 1)
def contar_lineas(nombre_archivo: str) -> int:
  archivo = open(nombre_archivo, 'r')
  lineas: list[str] = archivo.readlines()
  archivo.close()
  return len(lineas)

#print(contar_lineas("texto.txt"))

# 2)
def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
  archivo = open(nombre_archivo, 'r')
  palabras: list[str] = obtener_palabras(archivo.read())
  archivo.close()
  print(palabras)
  for elem in palabras:
    if elem == palabra:
      return True
  return False

#print(existe_palabra("shortcuts", "texto.txt"))

# 3)
def cantidad_apariciones(nombre_archivo: str, palabra: str) -> int:
  archivo = open(nombre_archivo, 'r')
  palabras: list[str] = obtener_palabras(archivo.read())
  archivo.close()
  res: int = 0
  for elem in palabras:
    if elem == palabra:
      res += 1
  return res

#print(cantidad_apariciones("texto.txt", "I"))

# 22)
def tiene_comentarios(linea: str) -> bool:
  indice: int = 0
  while linea[indice] == ' ' and indice < (len(linea)-1):
    indice += 1
  return linea[indice] == '#'
        

#print(es_comentario("#    esto es comentario"))
#print(es_comentario("#hola"))
#print(es_comentario("    hola"))
#print(es_comentario("hola #esto no"))
#print(es_comentario("           "))

def clonar_sin_comentarios(nombre_archivo: str) -> None:
  archivo = open(nombre_archivo, 'r')
  comentado: list[str] = archivo.readlines()
  archivo.close()
  sin_comentarios = open("nuevo_archivo.txt", 'w')
  for linea in comentado:
    if not(tiene_comentarios(linea)):
      sin_comentarios.write(linea)
  sin_comentarios.close()

#clonar_sin_comentarios("archivos.txt")

# 23)
def invertir_lineas(nombre_archivo: str) -> None:
  archivo = open(nombre_archivo, 'r')
  original: list[str] = archivo.readlines()
  archivo.close()
  invertido = open("invertido.txt", 'w')
  for i in range(len(original)-1, -1, -1):
    if i == (len(original) - 1):                  # no se porque si no hago esto me escribe la primer y segunda linea seguido, despues las demas bien..
      invertido.writelines(original[i] + "\n") 
      continue
    invertido.writelines(original[i]) 
  invertido.close()

#invertir_lineas("archivos.txt")

# 24)
def agregar_frase_al_final(nombre_archivo: str, frase: str) -> None:
  archivo = open(nombre_archivo, 'r')
  contenido: str = archivo.read()
  archivo = open(nombre_archivo, 'w')
  archivo.write(contenido)
  archivo.write('\n' + frase)
  archivo.close()

#agregar_frase_al_final("archivos.txt", "compila?")

# 25)
def agregar_frase_al_principio(nombre_archivo: str, frase: str) -> None:
  archivo = open(nombre_archivo, 'r')
  contenido: list[str] = [frase + '\n'] + archivo.readlines()
  print(contenido)
  archivo = open(nombre_archivo, 'w')
  for linea in contenido:
    archivo.write(linea)
  archivo.close()

#agregar_frase_al_principio("archivos.txt", "iara iara")
