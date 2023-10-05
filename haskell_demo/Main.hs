import Lists

{-- Some predefined functions for composing --}
add1 x = 1 + x

add2 x = 2 + x

add3 x = 3 + x

{- testIt takes as input a String and a test, prints the String and
   evaluates the test.
-}
testIt :: (Show t) => (String, t) -> IO ()
testIt (s, f) = do
  putStr "\n"
  putStr s
  putStr "\n"
  print (f)

{- main executes a sequence of tests. Each test is an ordered pair
   of (String, t), where t is the test. Add tests as you like or
   remove tests if you like.
-}
main = do
  let add1 x = 1 + x
  let add2 x = 2 + x
  mapM
    testIt
    [ ("take 3 countingNumbers", take 3 countingNumbers),
      ("take 10 padovanNumbers", take 10 padovanNumbers),
      ("take 10 woodallNumbers", take 10 woodallNumbers),
      ("take 5 multiplesOfNumbers 5", take 5 (multiplesOfNumbers 5)),
      ( "order (<) (take 5 countingNumbers) (take 5 padovanNumbers)",
        order (<) (take 5 countingNumbers) (take 5 padovanNumbers)
      ),
      ( "order (>) (take 5 countingNumbers) (take 5 padovanNumbers)",
        order (>) (take 5 countingNumbers) (take 5 padovanNumbers)
      ),
      ( "order (>) [] (take 5 padovanNumbers)",
        order (>) [] (take 5 padovanNumbers)
      )
    ]
  mapM
    testIt
    [ ( "runLengthEncoding (take 5 countingNumbers)",
        runLengthEncoding (take 5 countingNumbers)
      ),
      ( "runLengthEncoding (take 5 padovanNumbers)",
        runLengthEncoding (take 5 padovanNumbers)
      )
    ]
  mapM
    testIt
    [ ("pairUp (take 5 countingNumbers)", []),
      ("pairUp (take 5 countingNumbers)", pairUp (take 5 countingNumbers))
    ]
  mapM
    testIt
    [ ( "listPairApply [(+),(-)] []",
        listPairApply [(+), (-)] []
      ),
      ( "listPairApply [(+),(-)] (pairUp (take 5 countingNumbers))",
        listPairApply [(+), (-)] (pairUp (take 5 countingNumbers))
      )
    ]
  mapM
    testIt
    [ ("(composeList [add1,add2,add1]) 3", ((composeList [add1, add2, add1]) 3))
    ]
