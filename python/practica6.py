import math as math

# tipado def funcion(numero: int) ->bool:

# Ejercicio 1
# 1)
def imprimir_hola_mundo () :
  print("Hola Mundo!")

# 2)
def imprimir_un_verso():
  print("Por el principio de induccion.. \nAbsurdo! \nNovio gansta")

# 3)
def raizDe2():
  print(round(math.sqrt(2), 4))

# 4)
def factorial_de_dos() -> None:
  print(2**1)

# 5)
def perimetro() -> None:
  return 2 * math.pi

# Ejercicio 2
# 1)
def imprimir_saludo (nombre: str) -> None:
  print("Hola,", nombre)

# 2)
def raiz_cuadrada_de(numero: int) -> int:
  return math.sqrt(numero)

# 3)
def fahrenheit_a_celsius(temp: float) -> float:
  temp: int = ((temp-32)*5) / 9

# 4)
def imprimir_dos_veces(estribillo: str) -> None:
  print(estribillo * 2)

# 5)
def es_multiplo_de(n: int, m: int) -> bool:
  return (n % m) == 0 

# 6)
def es_par(n: int) -> bool:
  return es_multiplo_de(n, 2) 

# 7)
def cantidad_de_pizzas(comensales: int, min_cant_porciones: int) -> int:
  return math.ceil((comensales * min_cant_porciones) / 8)

# Ejercicio 3
# 1)
def alguno_es_0(num1: float, num2: float) -> bool:
  return num1 == 0 or num2 == 0

# 2)
def ambos_son_0(num1: float, num2: float) -> bool:
  return num1 == 0 and num2 == 0

# 3)
def es_nombre_largo(nombre: str) -> bool:
  return len(nombre) >= 3 and len(nombre) <= 8

# 4)
def es_bisiesto(año: int) -> bool:
  return año % 400 == 0 or (año % 4 == 0 and not(año % 100 == 0))

# Ejercicio 4
def peso_pino(altura: float) -> float:
  peso: float = 0
  if altura <= 300:
    peso = altura * 3
  else:
    peso = 900 + (altura - 300) * 2
  return peso   

def es_peso_util(peso: float) -> bool: 
  return peso >= 400 and peso <= 1000

def sirve_pino(altura: float) -> bool:
  return es_peso_util(peso_pino(altura))

# Ejercicio 5
# 1)
def devolver_el_doble_si_es_par(numero: int) -> int:
  if numero % 2 == 0:
    return numero * 2
  else:
    return numero

# 2)
def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
  if es_par(numero):
    return numero
  else:
    return numero + 1

# 3)
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
  if numero % 3 == 0:
    return numero * 2
  elif numero % 9 == 0:
    return numero * 3
  return numero 

# 4)
def lindo_nombre(nombre: str) -> str:
  if len(nombre) >= 5:
    return "Tu nombre tiene muchas letras!"
  else:
    return "Tu nombre tiene menos de 5 caracteres"

# 5)
def elRango(numero: int) -> None:
  if numero < 5:
    print("Menor a 5")
  elif numero >= 10 and numero <= 20:
    print("Entre 10 y 20")
  else:
    print("Mayor a 20")  

# 6)
def trabajar_o_vacacionar(sexo: chr, edad: int) -> None:
  if (sexo == "F" and edad >= 60) or (sexo == "M" and edad >= 65) or (edad < 18):
    print("Andá de vacaciones")
  else:
    print("Te toca trabajar")

# Ejercicio 6
# 1)
def imprimir_al_10() -> None:
  num: int = 1
  while num <= 10:
    print(num)
    num += 1

# 2)
def imprimir_pares_10_al_40() -> None:
  num: int = 10
  while num <= 40:
    if num % 2 == 0:
      print(num)
    num += 1

# 3)
def imprimir_eco() -> None:
  contador: int = 0
  while contador < 10:
    print("eco")
    contador += 1

# 4)
def cuenta_regresiva(contador: int) -> None:
  while contador >= 1:
    print(contador)
    contador -= 1
  print("¡Despegue!")

# 5)
def viajar_en_tiempo(partida: int, llegada: int) -> None:
  while partida >= llegada:
    partida -= 1
    print("Viajo un año al pasado, estamos en el año:", partida)

# 6)
def viajar_hasta_aristoteles(partida: int) -> None:
  while partida > 384:
    partida -= 20
    print("Viajo 20 años al pasado, estamos en el año:", partida)
  if partida < 384:
    print("Estamos lo mas cercano posible al 384 a.C")

# Ejercicio 7
# Lo hago unicamente con el 6 ya que es masomenos lo mismo
def viajar_hasta_aristoteles2(año_partida: int) -> None:
  for num in range(año_partida, 384, -20):
    año_partida -= 20
    print("Viajo 20 años en el pasado, estamos en el año:", año_partida)