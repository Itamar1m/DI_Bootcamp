let num = prompt('How many bottles of beer are on the wall?')
num = Number(num)
let increment = 1
function bottlesOfBeer() {
    for (i = 0; i <= Infinity; i++)
        if (increment + i == 1) {
            let loop1 = `${num+i} bottles of beer on the wall ${num+i}  bottles of beer take ${increment+i} down, pass it around`
            console.log(loop1);
            continue;
        } else if (num + i > 250) {
        console.log('too much beer')
        break;
    } else {
        console.log(`${num+i} bottles of beer on the wall ${num+i}  bottles of beer take ${increment+i} down, pass them around`)
    }
}
bottlesOfBeer()


