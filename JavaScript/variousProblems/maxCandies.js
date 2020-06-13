// source: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

const candies = [4, 2, 1, 1, 2];
const extraCandies = 1;

function kidsWithCandies(candies, extraCandies) {
  let maxCandies = 0;
  let result = [];

  for (let kid of candies) {
    if (kid > maxCandies) {
      maxCandies = kid;
    }
  }

  for (let i = 0; i < candies.length; i++) {
    if (candies[i] + extraCandies >= maxCandies) {
      result.push(true);
    } else {
      result.push(false);
    }
  }
  return result;
}

console.log(kidsWithCandies(candies, extraCandies));
