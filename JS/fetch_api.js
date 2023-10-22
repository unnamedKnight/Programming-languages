/* Promise.all() takes an array of promises
we can use Promise.all() to resolve promise in parallel but not sequentially
*/

function changeColor(element, color) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      element.style.backgroundColor = color;
      resolve();
    }, 1000);
    //     console.log('Changing color');
    //     element.style.backgroundColor = color;
    //     console.log('Done changing color');
    //     resolve();
  });
}

const btn = document.querySelector("button");
async function changeButtonColor(element) {
  /* ----------------- resolving promise sequentially ---------------- */
  //   await changeColor(element, "blue");
  //   await changeColor(element, "yellow");
  //   await changeColor(element, "red");
  //   await changeColor(element, "green");

  /* ----------------- resolving promise in parallel---------------- */

  //   const test1 = changeColor(element, "blue");
  //   const test2 = changeColor(element, "yellow");
  //   const test3 = changeColor(element, "red");
  //   const test4 = changeColor(element, "green");
  //   await test1
  //   await test2
  //   await test3
  //   await test4

  //  we can do the above operation with Promise.all()
  await Promise.all([
    changeColor(element, "blue"),
    changeColor(element, "yellow"),
    changeColor(element, "red"),
    changeColor(element, "green"),
  ]);
}

changeButtonColor(btn);
