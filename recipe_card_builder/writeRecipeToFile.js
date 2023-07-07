function writeRecipeToFile(recipe) {
  // taking from
  function download(text, filename){
    var blob = new Blob([text], {type: "text/html"});
    var url = window.URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
  }
  const output = `
    <html>
      <head>
        <style>
          :root {
            font-family: Inter, Avenir, Helvetica, Arial, sans-serif;
          }
          h1 {
            background-color: rgb(15,35,57);
            color: white;
            padding: 16px;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
          }
          .b-main {
            width: 600px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,.12), 0 1px 2px rgba(0,0,0,.24);
          }
          .b-content {
            padding: 16px;
            display: flex;
            gap: 16px;
          }
          .b-ingredients {
            flex: 1
          }
          .b-instructions {
            flex: 1'
          }
        </style>
      </head>
      <body>
        <main class="b-main">
          <h1>${recipe.title}</h1>
          <div class="b-content">
            <div class="b-ingredients">
              <strong>Ingredients</strong>
              <hr>
              ${
                recipe.ingredients.map(i => (
                  `
                    <div>${i}</div>
                  `
                )).join('')
              }
            </div>
            <div class="instructions">
              <strong>Instructions</strong>
              <hr>
              ${
                recipe.instructions.map((i, index) => (
                  `
                    <div>${index+1}: ${i}</div>
                  `
                )).join('')
              }
            </div>
          </div>
        </main>
      </body>
    </html>
  `;
  download(output, `recipe-card.html`);
}