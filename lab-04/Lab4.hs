module Lab4 where

import Text.Read (readMaybe)

-- Task 1. Recursion and Fibonacci numbers
factorial :: Integer -> Integer
factorial n
  | n < 0     = error "factorial: n must be >= 0"
  | n == 0    = 1
  | otherwise = n * factorial (n - 1)

fib :: Integer -> Integer
fib n
  | n < 0     = error "fib: n must be >= 0"
  | n == 0    = 0
  | n == 1    = 1
  | otherwise = fib (n - 1) + fib (n - 2)

fibFast :: Integer -> Integer
fibFast n
  | n < 0     = error "fibFast: n must be >= 0"
  | otherwise = go n 0 1
  where
    go 0 a _ = a
    go k a b = go (k - 1) b (a + b)

fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

-- Task 2. Lazy lists
sumEvenSquares :: Int -> Integer
sumEvenSquares n
  | n <= 0    = 0
  | otherwise = sum (take n (map (^ (2 :: Int)) (filter even [1..])))

takeWhileRec :: (a -> Bool) -> [a] -> [a]
takeWhileRec _ [] = []
takeWhileRec p (x:xs)
  | p x       = x : takeWhileRec p xs
  | otherwise = []

primes :: [Integer]
primes = sieve [2..]
  where
    sieve [] = []
    sieve (p:xs) = p : sieve [x | x <- xs, x `mod` p /= 0]

firstNPrimes :: Int -> [Integer]
firstNPrimes n = take (max 0 n) primes

-- Task 3. RPN calculator (option A)
-- Extra operations: sqrt and neg.
evalRPN :: [String] -> Maybe Double
evalRPN = go []
  where
    go :: [Double] -> [String] -> Maybe Double
    go [x] [] = Just x
    go _ [] = Nothing
    go stack (t:ts) =
      case t of
        "+"    -> binary (+)
        "-"    -> binary (-)
        "*"    -> binary (*)
        "/"    -> case stack of
                    (y:x:rest) | y /= 0 -> go (x / y : rest) ts
                    _ -> Nothing
        "sqrt" -> case stack of
                    (x:rest) | x >= 0 -> go (sqrt x : rest) ts
                    _ -> Nothing
        "neg"  -> case stack of
                    (x:rest) -> go (negate x : rest) ts
                    _ -> Nothing
        _      -> case readMaybe t of
                    Just x  -> go (x : stack) ts
                    Nothing -> Nothing
      where
        binary op = case stack of
          (y:x:rest) -> go (op x y : rest) ts
          _          -> Nothing

evalRPNString :: String -> Maybe Double
evalRPNString = evalRPN . words
