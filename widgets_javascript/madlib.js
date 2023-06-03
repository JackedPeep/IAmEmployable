
class Madlib{
  constructor(madlib) {
    this.properNoun = madlib.properNoun;
    this.pastVerb = madlib.pastVerb;
    this.presVerb = madlib.presVerb;
    this.adjective = madlib.adjective;
    this.object = madlib.object;
  }
  myStory() {
    return `${this.properNoun} is ${this.presVerb} down the ${this.adjective} ${this.object}. Before
    ${this.properNoun} was participating in ${this.presVerb} they ${this.pastVerb} by the ${this.object}.
    The ${this.object} started ${this.presVerb} with malice. Nothing could save ${this.properNoun} as their ${this.adjective}
    retribution was at hand. The ${this.object} had, in a previous life, ${this.pastVerb} a ${this.adjective} ${this.properNoun}
    just like this. ${this.object} looked pensive as it started ${this.presVerb} back home.
    `
  }
  
}

const inputNoun = document.getElementById("proper-noun");
const inputPastVerb = document.getElementById("past-verb");
const inputPresVerb = document.getElementById("presant-verb");
const inputAdjective = document.getElementById("adjective");
const inputObject = document.getElementById("object");
const outputMadlib = document.getElementById("output-mad-lib");


const button = document.getElementById("lib-butt");
button.addEventListener("click", () => {
  const noun = inputNoun.value;
  const pastVerb = inputPastVerb.value;
  const presVerb = inputPresVerb.value;
  const adjective = inputAdjective.value;
  const object = inputObject.value;
  if (noun == false){
    outputMadlib.innerHTML = `Please enter a noun`
  }
  else if (pastVerb == false){
    outputMadlib.innerHTML = `Please enter a past tense verb`
  }
  else if (presVerb == false){
    outputMadlib.innerHTML = `Please enter a present tense verb`
  }
  else if(adjective == false){
    outputMadlib.innerHTML = `Please enter an adjective`
  }
  else if (object == false){
    outputMadlib.innerHTML = `Please enter an object`
  }
  else{
    const madLib = new Madlib({properNoun:noun, pastVerb:pastVerb, presVerb:presVerb, adjective:adjective, object:object});
    outputMadlib.innerHTML = `${madLib.myStory()}`;
  }
})


