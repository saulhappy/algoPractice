const targetWord = "Dog";
const dict = ["team", "meat", "apple", "god", "orange"];

function anagrams(targetWord, dict) {
  const targetWordSorted = [...targetWord]
    .sort()
    .join("")
    .toLocaleLowerCase();
  let foundAnagrams = [targetWord];

  for (let i = 0; i < dict.length; i++) {
    if (
      [...dict[i]]
        .sort()
        .join("")
        .toLocaleLowerCase() === targetWordSorted
    ) {
      foundAnagrams.push(dict[i]);
    }
  }
  console.log(foundAnagrams);
  return foundAnagrams;
}

anagrams(targetWord, dict);

module.exports = anagrams;
