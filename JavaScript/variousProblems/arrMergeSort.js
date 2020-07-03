// source: Pathrise Tech Assessment
// Directions: merge two sorted arrays, with resulting array also sorted
// eg. a= [1, 2, 3], b = [2, 5, 6], result = [1, 2, 2, 3, 5, 6]
// assume lengths of array can be different with no null values

const a = [1, 2, 3];
const b = [2, 5, 6, 7];

// using two pointers
function arrMergeSort(a, b) {
  let result = [];
  let i = 0;
  let j = 0;
  let k = 0;

  while (i < a.length && j < b.length) {
    if (a[i] < b[j]) {
      result[k] = a[i];
      i++;
    } else {
      result[k] = b[j];
      j++;
    }
    k++;
  }

  while (i < a.length) {
    result[k] = result[i];
    i++;
    k++;
  }

  while (j < b.length) {
    result[k] = b[j];
    j++;
    k++;
  }
  return result;
}

console.log(arrMergeSort(a, b));
