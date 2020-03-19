//HackerRank: https://www.hackerrank.com/challenges/bon-appetit/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

// Complete the bonAppetit function below.

const bill = [3, 10, 2, 9];
const k = 1;
const b = 7;

function bonAppetit(bill, k, b) {
  let correctBill = bill.filter(amount => amount !== bill[k]);
  let billSum = correctBill.reduce((a, b) => a + b, 0);
  let toCharge = billSum / 2;

  if (toCharge === b) {
    console.log("Bon Appetit");
  } else {
    console.log(b - toCharge);
  }
}

bonAppetit(bill, k, b);
