const num = 11;

function minimumStepsToOne(num) {
  let counter = 0;

  while (num != 1) {
    debugger;
    if (num % 3 === 0) {
      num /= 3;
      minimumStepsToOne(num);
      counter++;
    } else if (num % 2 === 0) {
      num /= 2;
      minimumStepsToOne(num);
      counter++;
    } else {
      num--;
      minimumStepsToOne(num);
      counter++;
    }
  }

  return counter;
}

console.log(minimumStepsToOne(num));
