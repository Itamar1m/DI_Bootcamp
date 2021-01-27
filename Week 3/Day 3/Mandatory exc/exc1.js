let p 
let timer
function myMove(event) {
     timer = setInterval(call, 2)
p=0
}

function call() {
    if (p == 350) {
        clearInterval(timer)
        document.getElementById('animate').style.top = '0px'
        document.getElementById('animate').style.left = '0px'
    } else {
        p++
        document.getElementById('animate').style.top = p + ".1px"
        document.getElementById('animate').style.left = p + ".1px"
    }
}