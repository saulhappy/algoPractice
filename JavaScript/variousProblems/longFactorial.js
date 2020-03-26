// source: https://www.hackerrank.com/challenges/extra-long-factorials/problem

const n = 25;
// result = 15511210043330985984000000; 25x24x23x22...1

function extraLongFactorials(n) {
  let result = n;
  if (n === 0 || n === 1) return 1;
  while (n > 1) {
    n--;
    result *= n;
  }
  return result;
}

console.log(extraLongFactorials(n));
