// source: https://leetcode.com/problems/lemonade-change/

const bills = [5, 5, 5, 10, 20];

function lemonadeChange(bills) {
  let billsObj = {};
  let changeDue = 0;

  for (let bill of bills) {
    billsObj[bill] = billsObj[bill] + 1 || 1;
    changeDue = bill - 5;
    if (changeDue > 0) {
      let cashOnHand = 0;
      let changeGiven = 0;

      for (let bill in billsObj) {
        cashOnHand += billsObj[bill] * bill;
        if (cashOnHand < changeDue) return false;

        debugger;
      }
    }
  }

  return false;
}

console.log(lemonadeChange(bills));
