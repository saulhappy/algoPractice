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
      result.push(checkDivNum(i));
    }
  }

  result = result.filter(function (element) {
    return element !== undefined;
  });

  return result;

  function checkDivNum(n) {
    let nString = n.toString();
    let nArray = [...nString];
    nArray = nArray.map((num) => parseInt(num));

    let divisibleNums = [];

    for (let i = 0; i < nArray.length; i++) {
      if (nArray[i] === 0) return;

      if (n % nArray[i] === 0) {
        divisibleNums.push(nArray[i]);
      } else {
        continue;
      }
    }

    if (nArray.length === divisibleNums.length) return n;
  }
}

console.log(selfDividingNumbers(left, right));
