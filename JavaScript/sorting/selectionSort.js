const arr = [10, 0, 97, -30, 5];
// sortedArr = [-30, 10, 0, 5, 97]

function selectionSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    let indexOfMin = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[indexOfMin]) {
        indexOfMin = j;
      }
    }
    if (i !== indexOfMin) {
      const swap = arr[i];
      arr[i] = arr[indexOfMin];
      arr[indexOfMin] = swap;
    }
  }
  return arr;
}

console.log(selectionSort(arr));
