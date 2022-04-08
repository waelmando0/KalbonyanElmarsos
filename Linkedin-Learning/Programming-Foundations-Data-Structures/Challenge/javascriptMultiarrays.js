const dinnerChoices = [
    ["salad", "soup", "cheese plate"],
    ["Chicken", "Salmon", "Lasagna"],
]

let appIndex = 0
let mainDishIndex = 1

const firstApp = dinnerChoices[appIndex][0]
const secondApp =  dinnerChoices[appIndex][1]
const thirdMainDish = dinnerChoices[mainDishIndex][2]

console.log(firstApp)
console.log(secondApp)
console.log(thirdMainDish)

dinnerChoices[mainDishIndex][0] = "steak"
console.log(dinnerChoices[mainDishIndex][0])


console.log(dinnerChoices)