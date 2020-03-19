// --- Directions
// Given the root node of a tree, return
// an array where each element is the width
// of the tree at each level.
// --- Example
// Given:
//     0
//   / |  \
// 1   2   3
// |       |
// 4       5
// Answer: [1, 3, 2]

// algorithm: initialize two arrays, one with the root of the node with a "levelStop" added to the end
// to signal end of level called arr, and an widthCounter array with 0.
// while the arr is greater than 1, take the current node out
// if that node is "levelStop", push a 0 to the widthCounter, and place "levelStop" back at the end of the array
// otherwise, take all the children of that node and push it into arr
// then increment the last element of the widthCounter array

function levelWidth(root) {
  const arr = [root, "levelStop"];
  let widthCounter = [0];

  while (arr.length > 1) {
    const node = arr.shift();

    if (node === "levelStop") {
      widthCounter.push(0);
      arr.push("levelStop");
    } else {
      arr.push(...node.children);
      widthCounter[widthCounter.length - 1]++;
    }
  }
  return widthCounter;
}
