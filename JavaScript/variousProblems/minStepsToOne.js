// You're provided an integer between 1 and 100,000,000. Write a function that returns the minimum
// steps to reach one, by either subtracting 1, dividing by 2, or dividing by 3.
// Example: input: 4 => 2: 4 / 2 = 2, 2 / 2 = 1.
// 10 => 3: 10 - 1 = 9, 9 / 3 = 3, 3 / 3 = 1.

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
