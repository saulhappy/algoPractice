// TABULATED SOLUTION

function minStepsToOneTab(n) {
  let table = [-1, 0];

  for (let i = 2; i < n; i++) {
    table[i] = Math.min(table[i + 1], table[i] + 1);
  }

  if (i * 2 <= n) {
    table[i] = Math.min(table[i + 1], table[i * 2]);
  }

  if (i * 3 <= n) {
    table[i * 3] = Math.min(table[i + 1], table[i * 3]);
  }

  return table[n];
}

console.log(minStepsToOneTab(10));
