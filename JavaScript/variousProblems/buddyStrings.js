// source: https://leetcode.com/problems/buddy-strings/

// Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

// Example 1:

// Input: A = "ab", B = "ba"
// Output: true

const A = "abab";
const B = "abab";
// true

function buddyStrings(A, B) {
  let validSwaps = 0;
  let isSame = true;

  let arrA = A.split("");
  let arrB = B.split("");

  const isSameChar = (currentChar) => currentChar === A[0];

  if (A.length != B.length) return false;
  if (A.length === 0 && B.length === 0) return false;

  isSame = arrA.every(isSameChar);
  isSame = arrB.every(isSameChar);

  if (isSame === true) return true;

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
