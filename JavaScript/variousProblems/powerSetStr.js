const inputStr = "abc";
// output = a, ab, abc, ac, b, bc, c

function PowerSet(inputStr) {
  let result = "";

  if (inputStr.length === 0) return 0;

  function addToResult(prefix, string) {
    if (string.length === 0) return "";

    for (let i = 0; i < string.length; i++) {
      result + prefix + string[i];
      addToResult(prefix + string[i], string.slice(i + 1));
    }
  }

  addToResult("", inputStr);

  return result;
}

console.log(PowerSet(inputStr));
