
class Mortgage{
  constructor() {
    this.amount = 340000;
    this.apr = 5.5;
    this.years = 30;
    this.monthly = this.monthlyPayments();
  }

  monthlyPayments() {
    const rate = this.apr * .01 / 12;
    const months = this.years * 12;
    return (this.amount * ((rate * Math.pow((1 + rate), months)) / (Math.pow((1 + rate),months)-1)));
  }
  
  updateAmount(newAmount) {
    if (Number.isNaN(newAmount)){
      this.amount = 340000
    }
    else this.amount = newAmount;
    this.monthly = this.monthlyPayments();
  }
  updateApr(newApr) {
    if (Number.isNaN(newApr)){
      this.apr = 5.5
    }
    else this.apr = newApr
    this.monthly = this.monthlyPayments();
  }
  updateYears(newYears) {
    if (Number.isNaN(newYears)){
      this.years = 30
    }
    else this.years = newYears
    this.monthly = this.monthlyPayments();
  }
}


const inputAmount = document.getElementById("loan-amount");
const inputAPR = document.getElementById("apr");
const inputYears = document.getElementById("years");
const outputMortgage = document.getElementById("output-monthly-payment");

const textamount = parseFloat(inputAmount.value);
const textapr = parseFloat(inputAPR.value);
const textyears = parseFloat(inputYears.value);

const mortgage = new Mortgage({amount:textamount, apr:textapr, years:textyears});
outputMortgage.innerHTML = `Monthly payment: $${mortgage.monthly.toFixed(2)}`;

inputAmount.addEventListener("blur", () => {
  if(Number.isNaN(parseFloat(inputAmount.value)) && inputAmount.value !== ``) {
    outputMortgage.innerHTML = `ERROR: '${inputAmount.value}' is not a number`
  } else {
    mortgage.updateAmount(parseFloat(inputAmount.value))
    outputMortgage.innerHTML = `Monthly payment: $${mortgage.monthly.toFixed(2)}`;}
});
inputAPR.addEventListener("blur", () => {
  if(Number.isNaN(parseFloat(inputAPR.value)) && inputAPR.value !== ``) {
    outputMortgage.innerHTML = `ERROR: '${inputAPR.value}' is not a number`
  } else {
    mortgage.updateApr(parseFloat(inputAPR.value))
    outputMortgage.innerHTML = `Monthly payment: $${mortgage.monthly.toFixed(2)}`;}
});
inputYears.addEventListener("blur", () => {
  if(Number.isNaN(parseFloat(inputYears.value)) && inputYears.value !== ``) {
    outputMortgage.innerHTML = `ERROR: '${inputYears.value}' is not a number`
  } else {
    mortgage.updateYears(parseFloat(inputYears.value))
    outputMortgage.innerHTML = `Monthly payment: $${mortgage.monthly.toFixed(2)}`;}
});

