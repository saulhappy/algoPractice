const arr = [1, 2, 4, 5, 7, 8, 9];
const n = 12;

function binarySearch(n, arr) {
  let midpoint = Math.floor(arr.length / 2);

  if (arr.length === 0 && arr[0] != n) {
    return false;
  }

  if (n === arr[midpoint]) {
    return true;
  } else if (n < arr[midpoint]) {
    return binarySearch(n, arr.slice(0, midpoint));
  } else if (n > arr[midpoint]) {
    return binarySearch(n, arr.slice(midpoint));
  }
}

console.log(binarySearch(n, arr));
