// TABULATED SOLUTION

function minStepsToOneTab(n) {
  let table = new Array(n + 1).fill(n);
  table[0] = 0;
  table[1] = 0;

  for (let i = 1; i < n; i++) {
    table[i + 1] = Math.min(table[i + 1], table[i] + 1);

    if (i * 2 <= n) {
      table[i * 2] = Math.min(table[i] + 1, table[i * 2]);
    }

    if (i * 3 <= n) {
      table[i * 3] = Math.min(table[i] + 1, table[i * 3]);
    }
  }

  return table[n];
}

console.time("RECURSION WITH TABULATION:");
console.log(minStepsToOneTab(20000000));
console.timeEnd("RECURSION WITH TABULATION:");
