// source: https://leetcode.com/problems/shortest-distance-to-a-character/

// Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

// Example 1:

// Input: S = "loveleetcode", C = 'e'
// Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

const S = "loveleetcode";
const C = "e";

function shortestToChar(S, C) {
  let cIndices = [];
  let result = [];

  for (let i = 0; i < S.length; i++) {
    if (S[i] === C) {
      cIndices.push(i);
    }
  }

  for (let j = 0; j < S.length; j++) {
    debugger;
    result.push(Math.min(Math.abs(j)));
  }
  debugger;
  return result;
}

console.log(shortestToChar(S, C));
