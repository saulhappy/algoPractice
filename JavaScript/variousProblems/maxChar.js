// Max Character
// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
// maxChar("abcccccccd") === "c"
// maxChar("apple 1231111") === "1”

const str = "aabbbbccdddddddd";

function maxChar(str) {
  let charsObj = {};
  let maxVal = 0;
  let maxChar = "";

  // for (of) loop for iterables
  for (let char of str) {
    charsObj[char] = charsObj[char] + 1 || 1;
  }

  // for (in) loop for objects
  for (let char in charsObj) {
    if (charsObj[char] > maxVal) {
      maxVal = charsObj[char];
      maxChar = char;
    }
  }
  return maxChar;
}

maxChar(str);
