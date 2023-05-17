// make sure the data is read
console.log(transactions);
console.log(customers);
// Modular functions

// filter function
function filter(data, predicate) {
    debugger;
    const filteredArray = [];
      for(const i of data) {
        if(predicate) filteredArray.push(data[i]);
      }
    return filteredArray;
}

// Filter tests
const data = [1,2,3,4,undefined,5,6,7,0,0,"Hey bud!", null, `You are uncooth`, 'Bee yourself', "",``,'',true,false, x => x === "this is a test"];
const modResult = filter(data, i => i % 2 === 0);
const stringResult = filter(data, i => typeof i === 'string');
const undefinedResult = filter(data, i => typeof i === 'undefined');
const nullResult = filter(data, i => i === null);
const boolResult = filter(data, i => typeof i === 'boolean');
const funcResult = filter(data, i => typeof i === 'function');
console.log(result); // [2,4,6];
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