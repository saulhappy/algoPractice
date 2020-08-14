// RECURSION WITH MEMOIZATION

let memo = {};

function minStepsToOneRecursionMemo(n) {
  if (n === 1) {
    return 0;
  }

  if (memo[n]) {
    return memo[n];
  }

  let result = minStepsToOneRecursionMemo(n - 1);

  if (n % 2 === 0) {
    result = Math.min(result, minStepsToOneRecursionMemo(n / 2));
  }

  if (n % 3 === 0) {
    result = Math.min(result, minStepsToOneRecursionMemo(n / 3));
  }

  memo[n] = result + 1;
  return result + 1;
}

console.time("RECURSION WITH MEMOIZATION:");
console.log(minStepsToOneRecursionMemo(800));
console.timeEnd("RECURSION WITH MEMOIZATION:");
