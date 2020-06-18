// Given an array of characters ["a", "b", "b", "c", "c", "a"] return a string
// that counts the number of times a character
// consecutively appears
// Example:  a1b2c2a1

const array = ["a", "b", "b", "c", "c", "a"];

function cntConsecutiveElements(array) {
  let resultStr = "";

  for (let i = 0; i < array.length; i++) {
    let counter = 1;
    for (let j = i + 1; j < array.length; j++) {
      if (array[i] === array[j]) {
        counter++;
      }
      break;
    }

    resultStr += array[i] + counter;
  }

  return resultStr;
}
// i = 0 # a
// counter = 1
// array[0] === array[1]

// i = 1 # b
// counter = 1
// array[1] === array[2]
// array[2] === array[3]
// resultStr = a1b2
// i = 2 # b
// counter = 1
// array[3] === array[4]
// resultStr = a1b2b1

console.log(cntConsecutiveElements(array));
