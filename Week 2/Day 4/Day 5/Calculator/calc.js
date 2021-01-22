
// Calculator....
let arrayNumbers = []
function my_f(num) {
    if(num==='='){
        console.log()
       arrayNumbers =arrayNumbers.join("")
        console.log(eval(arrayNumbers))
    
    }else if(num=="reset"){
        let arrayNumbers=[]
    }
    else{
        arrayNumbers.push(num);  
        console.log(num)
    }


  return arrayNumbers
}












//     let arr = []
// function my_f(sign){
//   if(sign==="="){
//     console.log(arr);
//     let str = arr.join('');
//     console.log(str);
//     let calc = eval(str);
//     console.log(calc);
//   }
//   else if(sign==='reset'){
//     arr = []
//   }
//   else{
//     arr.push(sign)
//   }

// }
// my_f(6);
// my_f(6);
// my_f("+");
// my_f(3);
// my_f("+");
// my_f(10);