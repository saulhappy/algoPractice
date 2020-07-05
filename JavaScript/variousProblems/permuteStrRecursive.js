const str = "dog";

function findPerms(str) {
  if (str.length === 0) return "";
  if (str.length === 1) return [str];

  let result = [];

  for (let i = 0; i < str.length; i++) {
    const currentChar = str[i];
    const remainingChars = str.slice(0, i) + str.slice(i + 1);

    for (let permutation of findPerms(remainingChars)) {
      result.push(currentChar + permutation);
    }
  }
  return result;
}

console.log(findPerms(str));
