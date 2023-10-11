console.log("We are good !!!");

const deckOfCards = {
  deck: [],
  drawnCards: [],
  suits: ["heart", "spades", "clubs", "diamonds"],
  values: "2,3,4,5,6,7,8,9,10,J,Q,K,A",
  initializeDeck() {
    // destructing deckOfCards object with this keyword
    // here, this keyword refers to the scope of deckOfCards object
    const { deck, suits, values } = this;
    for (let suit of suits) {
      for (let value of values.split(",")) {
        deck.push({
          suit,
          value,
        });
      }
    }
  },

  drawSingleCard() {
    const card = this.deck.pop();
    this.drawnCards.push(card);
    return card;
  },

  drawMultipleCards(target) {
    const arr = [];
    for (let start = 0; start < target; start++) {
      arr.push(this.drawSingleCard());
    }
    return arr;
  },

  shuffleDeck() {
    const deck = this.deck;
    for (let index = deck.length - 1; index > 0; index--) {
      let randomIndex = Math.floor(Math.random() * deck.length);
      [deck[index], deck[randomIndex]] = [deck[randomIndex], deck[index]];
    }
  },
};
/* -------------------------------------------------------------------------- */
/*                                 GLOBAL NOTE                                */
/* -------------------------------------------------------------------------- */
// window is the global scope on the browser
// when we define a function like following
// function sayHi() {
//   console.log("HI");
// }
// this `sayHi` function is added as property in the `window object`
// In short any function normally refers to the `window object` in browser
// `var` declarations are added to the window object but `let` and `const` aren't

/* -------------------------------------------------------------------------- */
/*                                     END                                    */
/* -------------------------------------------------------------------------- */




