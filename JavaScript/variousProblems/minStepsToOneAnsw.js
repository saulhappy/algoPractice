// You're provided an integer between 1 and 100,000,000. Write a function that returns the minimum
// steps to reach one, by either subtracting 1, dividing by 2, or dividing by 3.
// Example: input: 4 => 2: 4 / 2 = 2, 2 / 2 = 1.
// 10 => 3: 10 - 1 = 9, 9 / 3 = 3, 3 / 3 = 1.

// RECURSIVE SOLUTION

function minStepsToOne(n) {
  function traverse(current) {
    if (current === 1) {
      return 0;
    }

    // subtract 1
    let option = traverse(current - 1);

    // divide by 3
    if (current % 3 === 0) {
      let divide3 = traverse(current / 3);
      option = Math.min(option, divide3);
    }

    // divide by 2
    if (current % 2 === 0) {
      let divide2 = traverse(current / 2);
      option = Math.min(option, divide2);
    }

    return option + 1;
  }

  return traverse(n);
}

console.time("RECURSION :");
console.log(minStepsToOne(100));
console.timeEnd("RECURSION :");

console.time("RECURSION :");
console.log(minStepsToOne(200));
console.timeEnd("RECURSION :");

console.time("RECURSION :");
console.log(minStepsToOne(300));
console.timeEnd("RECURSION :");

console.time("RECURSION :");
console.log(minStepsToOne(400));
console.timeEnd("RECURSION :");

// MEMOIZED RECURSIVE SOLUTION

function minStepsToOne(n) {
  function traverse(current) {
    if (current === 1) {
      return 0;
    }

    // subtract 1
    let option = traverse(current - 1);

    // divide by 3
    if (current % 3 === 0) {
      let divide3 = traverse(current / 3);
      option = Math.min(option, divide3);
    }

    // divide by 2
    if (current % 2 === 0) {
      let divide2 = traverse(current / 2);
      option = Math.min(option, divide2);
    }

    return option + 1;
  }

  return traverse(n);
}

// 1) Create cache
// 2) Check cache
// 3) Write to cache

function minStepsToOneMemo(n) {
  const cache = {};
  function traverse(current) {
    if (current in cache) {
      return cache[current];
    }
    if (current === 1) {
      return 0;
    }

    // subtract 1
    let option = traverse(current - 1);

    // divide by 3
    if (current % 3 === 0) {
      let divide3 = traverse(current / 3);
      option = Math.min(option, divide3);
    }

    // divide by 2
    if (current % 2 === 0) {
      let divide2 = traverse(current / 2);
      option = Math.min(option, divide2);
    }

    cache[current] = option + 1;
    return option + 1;
  }

  return traverse(n);
}

function minStepsToOneTab(n) {
  const table = new Array(n + 1);
  table[1] = 0;

  for (let i = 2; i < table.length; i++) {
    // subtract 1
    let option = table[i - 1];

    // divide by 3
    if (i % 3 === 0) {
      let divide3 = table[i / 3];
      option = Math.min(option, divide3);
    }

    // divide by 2
    if (i % 2 === 0) {
      let divide2 = table[i / 2];
      option = Math.min(option, divide2);
    }

    table[i] = option + 1;
  }

  return table[n];
}

// testing time
console.time("RECURSION :");
console.log(minStepsToOne(300));
console.timeEnd("RECURSION :");

console.time("MEMOIZATION :");
console.log(minStepsToOneMemo(300));
console.timeEnd("MEMOIZATION :");

console.time("TABULATION :");
console.log(minStepsToOneTab(300));
console.timeEnd("TABULATION :");
