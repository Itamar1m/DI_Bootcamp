function getBold_items() {
//   let boldWords=  document.querySelectorAll('strong')
let boldWords =document.getElementsByTagName('strong')
console.log(boldWords)
return boldWords
}
let highlighted=getBold_items()
console.log(highlighted)


function highlight() {
for(i=0;i<=highlighted.length-1 ;i++){
    highlighted[i].style.color='blue'
}

}


function return_normal() {
    for(i=0;i<=highlighted.length-1 ;i++){
        highlighted[i].style.color='black'
    }
    

}
let paragraph=document.getElementsByTagName('p')
console.log(paragraph)
document.body.firstElementChild.addEventListener('click',highlight)
document.body.firstElementChild.addEventListener('MouseOut',return_normal)
// mouseout/over not working only click.......
