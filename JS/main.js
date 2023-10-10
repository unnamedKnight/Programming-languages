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
