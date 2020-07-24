// max trailing record

// levels = [5, 3, 6, 7, 4];
//4

levels = [1, 2, 3, 4, 5];
// 0

function maxTrailing(levels) {
  let maxTrail = -1;

  for (let i = 0; i < levels.length; i++) {
    for (let j = i + 1; j < levels.length; j++) {
      if (levels[j] > levels[i] && maxTrail < levels[j] - levels[i]) {
        maxTrail = levels[j] - levels[i];
      }
    }
  }

  return maxTrail;
}

console.log(maxTrailing(levels));
