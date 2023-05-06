# Bingo Deck Generator

The main entry point to this program is `bingo.py`.  Run this script to make a Deck of Bingo Cards.


## Unit Tests

You may run all of the unit test suites through PyCharm or by running the `runTests.py` script from your shell.

The starter code consists of 13 test cases, 6 of which pass.  Of those which don't pass, 5 are failures (the tests don't find the expected results) and 2 cause errors (the tested code crashes).

```
$ python runTests.py

test_freeSquares (Testing.testCard.TestCard)
Ensure that odd-numbered cards have 1 "Free!" square in the center ... FAIL
test_id (Testing.testCard.TestCard)
Assert that card ID number is as expected ... FAIL
test_len (Testing.testCard.TestCard)
Assert that card size is as expected ... ERROR

...

======================================================================
FAIL: test_no_duplicates (Testing.testRandNumberSet.TestRandNumberSet)
Ensure that a RandNumberSet contains no duplicates
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/dev/shm/cs1440-falor-erik-assn4/src/Testing/testRandNumberSet.py", line 93, in test_no_duplicates
    self.assertNotIn(n, seen)
AssertionError: 8 unexpectedly found in {1, 2, 3, 4, 5, 6, 7, 8}

----------------------------------------------------------------------
Ran 13 tests in 0.016s

FAILED (failures=5, errors=2)
```

You may also run an individual unit test suite like this:

```
$ python -m unittest Testing/testMenu.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
