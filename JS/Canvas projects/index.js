class Timer {
  constructor(durationInput, startButton, pauseButton) {
    this.durationInput = durationInput;
    this.startButton = startButton;
    this.pauseButton = pauseButton;
    this.intervalId = null;
    this.startButton.addEventListener("click", this.start);
    this.pauseButton.addEventListener("click", this.pause);
  }

  start = () => {
    if (typeof this.intervalId !== "number") {
      this.intervalId = setInterval(this.tick, 1000);
    }
  };

  tick = () => {
    if (this.timeRemaining < 1) {
      this.pause();
    }
    // calling the getter method
    else {
      const getTime = this.timeRemaining;
      // the following code will call the setter like following
      // timeRemaining( const timeRemaining - 1)
      this.timeRemaining = getTime - 1;
    }
  };

  pause = () => {
    clearInterval(this.intervalId);
  };

  get timeRemaining() {
    return parseFloat(this.durationInput.value);
  }

  set timeRemaining(time) {
    this.durationInput.value = time;
  }
}

const durationInput = document.querySelector("#duration");
const startButton = document.querySelector("#start");
const pauseButton = document.querySelector("#pause");

const timer = new Timer(durationInput, startButton, pauseButton);
