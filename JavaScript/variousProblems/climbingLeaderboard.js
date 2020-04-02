//source: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

const scores = [100, 100, 50, 40, 40, 20, 10];
const alice = [5, 25, 50, 120];
// const globalUnique = [...new Set(scores)];

// globalUnique = [100, 50, 40, 20, 10]

function climbingLeaderboard(scores, alice) {
  let result = [];
  let uniqueScores = [...new Set(scores)];

  for (const score of alice) {
    if (score >= uniqueScores[0]) {
      result.push(1);
    } else if (score <= uniqueScores[uniqueScores.length - 1]) {
      result.push(uniqueScores.length + 1);
    } else {
      result.push(indexBinarySearch(score, uniqueScores, [...uniqueScores]));
    }
  }
  return result;
}

function indexBinarySearch(score, uniqueScores, globalUnique) {
  let mid = Math.floor(uniqueScores.length / 2);

  // base case
  if (score === uniqueScores[mid]) {
    return mid + 1;
  } else if (uniqueScores.length === 1 && uniqueScores[0] > score) {
    return 2 + globalUnique.indexOf(uniqueScores[0]);
  } else if (uniqueScores.length === 1 && uniqueScores[0] < score) {
    return 1 + globalUnique.indexOf(uniqueScores[0]);
  }

  if (score < uniqueScores[mid]) {
    return indexBinarySearch(score, uniqueScores.slice(mid), globalUnique);
  } else if (score > uniqueScores[mid]) {
    return indexBinarySearch(score, uniqueScores.slice(0, mid), globalUnique);
  }
}

console.log(climbingLeaderboard(scores, alice));
