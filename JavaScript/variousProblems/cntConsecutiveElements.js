// Given an array of characters return a string that counts the number of each consecutive letter.
// Example: ["a", "b", "b", "a"] should return "a1b2a1"

const array = ["a", "b", "b", "a"];

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
console.log(array[4]);
