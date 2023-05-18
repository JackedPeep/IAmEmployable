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

// myFilter tests
const data = [1,2,3,4,undefined,5,6,7,0,0,"Hey bud!", null, `You are uncooth`, 'Bee yourself', "",``,'',true,false, x => x === "this is a test"];
const modResultFilter = myFilter(data, i => i % 2 === 0);
const stringResultFilter = myFilter(data, i => typeof i === 'string');
const undefinedResultFilter = myFilter(data, i => typeof i === 'undefined');
const nullResultFilter = myFilter(data, i => i === null);
const boolResultFilter = myFilter(data, i => typeof i === 'boolean');
const funcResultFilter = myFilter(data, i => typeof i === 'function');

console.log(`My test array: ${data}`);
console.log(`My test array length: ${data.length}`)
console.log(modResultFilter); // [2, 4, 6, 0, 0, null, '', '', '', false]; <= this is because 0 is modular to 2 and 0 = '' = null = false.
console.log(stringResultFilter); // ["Hey bud!", `You are uncooth`, 'Bee yourself', '' ,'' ,''];
console.log(undefinedResultFilter); // [undefined];
console.log(nullResultFilter); // [null];
console.log(boolResultFilter); // [true, false];
console.log(funcResultFilter); // [f];



// findLast function
function myFindLast(data, predicate) {
  const reversedArray = [...data].reverse();
    for(const value of reversedArray) {
      if (predicate(value)) return value;
    }
}

// myFindLast test
const modResultFindLast = myFindLast (data, i => i % 2 === 0);
const stringResultFindLast = myFindLast (data, i => typeof i === 'string');
const undefinedResultFindLast = myFindLast (data, i => typeof i === 'undefined');
const nullResultFindLast = myFindLast (data, i => i === null);
const boolResultFindLast = myFindLast (data, i => typeof i === 'boolean');
const funcResultFindLast = myFindLast (data, i => typeof i === 'function');

console.log(`My test array: ${data}`);
console.log(`My test array length: ${data.length}`)
console.log(modResultFindLast); // false; <= this is because 0 is modular to 2 and 0 = '' = null = false.
console.log(stringResultFindLast); // '';
console.log(undefinedResultFindLast); // undefined;
console.log(nullResultFindLast); // null;
console.log(boolResultFindLast); // false;
console.log(funcResultFindLast); // x => x === "this is a test";


// myMap function
function myMap(data, callback) {
  let coppyData = [...data];
  for(let i = 0; i < coppyData.length; i++) {
    coppyData.splice(i, 1, callback(coppyData[i]));
  }
  return coppyData;
}

// myMap test

const doubles = myMap(data, x => x * 2);
console.log(doubles); // [2, 4, 6, 8, NaN, 10, 12, 14, 0, 0, NaN, 0, NaN, NaN, 0, 0, 0, 2, 0, NaN];
const strings = myMap(data, x => `${x}`);
console.log(strings); // ['1', '2', '3', '4', 'undefined', '5', '6', '7', '0', '0', 'Hey bud!', 'null', 'You are uncooth', 'Bee yourself', '', '', '', 'true', 'false', 'x => x === "this is a test"'];

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

// myPairIf test

const labels = ["positive", "negative"];
const nums = [1, -3, -5, 12];
const pairs = myPairIf(labels, nums, (label, num) => {
  return (label === "negative" && num < 0) || (label === "positive" && num >= 0);
});
console.log(pairs); // [["positive", 1], ["positive", 12], ["negative", -3], ["negative", -5]];

// // reduce function
// function reduce(data1, reducer, initialValue) {

// }