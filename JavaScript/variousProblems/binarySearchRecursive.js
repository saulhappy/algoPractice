const arr = [1, 2, 4, 5, 7, 8, 9];
const n = 12;

function recursiveBinarySearch(n, arr) {
  let mid = Math.floor(arr.length / 2);

  if (arr.length === 1 && arr[0] != n) {
    return false;
  }

  if (n === arr[mid]) {
    return true;
  } else if (n < arr[mid]) {
    return recursiveBinarySearch(n, arr.slice(0, mid));
  } else if (n > arr[mid]) {
    return recursiveBinarySearch(n, arr.slice(mid));
  }
}

console.log(recursiveBinarySearch(n, arr));
