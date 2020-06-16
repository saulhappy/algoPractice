// sum the elements of an array of integers  recursively

const arr = [1, 2, 3];

function sumArr(arr) {
  // using iteration:
  //   let sum = 0;
  //   for (let i = 0; i < arr.length; i++) {
  //     sum += arr[i];
  //   }
  //   return sum;

  // using recursion
  if (arr.length === 1) {
    return arr[0];
  } else {
    return arr.pop() + sumArr(arr);
  }
}

console.log(sumArr(arr));
