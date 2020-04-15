const obj = {
  one: ["1", "uno"],
  two: 1,
  three: 2,
};

obj.two = "cuatro!";

console.log([3] == [3]);

console.log(obj.two);

const x = 6 % 2;

console.log(x);

let s1Arr = s1.split("");
let s2Arr = s2.split("");
let matchCounter = 0;

for (let char of s1Arr) {
  if (s2Arr.includes(char)) {
    matchCounter++;
  }
}

if (matchCounter > 0) {
  return "YES";
} else {
  return "NO";
}
