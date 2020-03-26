// source: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

const c = [0, 0, 1, 0, 0, 1, 0];
// result: 4

// algorithm: for each step of c, if i + 2 != 1, then jump by increment i to that spot,
// and increment a jump counter.
// if i + 2 = 1, then pass

function jumpingOnClouds(c) {
  let jumps = 0;
  for (let i = 0; i < c.length; i++) {
    if (c[i + 2] != 1) {
      jumps += 1;
      i += 2;
    }
    if (c[i + 1] != 1) {
      jumps += 1;
      i += 1;
    }
  }
  return jumps;
}

console.log(jumpingOnClouds(c));
