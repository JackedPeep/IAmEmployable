
const errorSound = new Audio('system-error-notice-132470.mp3');

document.getElementById("search-input").addEventListener("keydown", function(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    performSearch();
  }
});

async function performSearch() {
  let searchInput = document.getElementById("search-input");
  let searchTerm = searchInput.value.trim();

  if (searchTerm === "") {
    displayError("Please enter a search term.");
    errorSound.play();
    return;
  }

  // Search functionality
  const results = await fetch(`https://usu-quotes-mimic.vercel.app/api/search?query=${searchTerm}`);
  const data = await results.json();

  if (data.totalCount > 0) {
    let quotes = Quote.fromData(data);
    displayQuotes(quotes);
  } else {
    displayError("No quotes found for your search term.");
    errorSound.play();
  }
}

async function displayRandomQuote() {
  const result = await fetch("https://usu-quotes-mimic.vercel.app/api/random");
  const data = await result.json();
  console.log(data);
  let randomQuote = Quote.fromData(data);
  displayQuotes(randomQuote);
}

displayRandomQuote()

// Display the error message to the user
function displayError(errorMessage) {
  let quotesContainer = document.getElementById("quotes-container");
  quotesContainer.textContent = errorMessage;
  quotesContainer.setAttribute("role", "alert");
}

function displayQuotes(quotes) {
  let quotesContainer = document.getElementById("quotes-container");
  quotesContainer.innerHTML = ""; 
  
  for (let quote of quotes) {
    let quoteElement = document.createElement("div");
    quoteElement.classList.add(`quote`);
    quoteElement.id = `${quote._id}`;
    quoteElement.setAttribute("role", "article");
    quoteElement.setAttribute("aria-label", `Quote by ${quote.author} ${quote.content}`);
    quoteElement.setAttribute("aria-live", "polite");

    let contentElement = document.createElement("p");
    contentElement.textContent = `"${quote.content}"`;
    quoteElement.appendChild(contentElement);

    let authorElement = document.createElement("p");
    authorElement.textContent = `~ ${quote.author}`;
    quoteElement.appendChild(authorElement);
    
    // Add pin button
    const pinButton = document.createElement("button");
    pinButton.classList.add("pin-button");
    const pinIcon = document.createElement("span");

    pinIcon.textContent = "push_pin";
    pinIcon.className = "material-icons";
    pinButton.appendChild(pinIcon);

    pinButton.addEventListener("click", () => {
      quote.pinUnpin();
      console.log(quote.pinned)
    });
    pinButton.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        quote.pinUnpin();
        console.log(quote.pinned);
      }
    });
    quoteElement.appendChild(pinButton);
    quotesContainer.appendChild(quoteElement);
  }
}





