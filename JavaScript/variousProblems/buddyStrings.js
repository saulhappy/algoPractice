// source: https://leetcode.com/problems/buddy-strings/

// Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

// Example 1:

// Input: A = "ab", B = "ba"
// Output: true

const A = "";
const B = "aa";

function buddyStrings(A, B) {
  return A.split("").sort().join("") === B.split("").sort().join("");
}

console.log(buddyStrings(A, B));
