const str = "saul";

// 2. Write a function to reverse a string using recursion.

function reverseString(str) {
  if (str.length === 0) {
    return "";
  } else if (str.length === 1) {
    return str;
  } else {
    return str[str.length - 1] + reverseString(str.slice(0, str.length - 1));
  }
}

console.log(reverseString(str));
