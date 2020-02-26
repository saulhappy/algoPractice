const dict = ["team", "meat", "apple", "orange"];
const targetWord = "tame";

function anagrams(dict, targetWord) {
  const targetWordSorted = [...targetWord].sort().join("");
  let foundAnagrams = [targetWord];

  for (let i = 0; i < dict.length; i++) {
    if ([...dict[i]].sort().join("") === targetWordSorted) {
      foundAnagrams.push(dict[i]);
    }
  }
  console.log(foundAnagrams);
}

anagrams(dict, targetWord);
