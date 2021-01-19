// Exercises xp
//  EXC 1
//YOU CAN JUST DO : 
// i + 1
// instead of Number(colors.indexOf(colors[i])+1)

let colors= ['blue','red','yellow','green']
for(let i=0;i<colors.length;i++) {
    console.log("My # "+Number(colors.indexOf(colors[i])+1) + " choice "+colors[i])
}

// Bonus
let position =['1st','2nd','3rd','4th']
for(let i=0;i<colors.length;i++){
    console.log('My '+ position[i] +' choice is '+ colors[i])
}

// EXC 2
let people = ["Greg", "Mary", "Devon", "James"]
for(let i=0;i<people.length;i++) {
    console.log(people[i])
}
people.shift()
people.splice(2,1,'Jason')
console.log(people)
people.push('Itamar')
console.log('hello')
for(let i=0;i<people.length;i++){    
    if(i=='Jason'){
        break;
    }
    console.log(people[i])
   }
//    Im not sure why this isnt working
//YOU DIDN'T DO THE INSTRUCTION HERE
let copy=people.slice(1,3)
console.log(copy)
console.log(people.indexOf('Mary'))
console.log(people.indexOf('foo'))
let last=people[people.length-1]
console.log(last)

// EXC 3: GOOD
//IT SEEMS GOOD
// let number = prompt('Please give me a number :)')
// while(number<10){
//     number=prompt('Please give me a number :)')
// }

// EXC 4 : YOU DIDN'T FINISH THE EXERCISE HERE

let guestList = {
  Randy: "Germany",
  Karla: "France",
  Wendy: "Japan",
  Norman: "England",
  Sam: "Argentina"
}
let name = prompt('What is your name?')
for(let i in guestList){
if(name!=i){
    continue;
   
}else if(name==i) {
    console.log('hello '+ i +' from '+guestList[i] )
}else{
    console.log('hi guest')
}


}
// EXC 5
// A VARIABLE SHOULD'T START WITH AN UPPERCASE LETTER 
// let family
let Family = {
  Randy: "Father",
  Karla: "Mother",
  Wendy: "Daughter",
  Norman: "Brother1",
  Sam: "Brother2"
}

//EXC 6
      let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
        names =names.sort()
        let array =[]
for(i=0;i<names.length;i++){

     array.push(names[i].charAt(0))

    }if(array.length==6){
   
 
  
        console.log(array.join(" "))
}