module Lists where

-- countingNumbers
countingNumbers :: [Int]
countingNumbers = [1 ..]

-- MultiplesOfNumbers
multiplesOfNumbers :: Int -> [Int]
multiplesOfNumbers n = [n, 2 * n ..]

-- woodallNumbers
woodallNumbers :: [Int]
woodallNumbers = [n * 2 ^ n - 1 | n <- [1 ..]]

-- padovanNumbers
padovanNumbers :: [Int]
padovanNumbers = 1 : 1 : 1 : next padovanNumbers
  where
    next (first : second : third : rest) = (first + second) : next (second : third : rest)
    next _ = [] -- catch all

-- order
order :: (Ord a) => (a -> a -> Bool) -> [a] -> [a] -> [a]
order comp a1 a2 = quicksort comp (a1 ++ a2)
  where
    -- quicksort is a helper function defined within the scope of the order function.

    quicksort :: (Ord a) => (a -> a -> Bool) -> [a] -> [a]
    quicksort _ [] = []
    quicksort comp (el1 : bigArray) =
      -- smallerSorted is a list of elements from bigArray that are smaller than or equal to el1 (eliment one in the array).
      let smallerSorted = quicksort comp [a | a <- bigArray, comp a el1]
          -- biggerSorted is a list of elements from bigArray that are greater than el1 (eliment one in the array).
          biggerSorted = quicksort comp [a | a <- bigArray, not (comp a el1)]
       in smallerSorted ++ [el1] ++ biggerSorted

-- pairUp
-- This function takes a list and pairs up adjacent elements.
pairUp :: [a] -> [[a]]
pairUp [] = [] -- catch if empty
pairUp [x] = [[x]] -- catch if single element.
pairUp (first : second : rest) = [first, second] : pairUp rest -- Pair up the first two elements and recursively process the rest.

-- runLengthEncoding
-- This function performs run-length encoding on a list.
runLengthEncoding :: Eq a => [a] -> [(a, Int)]
runLengthEncoding [] = [] -- catch if empty
runLengthEncoding (first : rest) = countOccurrences (first, 1) rest
  where
    countOccurrences (element, count) [] = [(element, count)]
    countOccurrences (element, count) (next : remaining)
      | element == next = countOccurrences (element, count + 1) remaining -- If the next element is the same, increment the count and continue.
      | otherwise = (element, count) : countOccurrences (next, 1) remaining -- If it's different, start counting a new element.

-- listPairApply
-- This function applies a list of binary functions to pairs of elements in a list of lists.
listPairApply :: [a -> a -> a] -> [[a]] -> [a]
listPairApply functions lists = zipWith ($) (cycle modifiedFunctions) lists
  where
    modifiedFunctions = map (\function list -> if length list == 1 then head list else function (head list) (list !! 1)) functions

-- composeList
-- This function composes a list of functions into a single function.
composeList :: [a -> a] -> a -> a
composeList = foldr (.) id -- Use foldr to compose all functions in the list with function composition (.).
