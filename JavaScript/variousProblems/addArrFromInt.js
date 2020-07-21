// source: https://leetcode.com/problems/add-to-array-form-of-integer/

// For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

// Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

// Example 1:

// Input: A = [1,2,0,0], K = 34
// Output: [1,2,3,4]
// Explanation: 1200 + 34 = 1234

// Example 2: A = [1,2,6,3,0,7,1,7,1,9,7,5,6,6,4,4,0,0,6,3], K = 516
// Output: [1,2,6,3,0,7,1,7,1,9,7,5,6,6,4,4,0,0,0,0]

const A = [1, 2, 6, 3, 0, 7, 1, 7, 1, 9, 7, 5, 6, 6, 4, 4, 0, 0, 6, 3];
const K = 34;

function addToArrayForm(A, K) {
  let AStr = "";
  let sum = 0;
  let result = [];

  for (let i = 0; i < A.length; i++) {
    AStr += A[i];
  }

  sum = BigInt(AStr) + BigInt(K);

  sum = sum.toString();

  for (let i = 0; i < sum.length; i++) {
    result.push(Number(sum[i]));
  }

  return result;
}

console.log(addToArrayForm(A, K));
