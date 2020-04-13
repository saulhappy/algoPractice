const obj = {
  one: ["1", "uno"],
  two: 1,
  three: 2,
};

word1 = "listen";
word2 = "silent";

console.log(word1.split("").sort().join(""));

console.log(
  word1.split("").sort().join("") === word2.split("").sort().join("")
);
