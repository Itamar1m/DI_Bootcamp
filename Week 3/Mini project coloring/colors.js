var colorArray = ['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6',
    '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
    '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A',
    '#FF99E6', '#CCFF1A', 'white',
]
let sideBar = document.body.firstElementChild.firstElementChild
let backgroundArray = "white"// doesnt have to be an array can just be a variable that changes each time a bg color is pickec
//clear button
document.getElementById('clear').addEventListener('click', clear)
console.log(document.getElementsByTagName('buttton'))

function clear() {
    for (g = 0; g <= mainCellDiv.children.length - 1; g++) {
        mainCellDiv.children[g].style.backgroundColor = 'white'
    }
}

function allColors() {
    for (i = 0; i <= colorArray.length - 1; i++) {
        let colorBox = document.createElement('div')
        colorBox.style.backgroundColor = colorArray[i]
        colorBox.style.border = '1px solid black'
        colorBox.style.height = '100%'
        sideBar.appendChild(colorBox)
    }
}
allColors()
let mainCellDiv = document.body.querySelector('.emptyCells')

function emptyCellDiv() {
    for (let index = 0; index < 4200; index++) {
        let cell = document.createElement('div')
        cell.style.border = '.5px solid lightgrey'
        cell.style.height = '100%'
        let mainCellDiv = document.body.querySelector('.emptyCells')
        mainCellDiv.appendChild(cell)
    }
}
emptyCellDiv()
//making empty cells clickable
for (let b = 0; b <= mainCellDiv.children.length - 1; b++) {
    mainCellDiv.children[b].addEventListener('mouseup', clickableCells)
    mainCellDiv.children[b].addEventListener('mousedown', clickableCells)
}


function clickableCells(event) {
    event.target.style.backgroundColor = backgroundArray
}
//making color cells clickable
for (let c = 0; c <= mainCellDiv.children.length - 1; c++) {
    sideBar.children[c].addEventListener('click', getBackgorund)
}
function getBackgorund(event) {
    let newColor = event.target.style.backgroundColor
    backgroundArray=newColor
    // backgroundArray.push(newColor)
    // console.log(backgroundArray)
}
