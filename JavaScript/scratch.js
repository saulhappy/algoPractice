const arr = [1, 1, 2, 2, 2];

function longestFlat(arr) {
  let maxCounter = 0;
  counter = 1;

  for (let i = 0; i < arr.length; i++) {
    // debugger;
    if (arr[i] === arr[i + 1]) {
      counter++;
    } else {
      maxCounter = counter;
      i++;
    }
  }
  return maxCounter;
}

console.log(longestFlat(arr));
