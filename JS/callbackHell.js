const btn = document.querySelector("button");

const promiseADog = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const num = Math.random();
      const value = 5;
      if (num > 0.1) {
        resolve(value);
      } else {
        reject();
      }
    }, 1000);
  });
};

// chaining Promises
promiseADog()
  .then((value) => {
    console.log(value);
    return promiseADog();
  })
  .then((value) => {
    console.log(value);
    return promiseADog();
  })
  .then((value) => {
    console.log(value);
    return promiseADog();
  })
  .then((value) => {
    console.log(value);
  })
  .catch(() => console.log("There is an error"));
