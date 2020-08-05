// source: https://leetcode.com/problems/length-of-last-word/

// Share
// Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

// If the last word does not exist, return 0.

// Note: A word is defined as a maximal substring consisting of non-space characters only.

// Example:

// Input: "Hello World"
// Output: 5

const s = "This is a Leetcode problem explanation  ";

function lengthOfLastWord(s) {
  let newInput = s.trim();
  let sArr = newInput.split("");
  let counter = 0;

  console.log(sArr);

  if (newInput.length === 0) return counter;

  if (!sArr.includes(" ")) return newInput.length;

  for (let i = newInput.length - 1; i > 0; i--) {
    if (newInput[i] != " ") {
      counter++;
    } else {
      return counter;
    }
  }
}

console.log(lengthOfLastWord(s));
