# <tt>Software Development Plan</tt>

## Phase 0: Requirements Specification 

1. Build two basic GUI applications
2. Apply the basics of event-driven programming
3. Interact with elements with JavaScript

## Phase 1: System Analysis 

**Madlibs**:
The madlib class takes the user's noun, pastence verb, presantence verb, adjective, and object. and prints to the html file a mad lib.

```
class MadLib(noun, pastVerb, presVerb, adjective, object, outline) {
  //constructor here

  //work functions
  
  //helper functions 
}
```
**Mortgage Calculator**:
The Mortgage class takes the user inputs loan amount, annual interest rate, and number of years the payments last. The output tells you the monthly payments you would have to make.

```
class Mortgage(amount, interestRate, fixedYears) {
  //constructor here

  //work functions

  //helper functions
}
```
 

## Phase 2: Design 

```
class MadLib(noun, pastVerb, presVerb, adjective, object) {
  this.noun = noun;
  this.pastVerb = pastVerb;
  this.presVerb = presVerb;
  this.adjective = adjective;
  this.object = object;



  toString() {
    return outline with nouns, pastVerbs, presVerbs, adjectives, and objects
  }
}
```

```
class Mortgage(amount, interestRate, fixedYears) {
  this.amount = amount;
  this.interestRate = interest;
  this.fixedYears = years;

  function monthlyPayments() {

    return (amount*(monthlyInterestRate(1+monthlyInterestRate())^payments())/((1+monthlyInterestRate())^payments()-1))
  }

  function toString() {
    return `Loan amount: amount\nAPR: interestRate\nLife of loan: years\nMonthly interest rate: ${monthlyInterestRate()}\nMonthly payments: ${monthlyPayments}`
  }

  function monthlyInterestRate() {
    return interestRate/12
  }

  function payments() {
    return years*12
  }
}
```

## Phase 3: Implementation 

TODO: Write encountered problems you ran into while implementing your code, and what parts of your code seem to be the weakest.

## Phase 4: Testing & Debugging 

TODO: After debugging your code write the method names for any tests run and what they test for.

## Phase 5: Deployment 

TODO: Wait for bug reports and continue to phase 6.

## Phase 6: Maintenance

TODO: Record all bug fixes to git and as they come. Be nice to the people reporting them.