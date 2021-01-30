//sidenav
const sideNav = document.querySelector('.sidenav');
M.Sidenav.init(sideNav, {});

//slider
const slider = document.querySelector(".slider");
M.Slider.init(slider, {
    indicators: false,
    height: 500,
    transition: 500,
    interval: 6000
});

// autocomplete
const ac = document.querySelector('.autocomplete');
M.Autocomplete.init(ac, {
    data: {
        "HTML": null,
        "CSS": null,
        "JAVASCRIPT": null,
        "DOM": null,
        "PYTHON": null,
        "GITHUB": null,
        "JSON": null,
        "APIs": null,
        "WEB SERVERS": null,
        "FLASK FRAMEWORK": null,
        "DJANGO": null,
        "SQL": null,
        "HEROKU": null,
        "AWS": null,
        "DEVELOPERS INSTITUTE": null,
        "DONALD TRUMP CAN SUCK IT": null,
        "WHATEVER YOU WANT": null
    }
});

// Material Boxed
const mb = document.querySelectorAll('.materialboxed');
M.Materialbox.init(mb, {});

//scrollspy
const ss = document.querySelectorAll('.scrollspy');
M.ScrollSpy.init(ss, {});

// Search and Blog input

// Fade-In
window.onload = function () {
    window.setTimeout(fadein, 1500); //8 seconds
};
function fadein() {
    document.getElementById('fadeIn').style.opacity = '1';
}
let buttonYes = document.getElementById('btnYes');
let buttonNo = document.getElementById('btnNo');
buttonYes.addEventListener("click", welcome);
buttonNo.addEventListener("click", goodBye);
let msg = document.getElementById('fadeIn');
function goodBye() {
    msg.innerText = 'Maybe it is time to reconsider joining Devlopers Institute';
    setTimeout(clearWelcome, 2000);
}
function welcome() {
    msg.innerText = 'Share your ideas with us';
}
function clearWelcome() {
    msg.style.opacity = '0';
}

// Clear button for text input field

let clearAllButton = document.querySelector('.btn-clear');
clearAllButton.addEventListener('click', clear);

let inputHeadline = document.querySelector(".form-control-headline");
let inputText = document.querySelector(".form-control-text");

function clear() {

    inputHeadline.value = "";
    inputText.value = "";
}

// Create new Blog card

let rowCards;
let divColumn;
let divPanel;
let cardTitle;
let cardText;

function createCard () {
    rowCards = document.querySelector('.row-cards');

    divColumn = document.createElement('div');
    divPanel = document.createElement('div');
    cardTitle = document.createElement('h4');
    cardText = document.createElement('p');

    divColumn.classList.add('col', 's12', 'm6');
    divPanel.classList.add('card-panel', 'blog-panel');
    cardTitle.classList.add('card-title');
    cardText.classList.add('card-text');

    divPanel.appendChild(cardTitle);
    divPanel.appendChild(cardText);
    divColumn.appendChild(divPanel);
    rowCards.appendChild(divColumn);
}

// Submit the post

let submitButton = document.querySelector(".btn-submit");

submitButton.addEventListener("click", addContent);

function addContent () {

    let headlineField = document.querySelector(".form-control-headline").value;
    let textField = document.querySelector(".form-control-text").value;

    if (inputHeadline.value == "" || inputText.value == "") {
        alert("Text fields can't be empty");
        return; // checks for empty input and leaves the function if empty
    } else {
        createCard();

        let headline = document.createTextNode(headlineField);
        cardTitle.appendChild(headline);
    
        let text = document.createTextNode(textField);
        cardText.appendChild(text);
    
        clear(); // clears the text fields after submitting
    }
}