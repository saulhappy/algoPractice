// Source: Cracking the coding interview, page 90.
// Implement an algorithm to determine if all characters in a string are unique. What if you couldn't use an additional data structure?

const str = "saul";

// method 1: no additional data structure.
function isUnique(str) {
  let cleansed = str.split("").sort().join("");

  for (let i = 0; i < cleansed.length; i++) {
    for (let j = i + 1; j < cleansed.length; j++) {
      if (cleansed[i] === cleansed[j]) {
        return false;
      }
    }
    return true;
  }
}

console.log(isUnique(str));
