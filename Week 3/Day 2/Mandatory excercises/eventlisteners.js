<<<<<<< HEAD
// Adding a paragraph.
let paragraph = document.getElementsByTagName('p')
for (i = 0; i <= paragraph.length - 1; i++) {
    paragraph[i].classList.add('para_article')
}

// Removing final paragraph.
let finalParagraph = document.body.firstElementChild.lastElementChild

finalParagraph.remove()
//Remove h2 onclick
let secondHeading = document.getElementById('header2')
secondHeading.addEventListener('click', removeHeader)

function removeHeader() {
    secondHeading.remove()
}
//remove firstHeader
let firstHeader = document.body.firstElementChild.children[0]
firstHeader.remove()
//hide firstParagraph
console.log(paragraph[0])
paragraph[0].addEventListener('click', hideP1)

function hideP1() {
    paragraph[0].style.display = 'none'
}
//value and append them.

let table=document.createElement('table')
let tableRow1=document.createElement('tr')
let tableRow2=document.createElement('tr')
table.style.border="solid black"
document.body.appendChild(table)

let form= document.forms[0]
console.log(form)
console.log(form[1])
let thought =form[1]
let names=form[0]
thought.addEventListener('change',addThought)
function addThought(){
    tableRow2.innerHTML=thought.value
 }
names.addEventListener('change',addName)
 function addName(){
    tableRow1.innerHTML=names.value
 }
 table.appendChild(tableRow1)
 table.appendChild(tableRow2)
// tableRow2.appendChild(thought) 


=======
// Adding a paragraph.
let paragraph = document.getElementsByTagName('p')
for (i = 0; i <= paragraph.length - 1; i++) {
    paragraph[i].classList.add('para_article')
}

// Removing final paragraph.
let finalParagraph = document.body.firstElementChild.lastElementChild

finalParagraph.remove()
//Remove h2 onclick
let secondHeading = document.getElementById('header2')
secondHeading.addEventListener('click', removeHeader)

function removeHeader() {
    secondHeading.remove()
}
//remove firstHeader
let firstHeader = document.body.firstElementChild.children[0]
firstHeader.remove()
//hide firstParagraph
console.log(paragraph[0])
paragraph[0].addEventListener('click', hideP1)

function hideP1() {
    paragraph[0].style.display = 'none'
}
//value and append them.

let table=document.createElement('table')
let tableRow1=document.createElement('tr')
let tableRow2=document.createElement('tr')
table.style.border="solid black"
document.body.appendChild(table)

let form= document.forms[0]
console.log(form)
console.log(form[1])
let thought =form[1]
let names=form[0]
thought.addEventListener('change',addThought)
function addThought(){
    tableRow2.innerHTML=thought.value
 }
names.addEventListener('change',addName)
 function addName(){
    tableRow1.innerHTML=names.value
 }
 table.appendChild(tableRow1)
 table.appendChild(tableRow2)
// tableRow2.appendChild(thought) 


>>>>>>> c32bad666f0f79b38aed580d610b5033c01498df
