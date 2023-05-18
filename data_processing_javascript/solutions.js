// make sure the data is read
console.log(transactions);
console.log(customers);
// Modular functions

// myFilter function
function myFilter(data, predicate) {
  const filteredArray = [];
    for(const value of data) {
      if(predicate(value)) {
        filteredArray.push(value);
      }
    }
  return filteredArray;
}

// findLast function
function myFindLast(data, predicate) {
  const reversedArray = [...data].reverse();
    for(const value of reversedArray) {
      if (predicate(value)) return value;
    }
}

// myMap function
function myMap(data, callback) {
  let coppyData = [...data];
  for(let i = 0; i < coppyData.length; i++) {
    coppyData.splice(i, 1, callback(coppyData[i]));
  }
  return coppyData;
}

// pairIf function
function myPairIf(data1, data2, callback) {
  const pairedArray = [];
  for(let i = 0; i < data1.length; i++) {
    for(let j = 0; j < data2.length; j++) {
      if(callback(data1[i],data2[j])) {
        let pair = [data1[i],data2[j]];
        pairedArray.push(pair);
      }
    }
  }
  return pairedArray;
}

// myReduce function
function myReduce(data1, reducer, initialValue) {
  let accumulatedResult = reducer(data1[0], initialValue);
  for(let i = 1; i < data1.length; i++) {
    accumulatedResult = reducer(data1[i], accumulatedResult)
  }
  return accumulatedResult;
}