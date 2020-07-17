const s = "a3112131";
let sObj = {};

for (let i = 0; i < s.length; i += 2) {
  sObj[s[i]] = parseInt(s[i + 1]);
}

console.log(sObj);
