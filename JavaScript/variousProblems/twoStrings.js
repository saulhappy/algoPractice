// source: https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

const s1 = "hello";
const s2 = "world";
function twoStrings(s1, s2) {
  for (let char of s1) {
    if (s2.includes(char)) {
      return "YES";
    }
  }
  return "NO";
}

console.log(twoStrings(s1, s2));
