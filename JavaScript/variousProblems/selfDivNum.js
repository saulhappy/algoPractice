// source: https://leetcode.com/problems/self-dividing-numbers/

const left = 1;
const right = 22;

function selfDividingNumbers(left, right) {
  let result = [];

  for (let i = left; i <= right; i++) {
    if (i === 0) return;

    if (i > 0 && i < 10) {
      result.push(i);
    } else {
      checkDivNum(i);
    }

    function checkDivNum(n) {
      let ints = [];
      let str = n.toString();

      for (let char of str) {
        if (parseInt(str[char]) === 0) {
          return;
        } else {
          ints.push(parseInt(str[char]));
        }
      }
    }
  }
}

selfDividingNumbers(left, right);
