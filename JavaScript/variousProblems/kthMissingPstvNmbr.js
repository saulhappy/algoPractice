// source: https://leetcode.com/problems/kth-missing-positive-number/

// Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

// Find the kth positive integer that is missing from this array.

// Input: arr = [2,3,4,7,11], k = 5
// Output: 9
// Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

const arr = [1, 2, 3, 4];
const k = 2;
// 2

function findKthPositive(arr, k) {
  let missingCounter = 0;

  for (let i = 1; missingCounter != k; i++) {
    if (!arr.includes(i)) missingCounter++;
    if (missingCounter === k) return i;
  }
}

console.log(findKthPositive(arr, k));
