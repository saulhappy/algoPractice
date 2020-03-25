/* 
Create a function that can take a multi dimensional array of Pixels and output how many shapes are present. Pixels will be either black or white. 
A shape is defined as a contiguous pattern of one or more black pixels in 4 dimensions: up, down, left, right, and not diagonal.
Example: matrix below has 2 shapes,
*/

const points = [
  ["b", "w", "b", "b", "b"],
  ["b", "w", "b", "w", "w"],
  ["b", "w", "b", "b", "b"]
];

function shapes(points) {
  let shapeCtr = 0;
  let pointsVisited = {};

  for (let row = 0; row < points.length; row++) {
    for (let col = 0; col < points[row].length; col++) {
      if (checkPoint(row, col, points, pointsVisited)) {
        shapeCtr++; // <- right here
      }
    }
  }
  return shapeCtr;
}

function checkPoint(row, col, points, pointsVisited) {
  if (position_invalid(row, col, points)) {
    return false;
  }
  let position = `${row}-${col}`;

  if (pointsVisited[position] === true) {
    return false;
  }

  // Check if this is in a shape
  const is_shape = points[row][col] === "b";
  pointsVisited[position] = true;

  if (is_shape) {
    checkPoint(row, col - 1, points, pointsVisited);
    checkPoint(row, col + 1, points, pointsVisited);
    checkPoint(row + 1, col, points, pointsVisited);
  }

  return is_shape;
}

function position_invalid(row, col, points) {
  if (row < 0 || col < 0) {
    return true;
  }

  if (row >= points.length || col >= points[row].length) {
    return true;
  }
}

console.log(shapes(points));
