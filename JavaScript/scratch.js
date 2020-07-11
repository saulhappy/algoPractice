const l = 2;
const r = 5;

function printNums(l, r) {
  results = [];

  for (let i = l; i < r + 1; i++) {
    if (i % 2 != 0) {
      results.push(i);
    }
  }

  return results;
}

console.log(printNums(l, r));
