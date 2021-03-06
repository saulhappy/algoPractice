// source: https://leetcode.com/problems/permutations/
// close approach: https://leetcode.com/problems/permutations/discuss/276363/JavaScript-Solution

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
  let result = [];

  if (nums.length === 0) return [];
  if (nums.length === 1) return [nums];

  for (let i = 0; i < nums.length; i++) {
    const currentNum = nums[i];
    const remainingNums = nums.slice(0, i).concat(nums.slice(i + 1));
    const remainingNumsPermuted = permute(remainingNums);

    for (let j = 0; j < remainingNumsPermuted.length; j++) {
      debugger;
      const permutedArray = [currentNum].concat(remainingNumsPermuted[j]);
      result.push(permutedArray);
    }
  }
  return result;
}

console.log(...permute(nums));
