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
  horas_por_empleado: dict[int,list[int]] = {}
  res: list[int] = []

  for empleado in horas.keys():
    cantidad_horas: int = 0
    for hs in horas[empleado]:
      cantidad_horas += hs
    horas_por_empleado[empleado] = cantidad_horas

  horas_empleados: list[int] = list(horas_por_empleado.values())  
  horas_mejor_empleado: int = maximo(horas_empleados)
  for empleado in horas_por_empleado.keys():
    if horas_por_empleado[empleado] >= horas_mejor_empleado:
      res.append(empleado)
  return res      
    
def maximo(l: list[int]) -> int:
  res: int = 0
  for i in range(len(l)):
    if l[i] > res:
      res = l[i]
  return res    

#4
def nivel_de_ocupacion(pisos: list[list[bool]]) -> list[float]:
  ocupacion: list[float] = []
  camas_por_piso: int = len(pisos[0])
  for piso in pisos:
    contador: int = 0
    for cama in piso:
      if cama == True:
        contador += 1
    ocupacion.append(contador / camas_por_piso)
  return ocupacion 