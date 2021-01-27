let text = document.getElementById('textInput')
console.log(text.value)
text.addEventListener('keypress', lettersOnly)
let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
let num = text.value

function lettersOnly() {

    if (text.value.includes(7)) {
        num = num.slice(0, -1)

    }

}