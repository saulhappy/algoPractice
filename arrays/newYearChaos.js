// problem: https://www.hackerrank.com/challenges/new-year-chaos/forum?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
// test says should be 7 vs 6 - why?

const q = [1, 2, 5, 3, 7, 8, 6, 4];

function minimumBribes(q) {
  let swaps = 0;
  for (let i = 0; i < q.length; i++) {
    // debugger;
    if (i + 1 != q[i]) {
      if (q[i] - (i + 1) > 2) {
        console.log("Too chaotic");
        swaps += q[i] - (i + 1);
        return;
      } else if (q[i] > i + 1) {
        swaps += q[i] - (i + 1);
      }
    }
  }
  console.log(swaps);
}

minimumBribes(q);
