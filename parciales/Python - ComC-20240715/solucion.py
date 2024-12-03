from typing import TypeVar
T = TypeVar('T')

# Ejercicio 1
def promedio_de_salidas(registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]:
  res: dict[str, tuple[int, float]] = {}

  for integrante in registro.keys():
    salidas: int = 0
    promedio: float = 0.0
    for i in range(len(registro[integrante])):
      if 0 < registro[integrante][i] < 61:
        salidas += 1
        promedio += registro[integrante][i]
    if salidas > 0:
      promedio = promedio / salidas
    res[integrante] = (salidas, promedio) 

  return res 

# Ejercicio 2
def tiempo_mas_rapido (tiempos_salas: list[int])-> int:
  mejor_tiempo: int = 60
  indice: int = 0

  for i in range(len(tiempos_salas)):
    if (0 < tiempos_salas[i] < 61) and tiempos_salas[i] < mejor_tiempo:
      mejor_tiempo = tiempos_salas[i]
      indice = i 
  
  return indice 

# Ejercicio 3
def racha_mas_larga (tiempos: list[int])-> tuple[int, int]:
  inicio: int = 0
  inicio_actual = 0
  final: int = 0
  racha: int = 0
  racha_actual: int = 0

  for i in range(len(tiempos)):
    if tiempos[i] == 0 or tiempos[i] == 61:
      if racha_actual > racha:
        final = i - 1
        inicio = inicio_actual 
        racha = racha_actual 
      inicio_actual = i + 1
      racha_actual = 0
    else:
      racha_actual += 1

  if racha_actual > racha:
    final = i
    inicio = inicio_actual  

  return (inicio, final)

# Ejercicio 4
def escape_en_solitario (amigos_por_salas: list[list[int]])-> list[int]:
  res: list[int] = []
  indice: int = 0
  
  for sala in amigos_por_salas:
    if sala[0] == 0 and sala[1] == 0 and sala[3] == 0 and sala[2] != 0:
      res.append(indice)
    indice += 1
  
  return res 