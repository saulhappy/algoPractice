const str = "saul";

function revStr(str) {
  // one liner:
  return [...str].reverse().join("");

  // or iteration:
  //   let revStr = "";

  //   for (let i = 0; i < str.length; i++) {
  //     revStr = str[i] + revStr;
  //   }

  //   return revStr;
}

console.log(revStr(str));
