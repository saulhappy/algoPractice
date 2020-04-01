//source: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

const scores = [100, 100, 50, 40, 40, 20, 10];
const alice = [5, 25, 50, 120];

function climbingLeaderboard(scores, alice) {
  let scoresRank = [];
  scoresRank[0] = 1;

  for (let i = 1; i < scores.length; i++) {
    // debugger;
    if (scores[i] === scores[i - 1]) {
      scoresRank.push(scoresRank[i - 1]);
    }
    scoresRank.push(scoresRank[i] + 1);
  }

  return scoresRank;
}

console.log(climbingLeaderboard(scores, alice));

// //source: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

// const scores = [100, 100, 50, 40, 40, 20, 10];
// const alice = [5, 25, 50, 120];

// function climbingLeaderboard(scores, alice) {
//   // create scoresMap
//   let uniqueScores = [...new Set(scores)];
//   let scoresMap = {};
//   let uniqueAlice = [...new Set(alice)];
//   let aliceRank = [];
//   for (let i = 0; i < uniqueScores.length; i++) {
//     scoresMap[i + 1] = uniqueScores[i];
//   }

//   // for each element of alice, if the value of i exist in the map, push that score's key (rank) into
//   // the alice rank. else, iterate through the maps keys, to see what the rank ought to be.

//   for (let i = 0; i < uniqueAlice.length; i++) {
//     if (Object.values(scoresMap).includes(uniqueAlice[i])) {
//       aliceRank.push(
//         Object.keys(scoresMap).find(key => scoresMap[key] === uniqueAlice[i])
//       );
//     } else {
//       for (score of uniqueAlice) {
//         for (value in scoresMap) {
//           if (uniqueAlice[score] > scoresMap[value]) {
//             scoresMap[value - 1] = uniqueAlice[score];
//           }
//           scoresMap[value] = uniqueAlice[score];
//         }
//       }
//     }
//   }
//   return scoresMap;
// }

// console.log(climbingLeaderboard(scores, alice));
