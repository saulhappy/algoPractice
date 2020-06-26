// source: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

// Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

// For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

// Example:

// Given the sorted array: [-10,-3,0,5,9],

// One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

//       0
//      / \
//    -3   9
//    /   /
//  -10  5

const T = require("./bst");
const BST = T.BST;

const nums = [-10, -3, 0, 5, 9];

function sortedArrayToBST(nums) {
  if (nums == null || !nums.length) {
    return null;
  }

  let mid = Math.floor(nums.length / 2);

  let node = new BST(nums[mid]);

  node.left = sortedArrayToBST(nums.slice(0, mid));
  console.log(nums);
  node.right = sortedArrayToBST(nums.slice(mid + 1, nums.length));
  console.log(nums);
  return node;
}

console.log(sortedArrayToBST(nums).root);
