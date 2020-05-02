// source: https://leetcode.com/problems/find-lucky-integer-in-an-array/

const arr = [
  5,
  8,
  10,
  9,
  8,
  10,
  9,
  6,
  6,
  7,
  10,
  8,
  10,
  10,
  9,
  4,
  6,
  2,
  10,
  3,
  5,
  10,
  2,
  6,
  4,
  8,
  7,
  3,
  9,
  9,
  5,
  7,
  8,
  7,
  11,
  9,
  3,
  1,
  5,
  11,
  9,
  5,
  8,
  10,
  8,
  4,
  9,
  7,
  6,
  7,
  10,
  9,
  7,
  8,
  6,
  10,
  4,
];

function findLucky(arr) {
  let arrMap = {};
  let luckies = [];

  for (let num of arr) {
    arrMap[num] = arrMap[num] + 1 || 1;
  }

  for (let num in arrMap) {
    if (parseInt(num) === arrMap[num]) {
      luckies.push(parseInt(num));
    }
  }

  if (luckies.length > 0) {
    return luckies.sort((a, b) => a - b).pop();
  } else {
    return -1;
  }
}

console.log(findLucky(arr));
