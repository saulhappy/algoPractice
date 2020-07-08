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

const nums = [1, 2, 3];

function permute(nums) {
  if (nums.length === 1) return nums;

  let result = [];

  for (let i = 0; i < nums.length; i++) {
    let numsCopy = [...nums];

    const currentNum = nums[i];
    const remainingNums = numsCopy.slice(0, i).concat(numsCopy.slice(i + 1));
    debugger;

    for (let j = 0; j < remainingNums.length; j++) {
      result.push(currentNum + permute(remainingNums)[j]);
    }
  }
}

console.log(permute(nums));
