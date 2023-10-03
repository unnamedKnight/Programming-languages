console.log("we are good");

function rollYourDice() {
    randomNumber = 0
    while (randomNumber === 0){
        randomNumber= Math.floor(Math.random() * 7)
    }
    return randomNumber
}

console.log(rollYourDice())