//DIRECTIONS

// You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age.
// When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.
// For example, if your niece is turning 4 years old, and the cake will have 4 candles of height [4,4,1,3]
// she will be able to blow out 2 candles successfully, since the tallest candles are of height 4 and there are 2 such candles.

const arr = [4, 5, 6, 6, 6, 1];

function birthdayCakeCandles(arr) {
  let max = 0;
  let count = 0;

  for (let num of arr) {
    if (max < num) {
      max = num;
      count = 0;
    }
    if (max === num) {
      count++;
    }
  }
  return count;
}

birthdayCakeCandles(arr);

module.exports = birthdayCakeCandles;
