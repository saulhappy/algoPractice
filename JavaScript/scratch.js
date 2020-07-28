const sentWord = "east";
const prefix = "burg";

function prefixTest(sentWord, prefix) {
  for (let i = 0; i < prefix.length; i++) {
    if (prefix[i] != sentWord[i]) return -1;
  }
  return 1;
}

console.log(prefixTest(sentWord, prefix));
