-- Practica 3

-- Ejercicio 1
-- a)
f :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16

-- b)
g :: Integer -> Integer
g 8 = 16
g 16 = 4
g 131 = 1

-- c)
h :: Integer -> Integer
h n = f (g (n))

k :: Integer -> Integer
k n = g (f n)

-- Ejercicio 2
-- a)
absoluto :: Integer -> Integer
absoluto x
  | x >= 0 = x
  | otherwise = -x

-- b)
maximoabsoluto :: Integer -> Integer -> Integer
maximoabsoluto x y
  | abs x > abs y = abs x
  | abs x < abs y = abs y
  | otherwise = 404

-- c)
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z
  | x >= y && x >= z = x
  | y >= x && y >= z = y
  | otherwise = z

-- d)
algunoEs0 :: Float -> Float -> Bool
algunoEs0 x 0 = True
algunoEs0 0 y = True
algunoEs0 x y = False

-- e)
ambosSon0 :: (Float, Float) -> Bool
ambosSon0 (0, 0) = True
ambosSon0 (x, y) = False

-- f)
mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y
  | x <= 3 && y <= 3 = True
  | x > 3 && x <= 7 && y > 3 && y <= 7 = True
  | x > 7 && y > 7 = True
  | otherwise = False

-- g)
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z
  | x /= y && x /= z && y /= z = x + y + z
  | x == y && x /= z = x + z
  | x /= y && x == z = x + y
  | y == z && y /= x = y + x
  | otherwise = 0

-- h)
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y
  | mod x y == 0 = True
  | otherwise = False

-- i)
digitoUnidades :: Integer -> Integer
digitoUnidades x = mod (abs x) 10

-- j)
digitoDecenas :: Integer -> Integer
digitoDecenas x = digitoUnidades (div x 10)

-- Ejercicio 3
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b
  | mod a b == 0 = True
  | otherwise = False

-- Ejercicio 4
-- a)
prodInt :: (Float, Float) -> (Float, Float) -> Float
prodInt (x1, y1) (x2, y2) = x1 * x2 + y1 * y2

-- b)
todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor (x1, y1) (x2, y2)
  | x1 < x2 && y1 < y2 = True
  | otherwise = False

-- c)
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (x1, y1) (x2, y2) = sqrt ((x1 - x2) ^ 2 + (y1 - y2) ^ 2)

-- d)
sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (x, y, z) = x + y + z

-- e)
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (x, y, z) n
  | mod x n == 0 && mod y n == 0 && mod z n == 0 = x + y + z
  | mod x n /= 0 && mod y n == 0 && mod z n == 0 = y + z
  | mod x n == 0 && mod y n /= 0 && mod z n == 0 = x + z
  | mod x n == 0 && mod y n == 0 && mod z n /= 0 = x + y
  | mod x n == 0 = x
  | mod y n == 0 = y
  | mod z n == 0 = z
  | otherwise = 0

-- f)
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (x, y, z)
  | mod x 2 == 0 = 0
  | mod y 2 == 0 = 1
  | mod z 2 == 0 = 2
  | otherwise = 4

-- Ejercicio 5
todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (x, y, z) = f1 (x) > g1 (x) && f1 (y) > g1 (y) && f1 (z) > g1 (z)

f1 :: Integer -> Integer
f1 n
  | n <= 7 = n ^ 2
  | n > 7 = 2 * n - 1

g1 :: Integer -> Integer
g1 n
  | mod n 2 == 0 = div n 2
  | otherwise = 3 * n + 1

-- Ejercicio 6
bisiesto :: Integer -> Bool
bisiesto n = not ((mod n 4 /= 0) || (mod n 100 == 0 && mod n 400 /= 0))

-- Ejercicio 7
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (x1, x2, x3) (y1, y2, y3) = abs (x1 - y1) + abs (x2 - y2) + abs (x3 - y3)

-- Ejercicio 8
comparar :: Integer -> Integer -> Integer
comparar a b
  | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
  | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
  | sumaUltimosDosDigitos a == sumaUltimosDosDigitos b = 0

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = mod (abs x) 10 + mod (div (abs x) 10) 10