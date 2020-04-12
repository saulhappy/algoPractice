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

// algorithm: create an anagram function
// for each i of strs,
//    nest another loop with var J
//      ask if next element is anagram of current element
//        if it is, push into element's array.
//        if it isn't move to next element, increment J.
// at end, increment i of strs with new array.
// then concat results of arrays.

const strs = ["eat", "tea", "tan", "ate", "nat", "bat"];

function groupAnagrams(strs) {}

console.log(groupAnagrams(str));
