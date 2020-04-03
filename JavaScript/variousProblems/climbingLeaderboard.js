//source: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

const scores = [100, 90, 90, 80, 75, 60];
const alice = [50, 65, 77, 90, 102];
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
      result.push(indexBinarySearch(score, uniqueScores));
    }
  }
  return result;
}

function indexBinarySearch(score, uniqueScores) {}

console.log(climbingLeaderboard(scores, alice));

// function works, but times out on tests. refactoring above.
// function indexBinarySearch(score, uniqueScores, globalUnique) {
//     let mid = Math.floor(uniqueScores.length / 2);

//     // base case
//     if (score === uniqueScores[mid]) {
//       return mid + 1;
//     } else if (uniqueScores.length === 1 && uniqueScores[0] > score) {
//       return 2 + globalUnique.indexOf(uniqueScores[0]);
//     } else if (uniqueScores.length === 1 && uniqueScores[0] < score) {
//       return 2 + globalUnique.indexOf(uniqueScores[0]);
//     }

//     if (score < uniqueScores[mid]) {
//       return indexBinarySearch(score, uniqueScores.slice(mid), globalUnique);
//     } else if (score > uniqueScores[mid]) {
//       return indexBinarySearch(score, uniqueScores.slice(0, mid), globalUnique);
//     }
//   }
