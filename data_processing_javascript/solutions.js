// make sure the data is read
console.log(transactions);
console.log(customers);
// Modular functions

// filter function
function myFilter(data, predicate) {
    const filteredArray = [];
      for(const value of data) {
        if(predicate(value)) {
          filteredArray.push(value);
        } else {
          console.log("This is nor the data we are looking for...");
        }
      }
    return filteredArray;
}

// Filter tests
const data = [1,2,3,4,undefined,5,6,7,0,0,"Hey bud!", null, `You are uncooth`, 'Bee yourself', "",``,'',true,false, x => x === "this is a test"];
const modResult = myFilter(data, i => i % 2 === 0);
const stringResult = myFilter(data, i => typeof i === 'string');
const undefinedResult = myFilter(data, i => typeof i === 'undefined');
const nullResult = myFilter(data, i => i === null);
const boolResult = myFilter(data, i => typeof i === 'boolean');
const funcResult = myFilter(data, i => typeof i === 'function');

console.log(`My test array: ${data}`);
console.log(`My test array length: ${data.length}`)
console.log(modResult); // [2,4,6,0,0];
console.log(stringResult); // ["Hey bud!",`You are uncooth`,'Bee yourself',"",``,''];
console.log(undefinedResult); // [undefined];
console.log(nullResult); // [null];
console.log(boolResult); // [true, false];
console.log(funcResult); // [x === "this is a test"];



// // findLast function
// function findLast(data, predicate) {
    
// }

// // map function
// function map(data, callback) {

// }

// // pairIf function
// function pairIf(data1, data2, callback) {

// }

// // reduce function
// function reduce(data1, reducer, initialValue) {

// }