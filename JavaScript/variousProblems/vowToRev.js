const word = "san francisco";

function reverseVowels(word) {
  const vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"];
  let wordVowelStack = [];
  let newWord = [];

  for (let i = 0; i < word.length; i++) {
    if (vowels.includes(word[i])) {
      wordVowelStack.push(word[i]);
    }
  }

  for (let i = 0; i < word.length; i++) {
    if (!vowels.includes(word[i])) {
      newWord.push(word[i]);
    } else {
      newWord.push(wordVowelStack.pop());
    }
  }

  return newWord.join("");
}

console.log(reverseVowels(word));
