// source: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

// Given a sentence that consists of some words separated by a single space, and a searchWord.

// You have to check if searchWord is a prefix of any word in sentence.

// Return the index of the word in sentence where searchWord is a prefix of this word (1-indexed).

// If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

// A prefix of a string S is any leading contiguous substring of S.

// Example 1:

// Input: sentence = "i love eating burger", searchWord = "burg"
// Output: 4
// Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.

const sentence = "hello from the other side";
const searchWord = "they";

function isPrefixOfWord(sentence, searchWord) {
  let sentSplit = sentence.split(" ");

  for (let i = 0; i < sentSplit.length; i++) {
    if (prefixTest(sentSplit[i], searchWord)) return i + 1;
  }

  return -1;

  function prefixTest(sentWord, searchWord) {
    for (let i = 0; i < searchWord.length; i++) {
      if (searchWord[i] != sentWord[i]) return false;
    }
    return true;
  }
}

console.log(isPrefixOfWord(sentence, searchWord));
