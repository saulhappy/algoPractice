// Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

// Return the array in the form [x1,y1,x2,y2,...,xn,yn].
// Example:
// Input: nums = [2,5,1,3,4,7], n = 3
// Output: [2,3,5,4,1,7]
// Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

const nums = [2, 5, 1, 3, 4, 7];
const n = 3;

function arrShuffle(nums, n) {
  let arr1 = nums.slice(0, n);
  let arr2 = nums.slice(n);
  let result = [];

  while (arr1.length > 0 && arr2.length > 0) {
    result.push(arr1.shift());
    result.push(arr2.shift());
  }
  return result;
}

console.log(arrShuffle(nums, n));
