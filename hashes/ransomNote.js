const magazine = "give me one grand today night";
const note = "give one grand today";

function checkMagazine(magazine, note) {
  for (word in magazine) {
    console.log(magazine[word]);
  }
}

checkMagazine(magazine, note);
