const n = 128;

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

console.log(checkDivNum(n));
