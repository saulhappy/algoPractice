// source: https://leetcode.com/problems/shuffle-string/

const s = "art";
const indices = [1, 0, 2];

function restoreString(s, indices) {
  let newStrArr = [];

  for (let i = 0; i < indices.length; i++) {
    newStrArr[indices[i]] = s[i];
  }
  return newStrArr.join("");
}

console.log(restoreString(s, indices));
