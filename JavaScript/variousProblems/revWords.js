// source: https://leetcode.com/problems/reverse-words-in-a-string/
// Example 1:

// Input: "the sky is blue"
// Output: "blue is sky the"
// Example 2:

// Input: "  hello world!  "
// Output: "world! hello"
// Explanation: Your reversed string should not contain leading or trailing spaces.
// Example 3:

// Input: "a good   example"
// Output: "example good a"
// Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

// Note:

// A word is defined as a sequence of non-space characters.
// Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
// You need to reduce multiple spaces between two words to a single space in the reversed string.

const s = "a good   example";

function reverseWords(s) {
  let arr = s.trim().split(" ");
  let l = arr.length;
  let revArr = [];

  for (let i = 0; i < l; i++) {
    revArr.push(arr.pop());
  }

  let revString = revArr.join(" ");
  return revString.replace(/\s\s+/g, " ");
}

console.log(reverseWords(s));
