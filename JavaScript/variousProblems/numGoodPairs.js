// source: https://leetcode.com/problems/number-of-good-pairs/

const nums = [1, 2, 3, 1, 1, 3];

function numIdenticalPairs(nums) {
  let count = 0;

  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] == nums[j] && i < j) {
        count++;
      }
    }
  }

  return count++;
}

console.log(numIdenticalPairs(nums));
