const dict = ["team", "meat", "apple", "orange"];
const targetWord = "Tame";

function anagrams(dict, targetWord) {
  function buildCharMap(str) {
    const charMap = {};
    for (let char of str.replace(/[^\w]/g, "").toLocaleLowerCase()) {
      charMap[char] = charMap[char] + 1 || 1;
    }
    return charMap;
  }

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
  console.log([...new Set(foundAnagrams)]);
}

anagrams(dict, targetWord);

module.exports = anagrams;
