const targetWord = "tame";
const dict = ["team", "meat", "apple", "orange"];

function anagrams(targetWord, dict) {
  const targetWordSorted = [...targetWord].sort().join("");
  let foundAnagrams = [targetWord];

  for (let i = 0; i < dict.length; i++) {
    if ([...dict[i]].sort().join("") === targetWordSorted) {
      foundAnagrams.push(dict[i]);
    }
  }
  console.log(foundAnagrams);
  return foundAnagrams;
}

anagrams(targetWord, dict);

module.exports = anagrams;
