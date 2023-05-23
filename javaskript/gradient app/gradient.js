
function randomNumber(n) {
    const randomNum = Math.floor(Math.random() * n)

    return randomNum;
}

function randomcolor() {
    const r = randomNumber(255)
    const g = randomNumber(255)
    const b = randomNumber(255)
    const randomrgb = 'rgb(' + r + ', ' + g + ', ' + b + ')'
    return randomrgb;
}

var lg = ''
var last = ''
var gradients = [];

function gradient() {
    const c1 = randomcolor()
    const c2 = randomcolor()
    const deg = randomNumber(360)
    // last = lg
    lg = "linear-gradient(" + deg + "deg," + c1 + ", " + c2 + ")"

    return lg;
}


/* Hämtar ut vår app */
const app = document.getElementById('app-gradient')

/* skapa nya element */
const grdnt = document.createElement('div')
const grdnt__btn = document.createElement('button')
const grdnt__clr = document.createElement('div')
const förra = document.createElement("button")

/* Sätter attribut och texter */
grdnt.setAttribute('class', 'grdnt')

grdnt__btn.setAttribute('class', 'grdnt__btn')
grdnt__btn.textContent = 'Create a gradient'

grdnt__clr.setAttribute('class', 'grdnt__clr')

förra.setAttribute("class", "förra")
förra.textContent = "last gradient"


/* Lägga till elemeneten på sidan */
app.appendChild(grdnt)
grdnt.appendChild(grdnt__btn)
grdnt.appendChild(grdnt__clr)
app.appendChild(förra)


/* nu gradient om sidan uppdateras */
gradient()
gradients.push(lg);
gradient()
gradients.push(lg);
app.style.backgroundImage = lg
grdnt__clr.textContent = lg
förra.style.backgroundImage = lg
last = lg

/* Eventlistner för att få ny gradient */
grdnt__btn.addEventListener('click', () => {

    last = lg

    gradient()
    gradients.push(lg);
    gradients.shift()
    console.log(gradients)
    console.log(gradients.length)

    grdnt__clr.textContent = lg
    app.style.backgroundImage = lg
    förra.style.backgroundImage = last
})



förra.addEventListener("click", () => {
    last = lg
    lg = gradients.pop(1)
    gradients.unshift(lg)
    
    app.style.backgroundImage = lg;
    grdnt__clr.textContent = lg;
    förra.style.backgroundImage = last;
    
})