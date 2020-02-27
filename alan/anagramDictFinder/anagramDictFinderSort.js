const targetWord = "tame";
const dict = ["team", "meat", "apple", "orange"];

function anagramDictFinder(targetWord, dict) {
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

anagramDictFinder(targetWord, dict);

module.exports = anagramDictFinder;
