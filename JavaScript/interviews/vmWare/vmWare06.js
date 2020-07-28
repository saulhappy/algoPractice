// balanced brackets

const values = ["[{}]", "[{]]"];

function braces(values) {
  let result = [];

  for (i = 0; i < values.length; i++) {
    result.push(isValid(values[i]));
  }

  function isValid(s) {
    let sArr = [...s];
    let stack = [];

    for (let char of sArr) {
      if (char === "[") stack.push("]");
      else if (char === "{") stack.push("}");
      else if (char === "(") stack.push(")");
      else if (stack.length === 0 || char !== stack.pop()) return "NO";
    }
    if (stack.length === 0) {
      return "YES";
    } else {
      return "NO";
    }
  }

  return result;
}

console.log(braces(values));
