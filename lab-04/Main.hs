module Main where

import Lab4

check :: (Eq a, Show a) => String -> a -> a -> IO ()
check name expected actual =
  if expected == actual
    then putStrLn ("OK: " ++ name)
    else error ("FAIL: " ++ name ++
                "\n expected: " ++ show expected ++
                "\n actual:   " ++ show actual)

main :: IO ()
main = do
  putStrLn "=== TASK 1: recursion ==="
  check "factorial 0" 1 (factorial 0)
  check "factorial 1" 1 (factorial 1)
  check "factorial 5" 120 (factorial 5)
  check "factorial 7" 5040 (factorial 7)
  check "fib 0" 0 (fib 0)
  check "fib 1" 1 (fib 1)
  check "fib 10" 55 (fib 10)
  check "fibFast 0" 0 (fibFast 0)
  check "fibFast 1" 1 (fibFast 1)
  check "fibFast 10" 55 (fibFast 10)
  check "fibFast 50" 12586269025 (fibFast 50)
  check "take 10 fibs"
    [0,1,1,2,3,5,8,13,21,34] (take 10 fibs)

  putStrLn "=== TASK 2: lazy lists ==="
  check "sumEvenSquares 0" 0 (sumEvenSquares 0)
  check "sumEvenSquares 3" 56 (sumEvenSquares 3)
  check "sumEvenSquares 5" 220 (sumEvenSquares 5)
  check "takeWhileRec empty" ([] :: [Int]) (takeWhileRec (< 5) [])
  check "takeWhileRec stop" [1,4,9,16,25]
    (takeWhileRec (< 30) [x*x | x <- [1..]])
  check "takeWhileRec all" [1,2,3] (takeWhileRec (< 10) [1,2,3])
  check "take 10 primes" [2,3,5,7,11,13,17,19,23,29] (take 10 primes)
  check "firstNPrimes 0" [] (firstNPrimes 0)
  check "firstNPrimes 5" [2,3,5,7,11] (firstNPrimes 5)
  check "firstNPrimes 10" [2,3,5,7,11,13,17,19,23,29]
    (firstNPrimes 10)

  putStrLn "=== TASK 3: RPN calculator ==="
  check "RPN addition and multiplication" (Just 20.0)
    (evalRPN ["2","3","+","4","*"])
  check "RPN subtraction order" (Just 7.0)
    (evalRPN ["10","3","-"])
  check "RPN division" (Just 3.0) (evalRPN ["6","2","/"])
  check "RPN sqrt" (Just 3.0) (evalRPN ["9","sqrt"])
  check "RPN neg" (Just (-5.0)) (evalRPN ["5","neg"])
  check "RPN string" (Just 20.0) (evalRPNString "2 3 + 4 *")
  check "RPN empty" Nothing (evalRPN [])
  check "RPN missing operand" Nothing (evalRPN ["2","+"])
  check "RPN division by zero" Nothing (evalRPN ["5","0","/"])
  check "RPN sqrt of negative" Nothing (evalRPN ["-9","sqrt"])
  check "RPN invalid token" Nothing (evalRPN ["2","cat","+"])
  check "RPN extra values" Nothing (evalRPN ["2","3"])

  putStrLn "=== ALL TESTS COMPLETED ==="
