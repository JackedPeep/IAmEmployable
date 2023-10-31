// Do not remove or rename the package
package lists

/*
* The following functions are helper functions that I am providing
*/

/*
* Extend the List class with a "tail" getter to get the tail of a list.
* Below is an example of how you would use tail
*    val a = listOf(1,2,3)
*    val t = a.tail
*    println("tail of $a is $t") // prints [2,3]
*/
val <T> List<T>.tail: List<T>
get() = drop(1)

/*
* Extend the List class with a "head" getter to get the head of a list.
* Below is an example of how you would use head
*    val a = listOf(1,2,3)
*    val h = a.head
*    println("head of $a is $h") // prints 1
*/
val <T> List<T>.head: T
get() = first()

/* 
* The isPrime function takes as input an Int
*      x : an Int object to test
* and returns a Boolean
*      true  if x is a prime
*      false if x is not a prime
*/
fun isPrime(x : Int) : Boolean {
    if (i < 2) { return false }
    for (i in 2..(x-1)) {
        if (x % i == 0) {
            return false
        }    
    }
    return true
}

/* The compose function takes as input
*     f - A function that takes as input a value of type T and returns a value of type T
*     g - A function that takes as input a value of type T and returns a value of type T
*  and returns as output the composition of the functions
*     f(g(x))
*/
fun<T> compose(f: (T)->T,  g:(T) -> T) : (T) -> T = { f(g(it)) }

/* Be sure to document 
   your functions
   describing inputs and outputs and what the function does
*/
// countingNumbers function
fun countingNumbers(limit : Int?) : List<Int>? {
    return limit?.let { (1..it).toList() }
}

// evenNumbers function
fun evenNumbers(limit : Int?) : List<Int>? {
    return limit?.let { (1..it).filter { it % 2 == 0 } }
}

// primeNumbers function
fun primeNumbers(limit : Int?) : List<Int>? {
    return limit?.let { (1..it).filter { isPrime(it) } }
}

// subLists function
fun<T> subLists(list: List<T>?) : List<List<T>>? {
    return list?.let { (0 until it.size).map { i -> it.subList(i, it.size) } }
}

// countElements function
fun<T> countElements(list: List<List<T>>?) : Int? {
    return list?.sumBy { it.size }
}

// merge function
fun<T> merge(list1: List<T>?, list2: List<T>?) : List<T>? {
    return list1?.let { l1 -> list2?.let { l2 -> l1 + l2 } }
}

// listApply function
fun listApply(f: (Int, Int) -> Int, lists: List<List<Int>>?) : List<Int>? {
    return lists?.map { it.reduce(f) }
}

// composeList function
fun composeList(functions: List<(Int) -> Int>) : (Int) -> Int {
    return functions.reduce { f, g -> compose(f, g) }
}
