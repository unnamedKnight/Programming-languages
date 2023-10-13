console.log("We are good !!!");

/* -------------------------------------------------------------------------- */
/*                                 GLOBAL NOTE                                */
/* -------------------------------------------------------------------------- */
// window is the global scope on the browser
// when we define a function like following
// function sayHi() {
//   console.log("HI");
// }
// this `sayHi` function is added as property in the `window object`
// In short any function normally refers to the `window object` in browser
// `var` declarations are added to the window object but `let` and `const` aren't

/* -------------------------------------------------------------------------- */
/*                                     END                                    */
/* -------------------------------------------------------------------------- */


/* ----------------- creating an element in the DOM ----------------- */

const ul = document.querySelector('ul')
const li = document.querySelector('li')

const newLi = document.createElement('li')
// newLi is the element that we want to insert before li
newLi.innerText = 'I am a new li'

// inserting new li before the first element in the ul
// here, newLi is what we are inserting
// and li is what we are inserting before
ul.insertBefore(newLi, li)


const test = () => console.log('just a  test')
test()
