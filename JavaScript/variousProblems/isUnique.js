// Source: Cracking the coding interview, page 90.
// Implement an algorithm to determine if all characters in a string are unique. What if you couldn't use an additional data structure?

const str = "saaul";

// method 1: no additional data structure.
// function isUnique(str) {
//   let cleansed = str.split("").sort().join("");

//   for (let i = 0; i < cleansed.length; i++) {
//     for (let j = i + 1; j < cleansed.length; j++) {
//       if (cleansed[i] === cleansed[j]) {
//         return false;
//       }
//     }
//     return true;
//   }
// }

// method 2: using a hash table

function isUnique(str) {
  let hash = {};

  for (char of str) {
    hash[char] = hash[char] + 1 || 1;
  }

  for (char in hash) {
    if (hash[char] > 1) {
      return false;
    }
  }
  return true;
}

console.log(isUnique(str));
