// problem source: https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

// test case 1:
// const s = "abcac";
// const n = 10;
// expected result: 4
// status: pass

// test case 2:
// const s = "aba";
// const n = 10;
// expected result: 7
// status: pass

// test case 3:
// const s = "a";
// const n = 1000000000000;
// expected result: 1000000000000
// status: pass

// test case 4
// const s = "alan";
// const n = 20;
// expected result: 10
// status: pass

// test case 5
// const s = "this is test";
// const n = 1000;
// expected result: 0
// status: pass

// test case 6
// const s = "A";
// const n = 10;
// expected result: 0
// status: pass

// Complete the repeatedString function below.

const s = "abba";
const n = 6;

function repeatedString(s, n) {
  let fullFittingAs = aCounter(s) * Math.floor(n / s.length);
  let leftOverAs = aCounter(s.slice(0, n % s.length));

  return leftOverAs + fullFittingAs;
}

function aCounter(s) {
  let counter = 0;
  for (let char of s) {
    if (char === "a") {
      counter++;
    }
  }
  return counter;
}
console.log(repeatedString(s, n));
