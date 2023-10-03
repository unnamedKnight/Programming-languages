console.log("we are good");

function getCard() {
  const cardList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"];
  const suitList = ["clubs", "spades", "hearts", "diamonds"];
  let randomCard = Math.floor(Math.random() * cardList.length);
  console.log(randomCard);
  let randomSuit = Math.floor(Math.random() * suitList.length);
  return {
    value: cardList[randomCard],
    suit: suitList[randomSuit],
  };
}

console.log(getCard());
