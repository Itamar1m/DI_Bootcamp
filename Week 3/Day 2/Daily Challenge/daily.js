<<<<<<< HEAD
let listItems = document.body.getElementsByTagName('li')
console.log(listItems[1])

document.getElementById('lib-button').addEventListener('click', theStory)

function theStory() {
    let storyDiv = document.createElement('div')
    let storyParagraph = document.createElement('p')
  
    let storyText = document.createTextNode(listItems[1].children[0].value)
    storyDiv.appendChild(storyParagraph)
    storyParagraph.appendChild(storyText)
    document.appendChild(storyDiv)

=======
let listItems = document.body.getElementsByTagName('li')
console.log(listItems[1])

document.getElementById('lib-button').addEventListener('click', theStory)

function theStory() {
    let storyDiv = document.createElement('div')
    let storyParagraph = document.createElement('p')
  
    let storyText = document.createTextNode(listItems[1].children[0].value)
    storyDiv.appendChild(storyParagraph)
    storyParagraph.appendChild(storyText)
    document.appendChild(storyDiv)

>>>>>>> c32bad666f0f79b38aed580d610b5033c01498df
}