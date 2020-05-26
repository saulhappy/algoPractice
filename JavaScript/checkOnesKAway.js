const nums = [1, 0, 0, 1, 0, 1];
const k = 2;

function checkOnes(nums, k) {
  let onesPositions = [];
  let results = [];

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 1) {
      onesPositions.push(i);
    }
  }

  // check first vs last position

  const largestDistance =
    Math.abs(onesPositions[0] - onesPositions[onesPositions.length - 1]) - 1;

  // check everything in between
  for (let i = 0; i < onesPositions.length - 1; i++) {
    let currentDistance = Math.abs(onesPositions[i] - onesPositions[i + 1]) - 1;

    if (largestDistance && currentDistance >= k) {
      results.push(true);
    } else {
      results.push(false);
    }
  }

  results.every((val, i, arr) => val === arr[0]);
}

console.log(checkOnes(nums, k));

// [1,1,1,1].every( (val, i, arr) => val === arr[0] )   // true
