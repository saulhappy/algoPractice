const left = [-30, 22];
const right = [0, 97];

function merge(left, right) {
  const results = [];

  while (left.length && right.length) {
    debugger;
    if (left[0] < right[0]) {
      results.push(left.shift());
    } else {
      results.push(right.shift());
    }
  }
  return [...results, ...left, ...right];
}

console.log(merge(left, right));
