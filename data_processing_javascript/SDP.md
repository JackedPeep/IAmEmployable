# <tt>Fig Co. Transaction tracker</tt>
Build a file scanner that outputs information that the perscribed company wants.

## Modular functions 

These need to be modular programs that can be added uppon. Highly flexable.

### filter
```
/*
  filter: returns a subset of the input data that contains only the items for which the predicate returns true
  @data: an array of any arbitrary data
  @predicate: a function that takes a single datapoint as an argument. Returns either true or false.
  @return: a new array that contains all of the values in data
           for which the predicate function returns true
*/
function filter(data, predicate)
```
**Example Usage**
```
const data = [1,2,3,4,5,6,7];
const result = filter(data, x => x % 2 === 0);
console.log(result); // [2,4,6];

```
psudo code
```
function filter(data, predicate) {
  let filteredArray = [];
  for each(i in data.length){
    if(predicate == true){
      append data[i];
    }
  }
    return filteredArray;
  
}

```
### findlast
```
/*
  findLast: finds the last value in an array that meets the condition specified in the predicate
  @data: an array of any arbitrary data
  @predicate: a function that takes a single datapoint as an argument. Returns either true or false.
  @return: a single data point from data
*/
function findLast(data, predicate)
```
**Example Usage**
```
const data = [1,2,3,4,5,6,7];
const result = findLast(data, x => x % 2 == 0);
console.log(result); // 6

```
psudo code
```
function findLast(data, predicate){
  const filteredArray = filter(data,predicate);
  return filteredArray[filteredArray.length-1];
}

```
### map
```
/*
  map: creates a new array based on the input array where the value at each position in the array is the result of the callback function.
  @data: an array of any arbitrary data
  @callback: a function that takes a single datapoint as an argument. Returns a new value based on the input value
  @return: a single data point from data
*/
function map(data, callback)
```
**Example Usage**
```
const data = [1,2,3,4,5,6,7];
const doubles = map(data, x => x * 2);
console.log(doubles); // [2,4,6,8,10,12,14];
const strings = map(data, x => `${x}`);
console.log(strings); // ["1","2","3","4","5","6","7"];

```
psudo code
```
function map(data, callback){
  let mappedArray = [];
  for each(i in data.length){
    const mappedValue = callback (data[i])
    append mapped value to mappedArray;
  }
    return filteredArray;
  
}

```
### pairlIf
```
/*
  pairIf: creates a new array based on the input arrays where the value at each position is an 
          array that contains the 2 values that pair according to the predicate function.
  @data1: an array of any arbitrary data
  @data2: an array of any arbitrary data
  @predicate: a function that takes a single datapoint from each input array as an argument. Returns true or false
  @return: a single data point from data
*/
function pairIf(data1, data2, callback)
```
**Example Usage**
```
const labels = ["positive", "negative"];
const nums = [1, -3, -5, 12];
const pairs = pairIf(labels, nums, (label, num) => {
  return (label === "negative" && num < 0) || (label === "positive" && num >= 0);
});
console.log(pairs); // [["positive", 1], ["positive", 12], ["negative", -3], ["negative", -5]];
```
psudo code
```
function pairIf(data1, data2, callback){
  let pairedArray = []
  for each(i in data1){
    for each(j in data2){
      if(data1[i] blah data2[i]){
        append data1[i] + data2[j] to pairedArray
      }
    }
  }
  return pairedArray
}

```
### reduce
```
/*
  reduce: creates an accumulated result based on the reducer function. The value returned
          is the return value of the reducer function for the final iteration.
  @data: an array of any arbitrary data
  @reducer: a function that takes a single datapoint from each input array as an
            argument and the result of the reducer function from the previous iteration.
            Returns the result to be passed to the next iteration
  @initialValue: the starting point for the reduction.
  @return: the value from the final call to the reducer function.
*/
function reduce(data1, reducer, initialValue)
```
**Example Usage**
```
const nums = [1,2,3,4,5];
const sum = reduce(nums, (value, accumulatedResult) => value + accumulatedResult, 0);
console.log(sum); // 15

const evensAndOdds = reduce(nums, (value, acc) => {
  if (value % 2 == 0) {
    acc.evens.push(value);
  } else {
    acc.odds.push(value);
  }
  return acc;
}, {evens: [], odds: []});

console.log(evensAndOdds); //{evens: [2,4], odds: [1,3,5]};
```
psudo code
```
function reduce(data1, reducer, initialValue){
  
  for each(i in data.length){
    initialValue += reducer(data[i], accumulatedResult)
  }
  return initialValue
}
```

## Total measurments:

We will use the modular functions above in combination with callbacks and predicates solve these company issues.

### Measurement of invalid transactions
Input: File Output: number, invalid transactions

psudo code
```
const nonTransactionArray = myFilter(data, if invalid transaction)
print("Number of invalid transactions: nonTransactionArray.length")
```
### Measures the ammount of duplacate customers
Input: File Output: number, duplicate customers

psudo code
```

```
### Allows you to find the most recent transaction over $200
Input: File Output: number, ID of recent transaction over $200

psudo code
```
const transaction = myFindLast(data, transaction > 200)
return worth of transaction
```
### Measures the number of small, medium, and large transactions
Input: File Output: number, small; number, medium; number, large

psudo code
```
small = filter(data, if small)
med = filter(data, if medium)
lrg = filter(data, if large)

print(small.length med.length lrg.length)
```
## Costomer measurments:

This section has yet to be expanded and needs to be constructable based on company needs.

### Identify which costomers have one transaction over $200
Input: File Output: number, unique customer ID

psudo code
```
myPairIf(data1, data2, customer transaction over $200)
```
