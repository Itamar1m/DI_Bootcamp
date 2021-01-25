let planets = ['Earth', 'Jupiter', 'Mars', 'Neptune', 'Saturn', 'Venus', 'Uranus', 'Mercury']
let colors = ['red', 'blue', 'green', 'yellow', 'pink', 'white', 'orange', 'purple']
let moons=[1, 79, 0, 0, 2, 62, 27, 14];


for (i = 0; i <= planets.length - 1; i++) {
    // Planets
    let circle = document.createElement('div')
    //toLowercase--- because classes should be lower case.
    circle.classList.add(planets[i].toLowerCase(), 'planet')
    circle.style.backgroundColor = colors[i]
    circle.style.margin = '30px'
    let name = document.createTextNode(planets[i])
    circle.appendChild(name)
    document.body.appendChild(circle)

}