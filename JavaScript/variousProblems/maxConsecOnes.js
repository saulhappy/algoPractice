// source:  https://leetcode.com/problems/max-consecutive-ones/

// Given a binary array, find the maximum number of consecutive 1s in this array.

// Example 1:
// Input: [1,1,0,1,1,1]
// Output: 3
// Explanation: The first two digits or the last three digits are consecutive 1s.
//     The maximum number of consecutive 1s is 3.

const nums = [1, 1, 0, 1, 1, 1];

function findMaxConsecutiveOnes(nums) {
  const isZero = (currentValue) => currentValue === 0;

  if (nums.every(isZero)) return 0;
  else {
    let max = 0;
    let counter = 1;

    for (let i = 0; i < nums.length; i++) {
      if (nums[i] === 1 && nums[i + 1] === 1) counter++;
      else {
        if (max < counter) max = counter;
        counter = 1;
      }
    }
    return max;
  }
}

console.log(findMaxConsecutiveOnes(nums));
