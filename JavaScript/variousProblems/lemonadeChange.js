// source: https://leetcode.com/problems/lemonade-change/

const bills = [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5];

function lemonadeChange(bills) {
  let fives = 0;
  let tens = 0;

  for (let i = 0; i < bills.length; i++) {
    // debugger;
    if (bills[i] === 5) {
      fives++;
    }
    if (bills[i] === 10) {
      if (fives < 1) {
        return false;
      } else {
        tens++;
        fives--;
      }
    }
    if (bills[i] === 20) {
      if (fives && tens) {
        fives -= 1;
        tens -= 1;
      } else if (fives && tens) {
        fives -= 1;
        tens -= 1;
      } else if (fives >= 3) {
        fives -= 3;
      } else {
        return false;
      }
    }
  }

  return true;
}

console.log(lemonadeChange(bills));
