// NON-WORKING SOLUTION

// Directions
// Write an algorithm to determine if a number is "happy".
// A happy number is a number defined by the following process:
// Starting with any positive integer, replace the number by the sum of the squares of its digits,
// and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
// Those numbers for which this process ends in 1 are happy numbers.
// Example:
// Input: 19
// Output: true
// Explanation:
// 1^2 + 9^2 = 82
// 8^2 + 2^2 = 68
// 6^2 + 8^2 = 100
// 1^2 + 0^2 + 0^2 = 1

const n = 2;
function isHappy(n) {
  let nStr = n.toString();
  let nArr = [...nStr];
  let sqrArr = [];

  for (let i = 0; i < nArr.length; i++) {
    sqrArr.push(squareN(nArr[i]));
  }

  if (checkSum(sqrArr) === 1 || checkSum(sqrArr) === 7) {
    return true;
  }
  return isHappy(checkSum(sqrArr));
}

function squareN(n) {
  return n * n;
}
function checkSum(sqrArr) {
  return sqrArr.reduce((a, b) => a + b, 0);
}

console.log(isHappy(n));
