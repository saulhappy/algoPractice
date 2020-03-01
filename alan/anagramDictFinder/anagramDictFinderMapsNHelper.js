const dict = ["team", "meat", "apple", "orange"];
const targetWord = "Tame";

function buildCharMap(str) {
  const charMap = {};
  for (let char of str.replace(/[^\w]/g, "").toLocaleLowerCase()) {
    charMap[char] = charMap[char] + 1 || 1;
  }
  return charMap;
}

function anagrams(targetWord, dict) {
  const targetWordMap = buildCharMap(targetWord);
  let foundAnagrams = [targetWord];

  for (let word of dict) {
    if (word.length === targetWord.length) {
      let wordMap = buildCharMap(word);
      for (char in wordMap) {
        wordMap[char] === targetWordMap[char]
          ? foundAnagrams.push(word)
          : false;
      }
    }
  }
  return [...new Set(foundAnagrams)];
}

anagrams(targetWord, dict);

module.exports = { anagrams, buildCharMap };
