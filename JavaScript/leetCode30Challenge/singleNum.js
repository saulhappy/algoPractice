// Given a non-empty array of integers, every element appears twice except for one. Find that single one.

// Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

// Example 1
// Input: [2,2,1]
// Output: 1

// Example 2
// Input: [4,1,2,1,2]
// Output: 4

const nums = [2, 2, 1];

function singleNum(nums) {
  let numsMap = {};

  for (let element of nums) {
    numsMap[element] = numsMap[element] + 1 || 1;
  }
  return Object.keys(numsMap).find(key => numsMap[key] === 1);
}

console.log(singleNum(nums));
