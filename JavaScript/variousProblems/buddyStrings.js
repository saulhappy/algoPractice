// source: https://leetcode.com/problems/buddy-strings/

// Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

// Example 1:

// Input: A = "ab", B = "ba"
// Output: true

const A = "ab";
const B = "ba";

function buddyStrings(A, B) {
  let validSwaps = 0;

  for (let i = 0; i < A.length; i++) {
    if (A[i] != B[i]) {
      if (A[i] === B[i + 1] && A[i + 1] === B[i]) {
        validSwaps++;
      }
    }
  }
  return validSwaps === 1;
}

console.log(buddyStrings(A, B));
