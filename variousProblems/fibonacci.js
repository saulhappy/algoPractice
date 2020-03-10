const n = 6;

function fib(n) {
  let result = 0;
  if (n <= 2) {
    result = n;
    console.log(result);
    return;
  }
  result = fib(n - 1) + fib(n - 2);
  console.log(result);
  return;
}

fib(n);
