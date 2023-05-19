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
  let accumulatedResult = initialValue;
  for(const value of data1) {
    accumulatedResult = reducer(value, accumulatedResult);
  }
  return accumulatedResult;
}

function main() {
  // num invalid transactions
  const invalidTransactions = myFilter(transactions, value = trans => (trans.amount === undefined || trans.amount == false || 
    (trans.product !== "FIG_JAM" && trans.product !== "FIG_JELLY" && trans.product !== "SPICY_FIG_JAM" && trans.product !== "ORANGE_FIG_JELLY"))); 
  console.log(`Number of invalid transactions: ${invalidTransactions.length}`);
  
  //num dupes
  const duplicates = myPairIf(customers, customers, (cust1,cust2) => {return (cust1.emailAddress === cust2.emailAddress && cust1.id !== cust2.id)});
  console.log(`Number of duplicate customers: ${duplicates.length/2}`);

  //last transaction ammount over $200
  const lastPerchaseOver200 = myFindLast(transactions, trans = trans => trans.amount > 200);
  console.log(`Most recent transaction over $200: $${lastPerchaseOver200.amount}`);
  
  //num small, medium, large transactions
  const orderall = myReduce(transactions, (trans,acc) => {
    if(trans.amount < 25) {
      acc.small.push(trans);
    }
    else if(trans.amount < 75) {
      acc.medium.push(trans);
    }
    else if(trans.amount >= 75){
      acc.large.push(trans);
    }
    return acc;
  }, {small: [], medium: [], large: []});

  console.log(`Number of small transactions: ${orderall.small.length}\nNumber of medium transactions: ${orderall.medium.length}\nNumber of large transactions: ${orderall.large.length}`);
//customers with transactions over $200
//debugger;
  const transactionOver200 = myFilter(transactions, trans = trans => trans.amount > 200);
  const pairedArray = myPairIf(transactionOver200, customers, (transaction,customer) => {return transaction.customerId === customer.id});
  const reducedArray = myReduce(pairedArray,(customer,acc) => {
    if(!acc.includes(customer[1])){
      acc.push(customer[1]);
  }return acc;
  }, []);
  console.log(`Customers with transactions over $200: ${reducedArray}`);
//names of customers with transactions over $200
  const walkingWallets = myMap(reducedArray, customer = customer => `${customer.firstName} ${customer.lastName}` );
  console.log(`Names of Customers with transactions over $200: ${walkingWallets}`)
}

main();