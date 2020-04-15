// source: https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

const s1 = "hello";
const s2 = "world";
function twoStrings(s1, s2) {
  let s1hash = {};
  let s2hash = {};

  for (let char of s1) {
    s1hash[char] = s1hash[char] + 1 || 1;
  }

  for (let char of s2) {
    s2hash[char] = s2hash[char] + 1 || 1;
  }

  // create a counter. loop through one of the hashes. for every match, increment counter. if at the end of the loop, counter
  // is at 0, then return No, else yes.
}

console.log(twoStrings(s1, s2));
