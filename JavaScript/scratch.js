let array = [1, 2, 3];

function test(arr) {
  let result = [];

  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      result.push(`(${i}, ${j})`);
    }
  }

  return result;
}

console.log(test(array).length);
