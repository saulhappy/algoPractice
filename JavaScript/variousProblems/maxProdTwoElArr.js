// source: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

// Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

// Example 1:

// Input: nums = [3,4,5,2]
// Output: 12
// Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
// Example 2:

// Input: nums = [1,5,4,5]
// Output: 16
// Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
// Example 3:

// Input: nums = [3,7]
// Output: 12

const nums = [3, 7];

function maxProduct(nums) {
  const sorted = nums.sort((a, b) => a - b);
  const max = sorted[sorted.length - 1];
  const secondMax = sorted[sorted.length - 2];
  return (max - 1) * (secondMax - 1);
}

console.log(maxProduct(nums));
