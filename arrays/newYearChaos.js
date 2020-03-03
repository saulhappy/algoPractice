// const q = [2, 1, 5, 3, 4];
// 3

const q = [1, 2, 5, 3, 7, 8, 6, 4];
//7

function minimumBribes(q) {
  let swaps = 0;
  for (let i = 0; i < q.length; i++) {
    if (i + 1 != q[i]) {
      if (q[i] - (i + 1) > 2) {
        console.log("Too chaotic");
        return;
      }
      if (Math.max(...q) > q[i]) {
        let currentNum = q[i];
        for (let j = 0; j < i; j++) {
          if (q[j] > currentNum) {
            swaps++;
          }
        }
      }
    }
  }
  console.log(swaps);
}

minimumBribes(q);
