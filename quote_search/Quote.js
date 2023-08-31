class Quote {
  constructor(_id, content, author) {
    this._id = _id;
    this.content = content;
    this.author = author;
    this.pinned = false;
  }

  static fromData(obj) {
    let quotes = [];
    if(obj.content !== undefined){
      quotes.push(new Quote(obj._id, obj.content, obj.author));
      console.log(quotes);
    } else {
      for (let i = 0; i < obj.results.length; i++) {
        quotes.push(new Quote(obj.results[i]._id, obj.results[i].content, obj.results[i].author));
      }
    }
    return quotes;
  }

  pinUnpin() {
    this.pinned = !this.pinned;
    let quoteElement = document.getElementById(`${this._id}`);
    if (this.pinned) {
      document.getElementById("pinned-container").appendChild(quoteElement);
      quoteElement.setAttribute("aria-label", `Pinned quote by ${this.author} ${this.content}`); // Update ARIA label
    } else {
      document.getElementById("quotes-container").appendChild(quoteElement);
      quoteElement.setAttribute("aria-label", `Quote by ${this.author} ${this.content}`); // Update ARIA label
    }
  }
}

