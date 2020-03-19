const magazine = "ive got a lovely bunch of coconuts";
const note = "ive got some coconuts";

function checkMagazine(magazine, note) {
  let magazineArray = magazine.split(/\s+/);
  let magazineMap = {};
  let noteArray = note.split(/\s+/);
  let noteMap = {};
  let result = [];

  for (let word of magazineArray) {
    magazineMap[word] = magazineMap[word] + 1 || 1;
  }

  for (let word of noteArray) {
    noteMap[word] = noteMap[word] + 1 || 1;
  }

  for (word in noteMap) {
    if (
      noteMap[word] > magazineMap[word] ||
      typeof magazineMap[word] === "undefined"
    ) {
      result.push("No");
    }
    result.push("Yes");
  }

  result.includes("No") ? console.log("No") : console.log("Yes");
}

checkMagazine(magazine, note);

// THIS IS THE FUNCTION TO GET HACKERRANK TESTS TO PASS- DOESN'T USE LARGE STRING, SO NO NEED TO SPLIT INTO ARRAY
// function checkMagazine(magazine, note) {
//   let magazineMap = {};
//   let noteMap = {};
//   let result = [];

//   for (let word of magazine) {
//     magazineMap[word] = magazineMap[word] + 1 || 1;
//   }

//   for (let word of note) {
//     noteMap[word] = noteMap[word] + 1 || 1;
//   }

//   for (let word in noteMap) {
//     if (
//       noteMap[word] > magazineMap[word] ||
//       typeof magazineMap[word] === "undefined"
//     ) {
//       result.push("No");
//     }
//     result.push("Yes");
//   }

//   result.includes("No") ? console.log("No") : console.log("Yes");

// }
