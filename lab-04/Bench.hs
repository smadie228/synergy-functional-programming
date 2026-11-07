module Main where

import Lab4 (sumEvenSquares)
import Control.Exception (evaluate)
import System.CPUTime (getCPUTime)

measure :: String -> Integer -> IO ()
measure title value = do
  start <- getCPUTime
  result <- evaluate value
  finish <- getCPUTime
  let seconds = fromIntegral (finish - start) / 1000000000000 :: Double
  putStrLn (title ++ ": result = " ++ show result)
  putStrLn ("CPU time (seconds) = " ++ show seconds)

main :: IO ()
main = do
  putStrLn "=== Optional exercise: CPU time ==="
  measure "sumEvenSquares 1000000" (sumEvenSquares 1000000)
  measure "sum [1..1000000]" (sum [1..1000000] :: Integer)
  putStrLn "Times depend on the computer, compiler flags, and each run."
