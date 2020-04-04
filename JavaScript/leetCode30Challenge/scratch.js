let sqrArr = [20, 10, 5, 10];

function checkSum(sqrArr) {
  return sqrArr.reduce((a, b) => a + b, 0);
}

console.log(checkSum(sqrArr));
