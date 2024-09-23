-- Ejercicio 1
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}

{-# HLINT ignore "Redundant bracket" #-}
{-# HLINT ignore "Eta reduce" #-}
fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)

-- Ejercicio 2
parteEntera :: Float -> Integer
parteEntera x
  | x >= 0 && x < 1 = 0
  | otherwise = parteEntera (x - 1) + 1

-- Ejercicio 3
esDivisible :: Integer -> Integer -> Bool
esDivisible x y
  | x < y = False
  | x == y = True
  | otherwise = esDivisible (x - y) y

-- Ejercicio 4
sumaImpares :: Integer -> Integer
sumaImpares 1 = 1
sumaImpares n = sumaImpares (n - 1) + 2 * n - 1

-- Ejercicio 5
medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n = medioFact (n - 2) * n

-- Ejercicio 6
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n
  | n < 10 = True
  | otherwise = ultimoDigito n == ultimoDigito (sacarUltimoDigito n) && todosDigitosIguales (sacarUltimoDigito n)

ultimoDigito :: Integer -> Integer
ultimoDigito x = mod x 10

sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito x = div x 10

-- Ejercicio 7
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i = mod (div n (10 ^ ((cantDigitos n) - i))) 10

cantDigitos :: Integer -> Integer
cantDigitos n
  | n < 10 = 1
  | otherwise = cantDigitos (div n 10) + 1

-- Ejercicio 8
sumaDigitos :: Integer -> Integer
sumaDigitos n
  | n < 10 = n
  | otherwise = sumaDigitos (sacarUltimoDigito n) + ultimoDigito n

-- Ejercicio 9
esCapicua :: Integer -> Bool
esCapicua n
  | n < 10 = True
  | iesimoDigito n 1 == iesimoDigito n (cantDigitos n) = esCapicua (numDeAdentro n)
  | otherwise = False 

numDeAdentro :: Integer -> Integer
numDeAdentro n = div (mod n (10 ^ ((cantDigitos n) - 1))) 10

-- Ejercicio 10
f1 :: Integer -> Integer 
f1 0 = 1
f1 n = 2^n + f1 (n-1) 

f2 :: Integer -> Float -> Float 
f2 1 q = q 
f2 n q = q^n + f2 (n-1) q

f3 :: Integer -> Float -> Float 
f3 n q = f2 (2*n) q 

-- Ejercicio 11
eAprox :: Integer -> Float 
eAprox 0 = 1
eAprox n = eAprox (n-1) + 1/fromIntegral((factorial n))

factorial :: Integer -> Integer 
factorial 0 = 1
factorial n = factorial (n-1) * n 

-- Ejercicio 12
