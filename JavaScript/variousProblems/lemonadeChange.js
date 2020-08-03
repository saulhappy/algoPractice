// source: https://leetcode.com/problems/lemonade-change/

const bills = [5, 5, 5, 10, 20];

function lemonadeChange(bills) {
  let billsObj = {};
  let changeDue = 0;

  for (let i = 0; i < bills.length; i++) {
    billsObj[bills[i]] = billsObj[bills[i]] + 1 || 1;
    changeDue = bills[i] - 5;

    if (changeDue > 0) {
      let cashOnHand = 0;
      let changeGiven = 0;

      for (let bill in billsObj) {
        cashOnHand += billsObj[bill] * bill;
        if (cashOnHand < changeDue) return false;
      }

      while (changeGiven != changeDue) {
        for (let cash in billsObj) {
          changeGiven += cash * 1;
          billsObj[cash] = billsObj[cash] - 1;

          if (changeGiven === changeDue) break;
          if (changeGiven > changeGiven) break;
        }
      }
    }
  }

  changeDue === 0 ? true : false;
}

console.log(lemonadeChange(bills));
