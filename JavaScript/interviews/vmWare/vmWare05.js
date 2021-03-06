// return an array of n integer including the givne (0, 1) of fibonnacci seq

const n = 4;

function fib(n) {
  let result = [0, 1];

  for (let i = 2; i <= n; i++) {
    const a = result[i - 1];
    const b = result[i - 2];
    result.push(a + b);
  }
  return result.slice(0, n);
}

console.log(fib(n));
