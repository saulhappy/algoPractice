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

// testing time
console.time("RECURSION :");
console.log(minStepsToOne(300));
console.timeEnd("RECURSION :");

console.time("MEMOIZATION :");
console.log(minStepsToOneMemo(300));
console.timeEnd("MEMOIZATION :");
