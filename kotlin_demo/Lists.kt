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
    if (x < 2) { return false } //there might have been a typo on this line
    for (i in 2 until x) {
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
/**
 * This function generates a list of counting numbers up to a given limit.
 * @param limit The upper limit for the counting numbers. If limit is null, the function returns null.
 * @return A list of counting numbers from 1 to limit, or null if limit is null.
 */
fun countingNumbers(limit : Int?) : List<Int>? {
    return limit?.let { (1..it).toList() }
}

/**
 * This function generates a list of even numbers up to a given limit.
 * @param limit The upper limit for the even numbers. If limit is null, the function returns null.
 * @return A list of even numbers from 1 to limit, or null if limit is null.
 */
fun evenNumbers(limit : Int?) : List<Int>? {
    return limit?.let { (1..it).filter { it % 2 == 0 } }
}

/**
 * This function generates a list of prime numbers up to a given limit.
 * @param limit The upper limit for the prime numbers. If limit is null, the function returns null.
 * @return A list of prime numbers from 1 to limit, or null if limit is null.
 */
fun primeNumbers(limit : Int?) : List<Int>? {
    return limit?.let { (1..it).filter { isPrime(it) } }
}

/**
 * This function generates all sublists of a given list.
 * @param list The list to generate sublists from. If list is null, the function returns null.
 * @return A list of all sublists of the input list, or null if the input list is null.
 */
fun<T> subLists(list: List<T>?) : List<List<T>>? {
    return list?.let { (0 until it.size).map { i -> it.subList(i, it.size) } }
}

/**
 * This function counts the total number of elements in a list of lists.
 * @param list The list of lists to count elements from. If list is null, the function returns null.
 * @return The total number of elements in all lists in the input list, or null if the input list is null.
 */
fun<T> countElements(list: List<List<T>?>?) : Int? {
    return list?.sumBy { it?.size ?: 0 }
}

/**
 * This function merges two lists into one.
 * @param list1 The first list to merge. If list1 is null, the function returns null.
 * @param list2 The second list to merge. If either list1 or list2 is null, the function returns null.
 * @return The merged list containing all elements from both input lists, or null if either input list is null.
 */
fun<T> merge(list1: List<T>?, list2: List<T>?) : List<T>? {
    return list1?.let { l1 -> list2?.let { l2 -> l1 + l2 } }
}

/**
 * This function applies a binary function to each sublist in a given list of lists and reduces each sublist to a single value by repeated application of the binary function.
 * @param f The binary function to apply. It takes two integers as input and returns an integer.
 * @param lists The list of lists to apply the binary function to. If lists is null, the function returns null.
 * @return A new list where each element is the result of reducing a sublist from the input lists by repeated application of f, or null if lists is null.
 */
fun listApply(f: (Int, Int) -> Int, lists: List<List<Int>>?) : List<Int>? {
    return lists?.map { it.reduce(f) }
}

/**
 * This function composes a list of unary functions into one unary function by applying them in order from last to first.
 * @param functions The list of unary functions to compose. Each unary function takes an integer as input and returns an integer.
 * @return The composed unary function that applies all functions in the input list in order from last to first.
 */
fun composeList(functions: List<(Int) -> Int>) : (Int) -> Int {
    return functions.reduce { f, g -> compose(f, g) }
}