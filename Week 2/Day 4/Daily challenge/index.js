let words = prompt('Please give me a few words')

words = words.split(" ");

function stars() {
    let array = []
    for (i = 0; i < words.length; i++) {
        (array.push(words[i].length))
     
    }
    array = array.sort()
    let bottomStarAmount = array.splice((array.length - 1), 1)
    let bottomTopBorder = "* ".repeat(bottomStarAmount)
  
    return bottomTopBorder
}
let bottomTopBorder2 = stars()


function frame() {
    console.log(bottomTopBorder2)
    for (i = 0; i < words.length; i++) {
        console.log('* ' + words[i]+" ".repeat(bottomTopBorder2.length-words[i].length-4)+'*')// This gives me an eror if I have more then 4 word && the longets word is about 6 or 7 letters im not sure why??

    
    }
console.log(bottomTopBorder2)


}
frame()
