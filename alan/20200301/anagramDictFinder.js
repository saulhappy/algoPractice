const dict = ["team", "meat", "apple", "orange"];
const word = "tame";

function anagrams(dict, word) {
  let wordObj = {};
  let dictWordObj = {};
  let anagrams = [word];

  for (let char of word) {
    wordObj[char] = wordObj[char] + 1 || 1;
  }

  for (let i = 0; i < dict.length; i++) {
    if ((dict[i].length = word.length)) {
      for (let char of dict[i]) {
        debugger;
        dictWordObj[char] = dictWordObj[char] + 1 || 1;
      }
      if (dictWordObj === wordObj) {
        anagrams.push(dict[i]);
      }
    }
  }
  console.log(anagrams);
}

anagrams(dict, word);
