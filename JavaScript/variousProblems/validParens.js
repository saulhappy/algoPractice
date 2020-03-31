// source: https://leetcode.com/problems/valid-parentheses/

// directions:
// Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Note that an empty string is also considered valid.

const s = "{[]}";

function isValid(s) {
  let sArr = [...s];
  let stack = [];

  for (let char of sArr) {
    debugger;
    if (char === "[") stack.push("]");
    else if (char === "{") stack.push("}");
    else if (char === "(") stack.push(")");
    else if (stack.length === 0 || char !== stack.pop()) return false;
  }
  if (stack.length === 0) return true;
  return false;
}

console.log(isValid(s));
