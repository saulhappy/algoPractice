// find the second largest element of an array
// example: arr = [1, 2, 3, 3, 2, 4, 5, 5, 1] => 4.

const arr = [1, 2, 3, 3, 2, 4, 5, 5, 1];

function findSecondLargest(arr) {
  const distinct = [...new Set(arr)];
  const maxNum = Math.max(...distinct);
  const filteredMaxOut = distinct.filter((num) => num < maxNum);
  const secondMax = Math.max(...filteredMaxOut);
  return secondMax;
}

console.log(findSecondLargest(arr));
