const a = 2437;
const b = 875;

function ma(a, b) {
  let x = a;
  let y = b;

  for (let i = 0; i < 100; i++) {
    debugger;
    if (x > y) {
      x = x - y;
    }

    if (x < y) {
      y = y - x;
    }
  }
  return x;
}

console.log(ma(a, b));
