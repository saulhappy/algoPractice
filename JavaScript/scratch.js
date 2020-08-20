let text = "dabbbaacc";

function maxChar(text) {
  let textSorted = text.split("").sort();
  let charsObj = {};
  let maxVal = 0;
  let maxChar = "";

  for (let char of textSorted) {
    charsObj[char] = charsObj[char] + 1 || 1;
  }

  for (let char in charsObj) {
    if (charsObj[char] > maxVal) {
      maxVal = charsObj[char];
      maxChar = char;
    }
  }
  return maxChar;
}

console.log(maxChar(text));
