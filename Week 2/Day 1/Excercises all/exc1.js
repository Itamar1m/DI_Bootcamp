// Excersise 1
console.log('Excersise 1:')
console.log(5 + '34')
console.log(5 - '4')
console.log(10 % 5)
console.log('java' + 'Script')
console.log(" " + " ")
console.log(" " + 0)
console.log(true + true)
console.log(true + false)
console.log(3 - 4)
console.log("bob" - 'bill')

// Excersise 2
console.log('Excersise 2:')
let me = ['my', 'favorite', 'color', 'is', 'blue']
let string = me.join(" ")
console.log(string)

// Excersise 3
// console.log('Excersise 3:')
let string1 = "Hello ";
let string2 = 'world';
let string3 = string1.replace('H', 'w') + string2.replace('w', 'H')
console.log(string3)


let string44 = string1.slice(0, 1) + string2.slice(1, string2.length)
console.log(string44)
let string45 = string2.slice(0, 1) + string1.slice(1, string1.length)
console.log(string45)
console.log(string45 + ' ' + string44)

//Excersise 4
// console.log('Excersise 4:')
// let firstNumber = Number(prompt('Type in a number'))
// console.log(firstNumber)
// let secondNumber = Number(prompt('Type in another number'))
//  console.log(secondNumber)
// let answer = alert(firstNumber +'+ '+ secondNumber +' =' + (firstNumber+secondNumber))

//Excersise 5
console.log('Excersise 5:')
let sentence = ['I', 'am', 'finding', 'nemo']
let log = 'I found nemo at ' + sentence.length

if (log == "I found nemo at 4") {
    console.log("I found nemo at 4")
} else {
    console.log('I cant find nemo')
}
// Excersise 6
// Part 1
console.log('Excersise 5:')
console.log(5 >= 1)
console.log(0 === 1)
console.log(4 <= 1)
console.log(1 != 1)
console.log("A" > "B")
console.log("B" < "C")
console.log("a" > "A")
console.log("b" < "A")
console.log(true === false)
console.log(true != true)
// Part 2
let c;
let a = 34;
let b = 21;
a = 2;
a + b;
// a+ b =23
// c=undefined
75
// Part 3
// let promp = prompt('Plese give 2 numbers sepertated by a comma and a space');
// console.log(promp)
// pro = promp.charAt(0)* promp.charAt(3)
// alert(promp)
// Part 4
let prom = prompt('Please type a number')
let o = 'o'
let boom='b'+o.repeat(prom)+'m'

    if (prom < 2) {
            console.log('boom')
        } else if(prom >= 2 && prom%2 != 0 && prom%5!=0){
            console.log(boom)
        }else if(prom >= 2 && prom%5==0 && prom%2 != 0 ){
           console.log(boom+'!')
        }else if (prom >= 2 && prom %2 ==0 && prom %5!=0 ){
            console.log(boom.toUpperCase())
        }else if(prom >= 2 && prom %2 ==0 && prom %5==0){
            console.log(boom.toUpperCase()+'!')
        }
