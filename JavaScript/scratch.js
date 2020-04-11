const obj = {
  "2": 0,
  "7": 1,
  "11": 2,
};

let x = obj["7"];

for (let key in obj) {
  debugger;
  console.log(obj[key]);
}
