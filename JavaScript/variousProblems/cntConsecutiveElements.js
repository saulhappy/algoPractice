// Given an array of characters ["a", "b", "b", "b", "c", "c", "a"] return a string
// that counts the number of each consecutive letter non-uniquely.
// Example:  a1b3c2a1

const array = ["z", "z", "z", "a", "z", "b", "b", "b", "c", "c", "a"];

function cntConsecutiveElements(array) {
  let result = "";
  let counter = 1;

  for (let i = 0; i < array.length; i++) {
    if (array[i] === array[i + 1]) {
      counter++;
    } else {
      result += array[i] + counter;
      counter = 1;
    }
  }
  return result;
}

console.log(cntConsecutiveElements(array));
