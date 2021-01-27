<<<<<<< HEAD
// Mandatory Excercise.
// Excercise 1
// Change ID
// let mainDiv = document.body.firstElementChild //could also get element by ID
// mainDiv.setAttribute('id', 'socialNetworkNavigation')
// // add new li to the ul.

// let linkList = document.createElement('li')
// let linkText = document.createTextNode('Logout')

// mainDiv.children[0].appendChild(linkList)
// linkList.appendChild(linkText)
// //Bonus
// console.log(getElemeytant)
// console.log()

// excercise 2
let lists =document.getElementsByTagName('ul')
lists[0].lastElementChild.innerHTML='Richard'
lists[0].firstElementChild.innerHTML='Itamar'
lists[1].firstElementChild.innerHTML='Itamar'



let heyStudents1 =document.createElement('li')
let heyStudents =document.createElement('li')
let text2=document.createTextNode('Hey students')
let text=document.createTextNode('Hey students')
lists[0].appendChild(heyStudents)
heyStudents.appendChild(text)
heyStudents1.appendChild(text2)
lists[1].appendChild(heyStudents1)
let sara = lists[1].children[1]
lists[1].removeChild(sara)
=======
// Mandatory Excercise.
// Excercise 1
// Change ID
// let mainDiv = document.body.firstElementChild //could also get element by ID
// mainDiv.setAttribute('id', 'socialNetworkNavigation')
// // add new li to the ul.

// let linkList = document.createElement('li')
// let linkText = document.createTextNode('Logout')

// mainDiv.children[0].appendChild(linkList)
// linkList.appendChild(linkText)
// //Bonus
// console.log(getElemeytant)
// console.log()

// excercise 2
let lists =document.getElementsByTagName('ul')
lists[0].lastElementChild.innerHTML='Richard'
lists[0].firstElementChild.innerHTML='Itamar'
lists[1].firstElementChild.innerHTML='Itamar'



let heyStudents1 =document.createElement('li')
let heyStudents =document.createElement('li')
let text2=document.createTextNode('Hey students')
let text=document.createTextNode('Hey students')
lists[0].appendChild(heyStudents)
heyStudents.appendChild(text)
heyStudents1.appendChild(text2)
lists[1].appendChild(heyStudents1)
let sara = lists[1].children[1]
lists[1].removeChild(sara)
>>>>>>> c32bad666f0f79b38aed580d610b5033c01498df
