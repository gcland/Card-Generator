function printCard(suit, num) {
    if (suit == "club") {
        char = "♣" 
    }
    else if (suit == "diamond") {
        char = "♦"
    }
    else if (suit == "heart") {
        char = "♥"
    }
    else if (suit == "spade") {
        char = "♠"
    } else {
        char = " "
    }
        

    console.log("╔═════════════╗")
    console.log(`║ ${num}           ║`)
    console.log("║             ║")
    console.log("║             ║")
    console.log(`║      ${char}      ║`)
    console.log("║             ║")
    console.log("║             ║")
    console.log(`║           ${num} ║`)
    console.log("╚═════════════╝")
}


suitList = ["club", "diamond", "heart", "spade"]
numList = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

suitIndex = Math.floor(Math.random()*3)
numIndex = Math.floor(Math.random()*12)

console.log(suitList[suitIndex])
console.log(suitList[suitIndex], numList[numIndex])

printCard(suitList[suitIndex], numList[numIndex])