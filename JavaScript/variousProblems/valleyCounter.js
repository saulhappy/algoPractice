// source: https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

const s = ["U", "D", "D", "D", "U", "D", "U", "U"];
const n = 8;

function countingValleys(n, s) {
  let valleyCounter = 0;
  let pathCounter = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "U") {
      pathCounter += 1;
    } else {
      pathCounter += -1;
    }
    if (pathCounter === 0 && s[i] === "U") {
      valleyCounter += 1;
    }
  }

  return valleyCounter;
}

console.log(countingValleys(n, s));
