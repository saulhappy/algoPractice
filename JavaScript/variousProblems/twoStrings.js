// source: https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

const s1 = "hello";
const s2 = "world";
function twoStrings(s1, s2) {
  let s1Arr = s1.split("");
  let s2Arr = s2.split("");
  let matchCounter = 0;

  for (let char of s1Arr) {
    if (s2Arr.includes(char)) {
      matchCounter++;
    }
  }

  if (matchCounter > 0) {
    return "YES";
  } else {
    return "NO";
  }
}

console.log(twoStrings(s1, s2));
