// source: https://leetcode.com/problems/consecutive-characters/

// Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

// Return the power of the string.

// Example 1:

// Input: s = "leetcode"
// Output: 2
// Explanation: The substring "ee" is of length 2 with the character 'e' only.
// Example 2:

// Input: s = "abbcccddddeeeeedcba"
// Output: 5
// Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

const s = "leetcode";

function maxPower(s) {
  let max = 0;
  let counter = 1;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === s[i + 1]) counter++;
    else {
      if (max < counter) max = counter;
      counter = 1;
    }
  }
  return max;
}

console.log(maxPower(s));
