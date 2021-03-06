// simple recursion

function minStepsToOneRecursion(n) {
  if (n === 1) {
    return 0;
  }

  let result = minStepsToOneRecursion(n - 1);

  if (n % 2 === 0) {
    result = Math.min(result, minStepsToOneRecursion(n / 2));
  }

  if (n % 3 === 0) {
    result = Math.min(result, minStepsToOneRecursion(n / 3));
  }

  return result + 1;
}

console.time("RECURSION TIME:");
console.log(minStepsToOneRecursion(800));
console.timeEnd("RECURSION TIME:");
