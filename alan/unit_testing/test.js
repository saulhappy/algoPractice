//npm run test

const birthdayCakeCandles = require("./index");

// test("birthdayCakeCandles is a function", () => {
//   expect(typeof birthdayCakeCandles.prototype.constructor).toEqual("function");
// });

// test("birthdayCakeCandles output is a number", () => {
//   expect(typeof birthdayCakeCandles([0, 1, 2, 3, 4, 5])).toEqual("number");
// });

test("birthdayCakeCandles with argument [4,4,1,3] returns 2", () => {
  expect(birthdayCakeCandles([4, 4, 1, 3])).toBe(2);
});

test("birthdayCakeCandles with argument [9,9,9,9,9] returns 5", () => {
  expect(birthdayCakeCandles([9, 9, 9, 9, 9])).toBe(5);
});

test("birthdayCakeCandles with argument [] returns 0", () => {
  expect(birthdayCakeCandles([])).toBe(0);
});

test("birthdayCakeCandles with argument [0,1,2,3,4,5] returns 1", () => {
  expect(birthdayCakeCandles([0, 1, 2, 3, 4, 5])).toBe(1);
});

function arrCall(arr) {
  return arr([1, 2, 3]);
}
// a test for no argument?
// a test for argument not equal to array?

test("birthdayCakeCandles calls its callback with array", () => {
  const birthdayCakeCandles = jest.fn();
  arrCall(birthdayCakeCandles);
  expect(birthdayCakeCandles).toBeCalledWith(expect.any(Array));
});
