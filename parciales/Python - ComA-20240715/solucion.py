from queue import Queue as Cola

#1
def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
  res: Cola[int] = Cola()
  c_urgentes: Cola[int] = copiar_cola(urgentes)
  c_postergables: Cola[int] = copiar_cola(postergables)

  while not c_urgentes.empty():
    res.put(c_urgentes.get())
    while not c_postergables.empty():
      res.put(c_postergables.get())
      break 

  return res

def copiar_cola(c: Cola[int]) -> Cola[int]:
  copia: Cola[int] = Cola()
  res: Cola[int] = Cola()
  while not c.empty():
    elem = c.get()
    copia.put(elem)
    res.put(elem)
  while not copia.empty():
    c.put(copia.get())
  return res 

#2
def alarma_epidemiologica(registros: list[tuple[int, str]], infecciosas: list[str], umbral: float) -> dict[str, float]:
  cant_por_infecciosas: dict[str,int] = {}
  res: dict[str,float] = {}
  cant_registro: int = len(registros)

  for paciente in registros:
    if paciente[1] in infecciosas:
      if paciente[1] in cant_por_infecciosas.keys():
        cant_por_infecciosas[paciente[1]] += 1
      else:
        cant_por_infecciosas[paciente[1]] = 1
      
  for registro in cant_por_infecciosas.keys():
    porcentaje: int = cant_por_infecciosas[registro] / cant_registro
    if porcentaje > umbral:
      res[registro] = porcentaje    

  return res 


#3
def empleados_del_mes(horas: dict[int, list[int]]) -> list[int]:
  return 0

#4
def nivel_de_ocupacion(pisos: list[list[bool]]) -> list[float]:
  return 0
