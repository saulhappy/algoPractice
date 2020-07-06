// source: tripleByte quiz
// find the longest consecutive count of elements in an array
// egs: [1, 1, 2] -> 2; [3, 3, 3, 3] -> 4; [2, 2, 2, 3, 4, 3, 3] -> 3

const arr = [1, 1, 2];

function longestFlat(arr) {
  let maxCounter = 0;
  let counter = 1;

  for (let i = 0; i < arr.length; i++) {
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
