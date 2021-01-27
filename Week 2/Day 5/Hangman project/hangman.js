let player1 = prompt('Player 1:Type in aword 8 letters or longer.')
if (player1.length < 8) {
    alert(`Your word is only player ${player1.length} letters`)
} else {
    let word = "*".repeat(player1.length)
    console.log(word)
    word = word.split('')
    let player2 = prompt('Player 2: Guess a letter')
    let wrongLetters = []
    let correctLetters = []
  
    guess()

    function guess() {
        if (player1.includes(player2) == true) {
            player1 = player1.split('')
            correct()
        } else if (wrongLetters.length <= 10 && player1.includes(player2) == false) {
            wrong()
        } else {
            console.log('You have lost all your lives......you lose!!')
        }
    }
    function correct() {
        
        for(i=0;i<=player1.length;i++){
        word.splice(player1.indexOf(player2), 1, player2)//here is my issue,this only works with one letter.
                                                                                     //getting closer....

        player1=  player1.splice (player1.indexOf(player2), 1, '-')}
         player1 = player1.join('')
        console.log(word.join(''))
        correctLetters.push(player2)
        if (word.length == correctLetters.length) {
            console.log('Well done you got it!')
        } else {
            player2 = prompt('ok next letter')
            guess()
        }
    
    }}
    function wrong() {
        wrongLetters.push(player2)
        console.log('You have guessed these letters incorrectly: ' + wrongLetters)
        player2 = prompt('wrong try again')
        guess()
    }
