

// Your previous javascript code is preserved below
// // Excersises xp gold
//  Exc 1: GOOD
let language = prompt('Which language do you speak')
switch (language) {
    case 'french ':
        alert("Bonjour")
        break;
    case 'english':
        alert('Hello')
        break;
    case 'Hebrew':
        alert("Shalom")
        break;
     default:
       alert( '01110011 01101111 01110010 01110010 01111001')
}
// Exc 2: GOOD
let grade =prompt('What is your grade?')
if (grade>90){
    console.log('A')

}else if(grade> 80 && grade<= 90){
    console.log('B')
}else if(grade >=70 && grade<=80){
    console.log('C')
}else{
    console.log('D')
}
// Exc 3
let verb='quick'
if(verb.length ==3){
    console.log(verb+'ing')
}else if (verb.length>3){
    console.log(verb +"ly")
}else{
    console.log(verb)
}

