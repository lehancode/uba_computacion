{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Redundant bracket" #-}
{-# HLINT ignore "Use foldr" #-}
type Productos = [String] 

-- Ej 1
-- ["banana", "pera", "banana", "manzana"]
generarStock :: [String] -> [(String, Int)]
generarStock [] = []
generarStock (x:xs) = añadirProducto x (generarStock xs)

añadirProducto :: String -> [(String, Int)] -> [(String, Int)]
añadirProducto p [] = [(p,1)]
añadirProducto p ((prod,cant):xs)
  | p == prod = ((prod,cant+1):xs)
  | otherwise = ((prod,cant):(añadirProducto p xs)) 
  
-- Ej 2
stockDeProducto :: [(String,Int)] -> String -> Int 
stockDeProducto [] producto = 0
stockDeProducto ((p,n):xs) producto
  | p == producto = n 
  | otherwise = stockDeProducto xs producto

-- Ej 3
dineroEnStock :: [(String, Int)] -> [(String,Float)] -> Float 
dineroEnStock [] _ = 0 
dineroEnStock ((p,n):xs) ps = (precioProducto ps p) * (fromIntegral n) + dineroEnStock xs ps 

precioProducto :: [(String, Float)] -> String -> Float
precioProducto ((p,precio):xs) prod
  | p == prod = precio 
  | otherwise = precioProducto xs prod 

-- Ej 4
-- si stockDeProducto (stock, precios[i]0) > 10 => res[i]0 = precios[i]0 y res[i]1 = precios[i]1 * 0,80
-- si stockDeProducto (stock, precios[i]0) <= 10 => res[i]0 = precios[i]0 y res[i]1 = precios[i]1
aplicarOferta :: [(String, Int)] -> [(String, Float)] -> [(String, Float)]
aplicarOferta _ [] = []
aplicarOferta xs ((prod,p):ss)
  | stockDeProducto xs prod > 10 = ((prod, p*0.80):aplicarOferta xs ss) 
  | stockDeProducto xs prod <= 10 = (prod,p):aplicarOferta xs ss