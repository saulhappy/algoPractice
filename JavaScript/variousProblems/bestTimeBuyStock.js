// source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

const prices = [7, 1, 5, 3, 6, 4];

function maxProfit(prices) {
  let profit = 0;

  for (let i = 0; i < prices.length; i++) {
    for (let j = i + 1; j < prices.length; j++) {
      if (-prices[i] + prices[j] > profit) {
        profit = -prices[i] + prices[j];
      }
    }
  }
  return profit;
}

console.log(maxProfit(prices));
