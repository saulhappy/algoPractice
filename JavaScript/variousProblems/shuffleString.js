// source: https://leetcode.com/problems/shuffle-string/

const s = "aiohn";
const indeces = [3, 1, 4, 2, 0];

function restoreString(s, indeces) {
  let newStrArr = [];

  for (let i = 0; i < indeces.length; i++) {
    newStrArr[indeces[i]] = s[i];
  }
  return newStrArr.join("");
}

console.log(restoreString(s, indeces));
