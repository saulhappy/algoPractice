const arr1 = [4, 4, 1, 3];
let arr1Obj = {};

for (let num in arr1) {
  arr1Obj[num] = arr1[num] + 1 || 1;
}
