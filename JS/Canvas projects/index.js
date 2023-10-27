class Timer {
  constructor(durationInput, startButton, pauseButton, callbacks) {
    this.durationInput = durationInput;
    this.startButton = startButton;
    this.pauseButton = pauseButton;
    if (callbacks) {
      this.onStart = callbacks.onStart;
      this.onTick = callbacks.onTick;
      this.onComplete = callbacks.onComplete;
    }
    this.intervalId = 0;
    this.startButton.addEventListener("click", this.start);
    this.pauseButton.addEventListener("click", this.pause);
  }

  start = () => {
    if (this.intervalId >= 0) {
      this.intervalId = setInterval(this.tick, 50);
      if (this.onStart) this.onStart();
    }
  };

  tick = () => {
    if (this.timeRemaining < 1) {
      this.pause();
      this.onComplete()
    }
    // calling the getter method
    else {
      const getTime = this.timeRemaining;
      // the following code will call the setter like following
      // timeRemaining( const timeRemaining - 1)
      this.timeRemaining = getTime - 0.05;
      this.onTick()
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
const circle = document.querySelector('circle')

const perimeter = circle.getAttribute('r') * 2 * Math.PI
circle.setAttribute('stroke-dasharray', perimeter) 

let current_offset = 0;

const timer = new Timer(durationInput, startButton, pauseButton, {
  onStart() {
    console.log("timer started");
  },

  onTick() {
    circle.setAttribute('stroke-dashoffset', current_offset )
    current_offset = current_offset - 1
  },
  onComplete() {
    console.log("timer completed");
  },
});
