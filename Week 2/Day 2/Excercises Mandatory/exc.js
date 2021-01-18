// Excersises: xp
// Exc 1:
console.log('exc1:')
let x = 55
let y = 10
if (x > y) {
    console.log('x is the bigger number')

} else {
    console.log('Y is the bigger number')
}
// Exc2
console.log('exc2:')
let newDog = 'chihuahua'
console.log(newDog.length)
console.log(newDog.toUpperCase())
console.log(newDog.toLowerCase())
if (newDog == 'chihuahua') {
    console.log('I love chihuahua, it’s my favorite dog breed')

} else {
    console.log('I dont care, I prefer cats')
}
// Exc3
console.log('exc3:')
let number = prompt('Give me a number')
if (number % 2 == 0) {
    console.log(number + ' is an even number')
} else {
    console.log(number + ' is not an even number')
}
// Exc4
console.log('exc4:')
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
if (users.length == 1) {
    console.log(users + ' is online')

} else if (users.length == 2) {
    console.log(users[0] + " and " + users[1] + ' are online')

    }else if(users.length>2){
        console.log(users[0] + " and " + users[1] + "and " +(users.length -2).toString() +" more users are online")
    }else{
        console.log('no one is online')
    }
    // Exc 2
