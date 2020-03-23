// Using your favorite language, find all numbers that occur more than once in an array of integers.
// What is a second way you might do the same problem?
// Which approach would you prefer and why?

const arr = [1, 1, 9, 3, 4, 5, 6, 6, 7, 9, 9, 9, 9];

function findDuplicates(arr) {
  const arrObj = {};
  const duplicates = [];
  for (let num of arr) {
    arrObj[num] = arrObj[num] + 1 || 1;
  }

  for (let num in arrObj) {
    if (arrObj[num] > 1) {
      duplicates.push(parseInt(num));
    }
  }
  return duplicates;
  // another approach:
  // const result = arr.filter(num => arr.indexOf(num) !== arr.lastIndexOf(num))
  // return [...new Set(result)]
}

console.log(findDuplicates(arr));
