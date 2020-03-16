// Source: https://www.hackerrank.com/challenges/camelcase/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

// count words in camelCase string s

function camelcase(s) {
  let counter = 1;
  for (let char of s) {
    if (char === char.toUpperCase()) {
      counter++;
    }
  }
  return counter;
}

console.log(camelcase(s));
