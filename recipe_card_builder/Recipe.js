class Component {

  onReady(el) {
    this.el = el;
  }

  getId() {}

  r(strings, ...components) {
    let output = "";
    for(let i = 0; i < components.length; i++) {
      output += strings[i];
      if(components[i].length !== undefined) {
        for(let j = 0; j < components[i].length; j++) {
          if(components[i][j] instanceof Component) {
            output += components[i][j].render();
            components.push(components[i][j]);
          } else {
            output += components[i][j];
          }
        }
      }
      else if(components[i] instanceof Component) {
        output += components[i].render();
        components.push(components[i]);
      } else {
        output += components[i];
      }
    }
    output += strings[strings.length - 1];
    return output;
  }

  render() {}
}

class Recipe extends Component {
  constructor(recipe) {
    super();
    this.ID = recipe.ID
    this.title = recipe.title;
    this.ingredients = recipe.ingredients;
    this.instructions = recipe.instructions;
  }

  onReady(el) {
    super.onReady(...el);
    el.map((e) => {
      e.addEventListener("click", (event) => {
        if (event.target.classList.contains("delete-ingredient")) {
          const index = event.target.dataset.index;
          this.ingredients.splice(index, 1);
          this.el.innerHTML = this.render();
        } else if (event.target.classList.contains("delete-instruction")) {
          const index = event.target.dataset.index;
          this.instructions.splice(index, 1);
          this.el.innerHTML = this.render();
        } else if (event.target.classList.contains("save-recipe")) {
          writeRecipeToFile(this);
        }
      });
      e.addEventListener("keydown", (event) => {
        if (event.key === "Enter") {
          const newIngredientInput = e.querySelector(".new-ingredient");
          const newInstructionInput = e.querySelector(".new-instruction");
          if (newIngredientInput && newIngredientInput.value) {
            this.ingredients.push(newIngredientInput.value);
            newIngredientInput.value = "";
            this.el.innerHTML = this.render();
          } else if (newInstructionInput && newInstructionInput.value) {
            this.instructions.push(newInstructionInput.value);
            newInstructionInput.value = "";
            this.el.innerHTML = this.render();
          }
        }
      });
    });
  }

  getId() {
    return `recipe-${this.ID}`;
  }

  buildRenderArray(array, type) {
    let divArray = array.map((e, index) => {
      let deleteButtonClass = type === "ingredients" ? "delete-ingredient" : "delete-instruction";
      return `<div class="user-inputs" id="${e}">
                <span>${e}</span>
                <button class="${deleteButtonClass}" data-index="${index}" tabindex="0" aria-label="${e} delete">Delete</button>
              </div>`;
    });
    if (type === "ingredients") {
      divArray.push(`<div><input type="text" class="new-ingredient" placeholder="Add new ingredient..."></div>`);
    } else if (type === "instructions") {
      divArray.push(`<div><input type="text" class="new-instruction" placeholder="Add new instruction..."></div>`);
    }
    return divArray;
  }  

  render() {
    return this.r`
      <div class="recipe-card" id="recipe-${this.ID}" role="article" aria-labelledby="recipe-title-${this.ID}">
        <h2 id="recipe-title-${this.ID}">${this.title}</h2>
        <section aria-labelledby="ingredients-header-${this.ID}">
          <h3 id="ingredients-header-${this.ID}">Ingredients</h3>
          <div class="ingredients">${this.buildRenderArray(this.ingredients, "ingredients")}</div>
        </section>
        <section aria-labelledby="instructions-header-${this.ID}">
          <h3 id="instructions-header-${this.ID}">Instructions</h3>
          <div class="instructions">${this.buildRenderArray(this.instructions, "instructions")}</div>
        </section>
        <button class="save-recipe">Save Recipe</button>
      </div>`;
  }
  
}

let recipes = [];
let id = 100;
const button = document.getElementById("submit");
let titleInput = document.getElementById("title");
let ingredientsInput = document.getElementById("ingredients");
let instructionsInput = document.getElementById("instructions");
//builds the Recipe class
button.addEventListener("click", () => {
  if(!isCorrectInput(titleInput.value)) {
    document.getElementById("title-error").innerHTML = `This field can not be blank.`;
  } 
  if(!isCorrectInput(ingredientsInput.value)) {
    document.getElementById("ingredients-error").innerHTML = `This field can not be blank.`;
  } 
  if(!isCorrectInput(instructionsInput.value)) {
    document.getElementById("instructions-error").innerHTML = `This field can not be blank.`;
  }
  // Check to see if user input is correct on submision.
  if(isCorrectInput(titleInput.value) &&
    isCorrectInput(ingredientsInput.value) &&
    isCorrectInput(instructionsInput.value)) {
    
    id += 1;
    const title = titleInput.value;
    const ingredientsArray = buildClassArray(ingredientsInput.value);
    const instructionsArray = buildClassArray(instructionsInput.value);
    const recipe = new Recipe({ID:id, title:title, ingredients:ingredientsArray, instructions:instructionsArray})
    recipes.push(recipe);

    let cardsHTML = "";
    for (let recipe of recipes) {
      cardsHTML += recipe.render();
    }
    const cardsEl = document.getElementById("cards");
    cardsEl.innerHTML = cardsHTML;

    // Call the onReady method for each recipe
    for (let recipe of recipes) {
      recipe.onReady([cardsEl]);
    }

    titleInput.value = "";
    ingredientsInput.value = "";
    instructionsInput.value = "";
    
  }
});


let inputs = document.querySelectorAll(".recipe-input");
inputs.forEach(input => {
  input.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      
      if(!isCorrectInput(titleInput.value)) {
        document.getElementById("title-error").innerHTML = `This field can not be blank.`;
      } 
      if(!isCorrectInput(ingredientsInput.value)) {
        document.getElementById("ingredients-error").innerHTML = `This field can not be blank.`;
      } 
      if(!isCorrectInput(instructionsInput.value)) {
        document.getElementById("instructions-error").innerHTML = `This field can not be blank.`;
      }
      // Check to see if user input is correct on submision.
      if(isCorrectInput(titleInput.value) &&
        isCorrectInput(ingredientsInput.value) &&
        isCorrectInput(instructionsInput.value)) {
        
        id += 1;
        const title = titleInput.value;
        const ingredientsArray = buildClassArray(ingredientsInput.value);
        const instructionsArray = buildClassArray(instructionsInput.value);
        const recipe = new Recipe({ID:id, title:title, ingredients:ingredientsArray, instructions:instructionsArray})
        recipes.push(recipe);
    
        let cardsHTML = "";
        for (let recipe of recipes) {
          cardsHTML += recipe.render();
        }
        document.getElementById("cards").innerHTML = cardsHTML;
    
        titleInput.value = "";
        ingredientsInput.value = "";
        instructionsInput.value = "";
      }
    }
  });
});





// constructs usable arrays from the user's input
function buildClassArray(string) {
  const array = string.split(",");
  const trimArray = array.map( (e) => {return e.trim();});
  return trimArray;

}

// check for fields to be correct inputs takes an array from build array
function isCorrectInput(input) {
    if(input === "") {
      return false;
    } return true;
}


