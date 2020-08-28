// 1. Use recursion to create a function to compute the exponent of a number.
// For Example: base=2, exp=3, would return 2^3=2*2*2=8

const base = 2;
const exp = -3;

const exponent = function (base, exp) {
  if (exp < 0) return;

  if (exp === 0) {
    return 1;
  } else if (exp === 1) {
    return base;
  } else {
    return (base *= exponent(base, exp - 1));
  }
};

console.log(exponent(base, exp));
