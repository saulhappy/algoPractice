// Given an array of characters ["a", "b", "b", "b", "c", "c", "a"] return a string
// that counts the number of times a character
// consecutively appears
// Example:  a1b3c2a1

// const array = ["a", "b", "b", "b", "c", "b", "c", "c", "a"];
const array = ["a", "b", "b", "b", "c", "c", "a"];

function cntConsecutiveElements(array) {
  let resultStr = "";

  for (let i = 0; i < array.length; i++) {
    let counter = 1;
    for (let j = i + 1; j < array.length; j++) {
      //   debugger;
      if (array[i] === array[j]) {
        counter++;
      }
      if (array[i] != array[j]) {
        resultStr += array[i] + counter;
        i = j;
        counter = 1;
      }

      //   break;
    }
  }

  return resultStr;
}

console.log(cntConsecutiveElements(array));
