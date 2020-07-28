// question 6: better compression
// string should be in alphabetical order followed by total count
// example 1: "a3c9b2c1" =>  "a3b2c10"
// example 2: "a12b56c1" => "a12b56c1"

const s = "a3c9b2c1";

function betterCompression(s) {
  const sSplit = s.match(/[a-z]+|[^a-z]+/gi);
  let sObj = {};
  let sorted = {};
  let result = "";

  // make object of strings, sum all occurrences
  for (let i = 0; i < sSplit.length; i += 2) {
    sObj[sSplit[i]] = (sObj[sSplit[i]] || 0) + parseInt(sSplit[i + 1]);
  }

  // sort
  Object.keys(sObj)
    .sort()
    .forEach(function (key) {
      sorted[key] = sObj[key];
    });

  // make string
  for (let char in sorted) {
    result += char + sorted[char];
  }

  return result;
}

console.log(betterCompression(s));
