const num = 10;

function minimumStepsToOne(num) {
  let counter = 0;

  while (num != 1) {
    if (num % 3 === 0) {
      num /= 3;
      counter++;
      minimumStepsToOne(num);
    } else if (num % 2 === 0) {
      num /= 2;
      counter++;
      minimumStepsToOne(num);
    } else {
      num--;
      counter++;
      minimumStepsToOne(num);
    }
  }
  return counter;
}

console.log(minimumStepsToOne(num));
