// source: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

// Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

// A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

// Example:

// Input: "23"
// Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

const digits = "23";

function letterCombinations(digits) {
  if (!digits) return [];

  const map = {
    1: [],
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
  };

  let combinations = [...map[digits[0]]];

  for (let i = 1; i < digits.length; i++) {
    debugger;
    const updatedCombinations = [];

    combinations.forEach((combination) => {
      map[digits[i]].forEach((letter) => {
        updatedCombinations.push(combination + letter);
      });
    });
    combinations = updatedCombinations;
  }
  return combinations;
}

console.log(letterCombinations(digits));
