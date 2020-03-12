// problem source: https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

// test case 1:
// const s = "abcac";
// const n = 10;
// epected result: 4
// status: pass

// test case 2:
// const s = "aba";
// const n = 10;
// epected result: 7
// status: pass

// test case 3:
// const s = "a";
// const n = 1000000000000;
// epected result: 1000000000000
// status: pass

// Complete the repeatedString function below.
function repeatedString(s, n) {
  let counter = 0;
  for (let char of s) {
    if (char === "a") {
      counter++;
    }
  }
  let result = Math.ceil(counter * (n / s.length));
  console.log(result);
  return result;
}

repeatedString(s, n);
