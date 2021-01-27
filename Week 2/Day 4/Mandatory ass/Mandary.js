// / Mandatory Exc 1
function checkDriverAge(age) {
    if (age < 18) {
        console.log('Sorry, you are too young to drive this car. Powering off')
    } else if (age == 18)
        console.log('Congratulations on your first year of driving. Enjoy the ride!')
    else {
        console.log('You are old enough to drive, Powering On. Enjoy the ride!')
    }
}
checkDriverAge(5)

function changeEnough(change, amountDue) {

    let value = change[0] * 0.25 + change[1] * 0.10 + change[2] * 0.05 + change[3] * .01
    if (value >= amountDue) {
        return true

    } else {
        return false
    }
}

console.log(changeEnough([7, 5, 0, 1], 3))


// Exc 3
function multiples() {
    let arrayNumber = [];
    for (let number = 0; number <= 500; number++) {
        if (number % 23 == 0) {
            arrayNumber.push(number)
        } else {
            continue;
        }

    }
    return arrayNumber
}
multiples()

function sumNumbers() {
    let listnumbers = multiples()
    let sum = 0
    for (i = 0; i < listnumbers.length; i++) {
        sum = sum + listnumbers[i]

    }
    console.log(sum)
}
sumNumbers()
// Exc 4
let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100,
    coat: 0
}

function checkBasket() {
    let item = prompt('Which item do you want?')

    for (x in amazonBasket) {
        if (item != x) {
            continue;
        } else if ((item == x && amazonBasket[x] >= 1)) {
            console.log("Here you go!")
        } else {
            console.log('Sorry none available') // These conditionals dont work properly ,trying to figure out why.
        }
    }
}
checkBasket()
// Exc 5
let stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
}
let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
}
let shoppingList = ['banana', 'orange', 'apple']

let array = []

function myBill() {
    for (i = 0; i <= shoppingList.length; i++) {
        for (x in prices) {
            if (x != shoppingList[i]) {
                continue;


            } else {
                array.push(prices[x])

            }
        }
        console.log(array)
    }
    return array
}
let cost=myBill()
console.log(cost)
function final() {
    let food = 0
    for (i = 0; i <cost.length; i++) {
        food +=cost[i]
        //Still have 2 more to do...


    }
   return food

}
console.log(final())
