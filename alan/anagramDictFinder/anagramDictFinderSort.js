const targetWord = "Dog";
const dict = ["team", "meat", "apple", "god", "orange"];

function sortFunc(str) {
  return [...str]
    .sort()
    .join("")
    .toLocaleLowerCase();
}

function anagrams(targetWord, dict) {
  const targetWordSorted = sortFunc(targetWord);
  let foundAnagrams = [targetWord];

  for (let i = 0; i < dict.length; i++) {
    if (sortFunc(dict[i]) === targetWordSorted) {
      foundAnagrams.push(dict[i]);
    }
  }
  return foundAnagrams;
}

anagrams(targetWord, dict);

module.exports = { anagrams, sortFunc };
