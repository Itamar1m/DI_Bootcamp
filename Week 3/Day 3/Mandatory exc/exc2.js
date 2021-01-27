let littleBox = document.getElementById('smallBox')
let largeBox = document.getElementById('bigBox')
let largeBox1 = document.getElementById('bigBox1')

//should group th boxes together and make a loop...less steps.
largeBox.addEventListener("dragover", dragOver)
largeBox.addEventListener("drop", drop)
largeBox1.addEventListener("dragover", dragOver)
largeBox1.addEventListener("drop", drop1)


// function dragStart(event) {
//     event.preventDefault();
// }

function dragOver(event) {
    event.preventDefault()
}
function drop(event) {
    largeBox.append(littleBox)
    largeBox.style.display = 'flex'
    largeBox.style.alignItems ='center'
    largeBox.style.justifyContent='center'
}


function drop1(event) {
    largeBox1.append(littleBox)
    largeBox1.style.display = 'flex'
    largeBox1.style.alignItems ='center'
    largeBox1.style.justifyContent='center'
    
}

//     largeBox.innerHTML = '<p>Drag Here</p>'
//     largeBox.style.color = 'white'
//     littleBox.style.display = 'none'
// 
// littleBox.addEventListener("dragend", dragThere)

// function dragThere(event) {

//     let _x = event.clientX;
//     let _y = event.clientY;
//     // console.log(event)



//     console.log(event)
//     littleBox.style.display = 'inherit'
//     event.target.style.position = "absolute";
//     event.target.style.top = _y + "px";
//     event.target.style.left = _x + "px";
// }