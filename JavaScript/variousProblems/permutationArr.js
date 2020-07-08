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
  if (nums.length === 0) return [];
  if (nums.length === 1) return nums[0];

  let result = [];

  for (let i = 0; i < nums.length; i++) {
    const currentNum = nums[i];
    const remainingNums = nums.slice(0, i).concat(nums.slice(i + 1));
    debugger;

    for (let j = 0; j < remainingNums.length; j++) {
      result.push(currentNum, ...permute(remainingNums)[j]);
    }
  }
  return result;
}

console.log(permute(nums));
