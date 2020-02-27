//to run test execute in terminal: npm run test

const anagrams = require("./anagramDictFinderSort.js");

test("anagrams with arguments targetWord of 'tame', and dictionary of ['team', 'meat', 'apple', 'orange'] returns an array of ['tame', 'team', 'meat']", () => {
  expect(anagrams("tame", ["team", "meat", "apple", "orange"])).toEqual([
    "tame",
    "team",
    "meat"
  ]);
});

test("anagrams with arguments targetWord of 'tame', and dictionary of ['apple', 'orange'] returns an array of ['tame']", () => {
  expect(anagrams("tame", ["apple", "orange"])).toEqual(["tame"]);
});

test("anagrams with arguments targetWord of 'dog', and dictionary of ['apple', 'orange', 'god'] returns an array of ['dog', 'god']", () => {
  expect(anagrams("dog", ["apple", "god", "orange"])).toEqual(["dog", "god"]);
});

// test("anagrams with arguments targetWord of 'dormitory', and dictionary of ['apple', 'orange', 'dirty room'] returns an array of ['tame']", () => {
//   expect(anagrams("dormitory", ["apple", "orange", "dirty room"])).toEqual([
//     "dormitory",
//     "dirty room"
//   ]);
// });
