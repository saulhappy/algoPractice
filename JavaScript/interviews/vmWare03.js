// question 6: better compression
// string should be in alphabetical order followed by total count
// example 1: "a3c9b2c1" =>  "a3b2c10"
// example 2: "a12b56c1" => "a12b56c1"

const s = "a3c9b2c1";

function betterCompression(s) {
  const sSplit = s.match(/[a-z]+|[^a-z]+/gi);
  let chars = [];
  let nums = [];
  let result = "";

  for (let i = 0; i < sSplit.length; i++) {
    if (i % 2 != 0) {
      nums.push(sSplit[i]);
    } else {
      chars.push(sSplit[i]);
    }
  }

  const sObj = objBuilder(nums, chars);

  for (let char in sObj) {
    result += char + sObj[char];
  }

  return result;

  // still need to sort.
}

const chars = ["a", "c", "b", "c"];
const nums = ["3", "9", "2", "1"];

function objBuilder(nums, chars) {
  let obj = {};
  let i = 0;

  for (let char of chars) {
    if (!obj[char]) {
      obj[char] = nums[i];
    } else {
      obj[char] = parseInt(obj[char]) + parseInt(nums[i]);
    }
    i++;
  }
  return obj;
}

betterCompression(s);
