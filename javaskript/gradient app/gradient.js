
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

/* Hämtar ut vår app */
const app = document.getElementById('app-gradient')

/* Creating new elements */
const grdnt = document.createElement('div')
const grdnt__btn = document.createElement('button')
const grdnt__clr = document.createElement('div')

/* Sätter attribut och texter */
grdnt.setAttribute('class', 'grdnt')

grdnt__btn.setAttribute('class', 'grdnt__btn')
grdnt__btn.textContent = 'Create a gradient'

grdnt__clr.setAttribute('class', 'grdnt__clr')
grdnt__clr.textContent = 'linear-gradient(217deg, rgb(50,112,241), rgb(89,197,98)'

/* Lägga till elemeneten på sidan */
app.appendChild(grdnt)
grdnt.appendChild(grdnt__btn)
grdnt.appendChild(grdnt__clr)

/* Eventlistner to get a new quote */
grdnt__btn.addEventListener('click', () => {

    const c1 = randomcolor()
    const c2 = randomcolor()
    const deg = randomNumber(360)
    const lg = "linear-gradient("+ deg +"deg," + c1 + ", " + c2 + ")"

    console.log(lg);

    grdnt__clr.textContent = lg
    app.style.backgroundImage = lg
})