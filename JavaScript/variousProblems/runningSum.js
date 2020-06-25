// source: https://leetcode.com/problems/running-sum-of-1d-array/

// Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

// Return the running sum of nums.

// Input: nums = [1,2,3,4]
// Output: [1,3,6,10]
// Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

const nums = [1, 2, 3, 4];

function runningSum(nums) {
  let result = [];

  for (let i = 0; i < nums.length; i++) {
    if (i === 0) {
      result.push(nums[i]);
    } else {
      result.push(result[i - 1] + nums[i]);
    }
  }
  return result;
}

console.log(runningSum(nums));
