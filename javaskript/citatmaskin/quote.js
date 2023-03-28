'use strict'

const quotes = [
    {
        quote: 'Kanoners!',
        name: 'Pelle'
    },
    {
        quote: 'Hoppsan!',
        name: 'Kalle'
    },
    {
        quote: 'Tjenixen!',
        name: 'Lelle'
    },
    {
        quote: 'Bomber å granater!',
        name: 'Kapten Haddock'
    },
    {
        quote: 'Se upp!',
        name: 'Olle'
    }
]

/* Get placeholder for the quote */
const quoteHolder = document.getElementById('quoteholder')

/* Creating new elements */
const quote = document.createElement('blockquote')
const quoteText = document.createElement('p')
const quoteName = document.createElement('p')
const quoteButton = document.createElement('button')

/* Setting attributes and text */
quote.setAttribute('class', 'quote')
quoteButton.setAttribute('class', 'update')
quoteButton.textContent = 'Slumpa citat'

/* Appendning elements */
quoteHolder.appendChild(quote)
quote.appendChild(quoteText)
quote.appendChild(quoteName)
quoteHolder.appendChild(quoteButton)

/* Set random quote at load */
const randomNumber = Math.floor(Math.random() * quotes.length)
quoteText.textContent = quotes[randomNumber].quote
quoteName.textContent = quotes[randomNumber].name

'use strict'

/* Function to get a new random quote */
function getQuote() {
    const randomNumber = Math.floor(Math.random() * quotes.length)

    return {
        quote: quotes[randomNumber].quote,
        name: quotes[randomNumber].name,
    }
}

/* Eventlistner to get a new quote */
quoteButton.addEventListener('click', () => {
    const x = getQuote()
    quoteText.textContent = x.quote
    quoteName.textContent = x.name
})