// source: https://leetcode.com/problems/add-digits/

// Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

// Example:

// Input: 38
// Output: 2
// Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
//              Since 2 has only one digit, return it.

const num = 38;

// using recursion
function addDigits(num) {
  let numSplitRet = numSplit(num);
  let numSplitSumRet = numSplitSum(numSplitRet);

  // base case:
  if (numSplitSumRet < 10) return numSplitSumRet;

  // recursive case
  function numSplit(num) {
    return num.toString().split("");
  }

  function numSplitSum(arr) {
    return arr.reduce((a, b) => parseInt(a) + parseInt(b), 0);
  }

  return addDigits(numSplitSumRet);
}

console.log(addDigits(num));
