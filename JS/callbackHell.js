const btn = document.querySelector("button");

setTimeout(() => {
  btn.style.transform = `translateX(1000px)`;

  setTimeout(() => {
    btn.style.transform = `translateX(200px)`;

    setTimeout(() => {
      btn.style.transform = `translateX(300px)`;

      setTimeout(() => {
        btn.style.transform = `translateX(400px)`;

        setTimeout(() => {
          btn.style.transform = `translateX(500px)`;
        }, 1000);
      }, 1000);
    }, 1000);
  }, 3000);
}, 5000);

const moveX = (element, amount, delay) => {
  setTimeout(() => {
    element.style.transform = `translate(${amount}px)`;
  }, delay);
};
