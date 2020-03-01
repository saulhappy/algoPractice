//to run test execute in terminal: npm run [name of test file]

const anagrams = require("./anagramDictFinderSort");

// test of sortFunc

test("expect with input of 'dog' return an object of {d: 1, o: 1, g:1", () => {
  expect(anagrams.sortFunc("dog")).toEqual("dgo");
});

// happy path test
test("anagrams with arguments targetWord of 'tame', and dictionary of ['team', 'meat', 'apple', 'orange'] returns an array of ['tame', 'team', 'meat']", () => {
  expect(
    anagrams.anagrams("tame", ["team", "meat", "apple", "orange"])
  ).toEqual(["tame", "team", "meat"]);
});

// test for no anagrams found
test("anagrams with arguments targetWord of 'tame', and dictionary of ['apple', 'orange'] returns an array of ['tame']", () => {
  expect(anagrams.anagrams("tame", ["apple", "orange"])).toEqual(["tame"]);
});

// test for arguments of different case
test("anagrams with arguments targetWord of 'Dog', and dictionary of ['apple', 'orange', 'god'] returns an array of ['Dog', 'god']", () => {
  expect(anagrams.anagrams("Dog", ["apple", "god", "orange"])).toEqual([
    "Dog",
    "god"
  ]);
});
