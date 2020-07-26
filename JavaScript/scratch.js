const A = ["a", "a"];
const B = ["a", "a", "b"];

const isSameChar = (currentChar) => currentChar === A[0];

console.log(A.every(isSameChar) === B.every(isSameChar));
