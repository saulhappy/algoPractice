// Source: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288/
// Given an array of strings, group anagrams together.
// Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
// Output:
// [
//   ["ate","eat","tea"],
//   ["nat","tan"],
//   ["bat"]
// ]
// all inputs will be lower case and order does not matter.

const strs = ["eat", "tea", "tan", "ate", "nat", "bat"];

function groupAnagrams(strs) {
  let result = {};

  for (let word of strs) {
    let cleansed = word.split("").sort().join("");
    if (result[cleansed]) {
      result[cleansed].push(word);
    } else {
      result[cleansed] = [word];
    }
  }
  return Object.values(result);
}

console.log(groupAnagrams(strs));
