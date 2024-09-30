-- Ej 1
aproboMasDeNMaterias :: [(String, [Int])] -> String -> Int -> Bool
aproboMasDeNMaterias ((nombre, notas) : xs) alumno n
  | nombre == alumno = cantidadMateriasAprobadas notas > n
  | otherwise = aproboMasDeNMaterias xs alumno n

cantidadMateriasAprobadas :: [Int] -> Int
cantidadMateriasAprobadas [] = 0
cantidadMateriasAprobadas (x : xs)
  | x >= 4 = 1 + cantidadMateriasAprobadas xs
  | otherwise = cantidadMateriasAprobadas xs

-- Ej 2
buenosAlumnos :: [(String, [Int])] -> [String]
buenosAlumnos [] = []
buenosAlumnos ((nombre, notas) : xs)
  | promedio notas >= 8 && noTieneAplazos notas = nombre : buenosAlumnos xs
  | otherwise = buenosAlumnos xs

promedio :: [Int] -> Float
promedio [] = 0
promedio (x : xs) = fromIntegral (sumaNotas (x : xs)) / fromIntegral (longitud (x : xs))

sumaNotas :: [Int] -> Int
sumaNotas [] = 0
sumaNotas (x : xs) = x + sumaNotas xs

longitud :: [Int] -> Int
longitud [] = 0
longitud (x : xs) = 1 + longitud xs

noTieneAplazos :: [Int] -> Bool
noTieneAplazos [] = True
noTieneAplazos (x : xs)
  | x >= 4 = noTieneAplazos xs
  | otherwise = False

-- Ej 3-
mejorPromedio :: [(String, [Int])] -> String
mejorPromedio n = mayorPromedio (promedios n) (alumnos n)

alumnos :: [(String, [Int])] -> [String]
alumnos [] = []
alumnos ((nombre, _) : xs) = nombre : alumnos xs

promedios :: [(String, [Int])] -> [Float]
promedios [] = []
promedios ((_, notas) : xs) = promedio notas : promedios xs

mayorPromedio :: [Float] -> [String] -> String
mayorPromedio [_] [nombre] = nombre
mayorPromedio (nota1 : nota2 : notas) (nombre1 : nombre2 : nombres)
  | nota1 >= nota2 = mayorPromedio (nota1 : notas) (nombre1 : nombres)
  | otherwise = mayorPromedio (nota2 : notas) (nombre2 : nombres)

-- Ejercicio 4
seGraduoConHonores :: [(String, [Int])] -> Int -> String -> Bool
seGraduoConHonores registro n alumno =
  aproboMasDeNMaterias registro alumno (n - 1)
    && pertenece alumno (buenosAlumnos registro)
    && diferenciaPromedio registro alumno

pertenece :: String -> [String] -> Bool
pertenece _ [] = False
pertenece alumno (x : xs) = alumno == x || pertenece alumno xs

diferenciaPromedio :: [(String, [Int])] -> String -> Bool
diferenciaPromedio registro alumno = ((promedioAVer - 1) < promedioMejorAlumno) && (promedioMejorAlumno < (promedioAVer + 1))
  where
    promedioAVer = promedioAlumno alumno registro
    promedioMejorAlumno = promedioAlumno (mejorPromedio registro) registro

promedioAlumno :: String -> [(String, [Int])] -> Float
promedioAlumno nombre ((nombre1, notas) : xs)
  | nombre1 == nombre = promedio notas
  | otherwise = promedioAlumno nombre xs
