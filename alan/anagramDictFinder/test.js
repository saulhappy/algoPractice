//to run test execute in terminal: npm run test

const anagramDictFinder = require("./anagramDictFinderSort.js");

test("anagramDictFinder with arguments targetWord of 'tame', and dictionary of ['team', 'meat', 'apple', 'orange'] returns an array of ['tame', 'team', 'meat']", () => {
  expect(
    anagramDictFinder("tame", ["team", "meat", "apple", "orange"])
  ).toEqual(["tame", "team", "meat"]);
});
