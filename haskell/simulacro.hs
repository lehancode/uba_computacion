-- Ejercicio 1
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas (x:xs) = esRepetida (x:xs) && relacionesValidas xs

esRepetida :: [(String, String)] -> Bool
esRepetida [] = True
esRepetida [(x,y)]
  | x == y = False
  | otherwise = True
esRepetida ((x,y):(z,w):xs)
  | (x,y) == (z,w) || (x,y) == (w,z) = False
  | otherwise = esRepetida ((x,y):xs)

-- Ejercicio 2
personas :: [(String, String)] -> [String]
personas [] = []
personas ((x,y):xs) = quitarElementos (x : y : personas xs)

quitarElementos :: (Eq t) => [t] -> [t]
quitarElementos [] = [] 
quitarElementos (x:xs) = x : quitarElementos (filtrar x xs)

filtrar :: (Eq t) => t -> [t] -> [t]
filtrar a [] = []
filtrar a (b:xs)
  | a == b = filtrar a xs 
  | otherwise = b : filtrar a xs

-- Ejercicio 3
-- devuelve lista de elementos que tiene la cantidad de personas con la que se relaciona persona
amigosDe :: String -> [(String, String)] -> [String]
amigosDe persona [] = []




{- INTENTO EN CLASE EJ 2, CHOCLITO!
personas :: [(String, String)] -> [String]
personas [] = []
personas ((x,y):xs) = quitarPersonas (agregarPersonas ((x,y):xs))

quitarPersonas :: [String] -> [String]
quitarPersonas [] = []
quitarPersonas [x] = [x]
quitarPersonas (x:xs)
  | not(esPersonaRepetida (x:xs)) = quitarPersonas (tail (x:xs))
  | otherwise = x : quitarPersonas (tail (x:xs))

agregarPersonas :: [(String, String)] -> [String]
agregarPersonas [] = []
agregarPersonas ((x,y):xs) = x : y : agregarPersonas xs

esPersonaRepetida :: [String] -> Bool
esPersonaRepetida [] = True
esPersonaRepetida [x] = True
esPersonaRepetida (x:y:xs)
  | x == y = False
  | otherwise = esPersonaRepetida (x:xs)
-}