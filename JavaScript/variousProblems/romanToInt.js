//source: https://leetcode.com/problems/roman-to-integer/

const romanHash = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

const s = "II";

function romanToInt(s) {
  let accumulator = 0;
  s = [...s];

  return s;
}

console.log(romanToInt(s));
console.log(romanHash);
