-- Ejercicio 2 
-- 5)
-- Guardas
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x xs
  | head xs == x = tail xs
  | otherwise = head xs : quitar x (tail xs)

-- Pattern Matching
quitarBis :: (Eq t) => t -> [t] -> [t]
quitarBis _ [] = []
quitarBis elem (x : xs)
  | x == elem = xs
  | otherwise = x : quitarBis elem xs

-- Ejercicio 3
-- 3)
-- Guardas
maximo :: (Ord s) => [s] -> s
maximo xs
  | tail xs == [] = head xs
  | head xs <= head (tail xs) = maximo (tail xs)
  | head xs >= head (tail xs) = maximo (head xs : (tail (tail xs)))

-- Pattern Matching
maximo1 :: (Ord s) => [s] -> s
maximo1 (x : []) = x
maximo1 (x : xs)
  | x >= head xs = maximo (x : (tail xs))
  | otherwise = maximo (tail xs)

-- Version hecha en clase
maximo2 :: (Ord s) => [s] -> s
maximo2 [x] = x
maximo2 (x : y : xs)
  | x >= y = maximo (x : xs)
  | otherwise = maximo (y : xs)

-- 9)
ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar xs = ordenar (quitar (maximo xs) xs) ++ [maximo xs]
