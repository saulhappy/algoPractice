const arr = [10, -30, 97, 0, 5];
// sortedArr = [-30, 10, 0, 5, 97]

function bubbleSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - i - 1; j++)
      if (arr[j] > arr[j + 1]) {
        const swap = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = swap;
      }
  }
  return arr;
}

console.log(bubbleSort(arr));
