//to run test execute in terminal: npm run test

const anagrams = require("./anagramDictFinderSort.js");

// happy path test
test("anagrams with arguments targetWord of 'tame', and dictionary of ['team', 'meat', 'apple', 'orange'] returns an array of ['tame', 'team', 'meat']", () => {
  expect(anagrams("tame", ["team", "meat", "apple", "orange"])).toEqual([
    "tame",
    "team",
    "meat"
  ]);
});

// test for no anagrams found
test("anagrams with arguments targetWord of 'tame', and dictionary of ['apple', 'orange'] returns an array of ['tame']", () => {
  expect(anagrams("tame", ["apple", "orange"])).toEqual(["tame"]);
});

// test for arguments of different case
test("anagrams with arguments targetWord of 'Dog', and dictionary of ['apple', 'orange', 'god'] returns an array of ['Dog', 'god']", () => {
  expect(anagrams("Dog", ["apple", "god", "orange"])).toEqual(["Dog", "god"]);
});
