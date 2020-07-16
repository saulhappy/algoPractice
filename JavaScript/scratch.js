const s = "helloooooworldddd";

function consecCounter(s) {
  let result = "";
  let counter = 1;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === s[i + 1]) {
      counter++;
    } else {
      result += s[i] + counter;
      counter = 1;
    }
  }
  return result;
}

console.log(consecCounter(s));
