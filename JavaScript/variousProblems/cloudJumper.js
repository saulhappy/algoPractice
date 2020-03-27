// source: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

const c = [0, 0, 1, 0, 0, 1, 0];
// result: 4

// const c = [0, 0, 0, 0, 1, 0];
// result: 3

// const c = [0, 0, 0, 0];
// result 3

function jumpingOnClouds(c) {
  let jumps = 0;
  let i = 0;
  while (i < c.length - 1) {
    debugger;
    if (c[i + 2] != 1) {
      i += 2;
      jumps++;
    } else if (c[i + 1] != 1) {
      i += 1;
      jumps++;
    } else {
      i++;
    }
  }
  return jumps;
}

console.log(jumpingOnClouds(c));
