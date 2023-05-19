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
    accumulatedResult = reducer(data1[i], accumulatedResult);
  }
  return accumulatedResult;
}

function main() {
  // num invalid transactions
  const invalidTransactions = myFilter(transactions, t = t => (t.amount === undefined || t.amount == false || 
    (t.product !== "FIG_JAM" && t.product !== "FIG_JELLY" && t.product !== "SPICY_FIG_JAM" && t.product !== "ORANGE_FIG_JELLY"))); 
  console.log(`Number of invalid transactions: ${invalidTransactions.length}`);
  
  //num dupes
  const duplicates = myPairIf(customers, customers, (v,t) => {return (v.emailAddress === t.emailAddress && v.id !== t.id)});
  console.log(`Number of duplicate customers: ${duplicates.length/2}`);

  //last transaction ammount over $200
  const lastPerchaseOver200 = myFindLast(transactions, v = v => v.amount > 200);
  console.log(`Most recent transaction over $200: $${lastPerchaseOver200.amount}`);
  
  //num small, medium, large transactions
  const orderSmall = myReduce(transactions, (x,r) => {
    if(x.amount < 25){
      r++;
    }
    return r;
  }, 0);
  const orderMedium = myReduce(transactions, (x,r) => {
    if(25 < x.amount < 75){
      r++;
    }return r;
  }, 0);
  const orderLarge = myReduce(transactions, (x,r) => {
    if(x.amount >= 75){
      r++;
    }return r;
  }, 0);

  console.log(`Number of small transactions: ${orderSmall}\nNumber of medium transactions: ${orderMedium}\nNumber of large transactions: ${orderLarge}`);
//customers with transactions over $200
//debugger;
  const transactionOver200 = myFilter(transactions, x = x => x.amount > 200);
  const pairedArray = myPairIf(transactionOver200, customers, (x,r) => {return x.customerId === r.id});
  const reducedArray = myReduce(pairedArray,(x,r) => {
    if(!r.includes(x[1].id)){
      r.push(x[1]);
  }return r;
  }, []);
  console.log(`Customers with transactions over $200: ${reducedArray}`);
//names of customers with transactions over $200
  const walkingWallets = myMap(reducedArray, c = c => `${c.firstName} ${c.lastName}` );
  console.log(`Names of Customers with transactions over $200: ${walkingWallets}`)
}



main();