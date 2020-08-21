// Directions
// Given a string, return true if the string is a palindrome or false if it is not.
// Palindromes are strings that form the same word if it is reversed.
// *Do* include spaces and punctuation in determining if the string is a palindrome.
// Examples:
// palindrome("abba") === true
// palindrome("abcdefg") === false

const str = "abba";

function palindrome(str) {
  let revStr = "";

  for (let i of str) {
    revStr = i + revStr;
  }

  if (revStr === str) return true;
  return false;
}

console.log(palindrome(str));
