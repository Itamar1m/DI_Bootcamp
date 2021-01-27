document.getElementById('submit').addEventListener('click',sphereCalculation)

function sphereCalculation(event){
event.preventDefault()
let radiusValue=document.forms[0].children[1].value
console.log(document.forms[0].children[3].value)
console.log(radiusValue)
let formula = (4/3) * Math.PI * Math.pow(radiusValue, 3);
console.log(formula)
let answerDisplay=document.forms[0].children[3]//For some reason when i put.value here it doesnt work?

answerDisplay.value=formula

}
