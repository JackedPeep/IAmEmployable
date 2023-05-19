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

// myMap test
const doubles = myMap(data, x => x * 2);
console.log(doubles); // [2, 4, 6, 8, NaN, 10, 12, 14, 0, 0, NaN, 0, NaN, NaN, 0, 0, 0, 2, 0, NaN];
const strings = myMap(data, x => `${x}`);
console.log(strings); // ['1', '2', '3', '4', 'undefined', '5', '6', '7', '0', '0', 'Hey bud!', 'null', 'You are uncooth', 'Bee yourself', '', '', '', 'true', 'false', 'x => x === "this is a test"'];

// myPairIf test
const labels = ["positive", "negative"];
const nums = [1, -3, -5, 12];
const pairs = myPairIf(labels, nums, (label, num) => {
  return (label === "negative" && num < 0) || (label === "positive" && num >= 0);
});
console.log(pairs); // [["positive", 1], ["positive", 12], ["negative", -3], ["negative", -5]];

// myReduce test

const numBum = [1,2,3,4,5];
const sum = myReduce(numBum, (value, accumulatedResult) => value + accumulatedResult, 0);
console.log(sum); // 15

const evensAndOdds = myReduce(numBum, (value, accumulatedResult) => {
  if (value % 2 == 0) {
    accumulatedResult.evens.push(value);
  } else {
    accumulatedResult.odds.push(value);
  }
  return accumulatedResult;
}, {evens: [], odds: []});

console.log(evensAndOdds); //{evens: [2,4], odds: [1,3,5]};