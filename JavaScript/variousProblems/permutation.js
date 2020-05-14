// source: https://leetcode.com/problems/permutations/

// Directions:
// Given a collection of distinct integers, return all possible permutations.

// Example:

// Input: [1,2,3]
// Output:
// [
//   [1,2,3],
//   [1,3,2],
//   [2,1,3],
//   [2,3,1],
//   [3,1,2],
//   [3,2,1]
// ]

// stack overflow
const nums = [1, 2];

function permute(nums) {
  const left = 0;
  const right = nums.length - 1;

  if (left === right) {
    return nums;
  } else {
    for (let i = left; i <= right; i++) {
      swapped = swap(nums, left, i);
      return permute(swapped, left + 1, right);
    }
  }
}

function swap(arr, i, j) {
  const arrCopy = [...arr];
  const temp = arrCopy[i];
  arrCopy[i] = arrCopy[j];
  arrCopy[j] = temp;
  return arrCopy;
}

console.log(permute(nums));
