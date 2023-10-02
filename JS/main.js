console.log("we are good");

function isPangram(sentence) {
    let allLetters = 'abcdefghijklmnopqrstuvwxyz'
    for (letter of sentence){
        if (allLetters.indexOf(letter.toLowerCase()) !== -1){
            allLetters = allLetters.replace(letter.toLowerCase(), '')
        }
    }
    return result = allLetters.length > 0 ? false : true;
}

// console.log(isPangram('The five boxing wizards jumps quick'))
console.log(isPangram('The five boxing wizards jumps quickly'))

