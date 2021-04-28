// custom implementation of binary search tree

// 1. create a node class

class Node {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}

// create a bst class

class BST {
  constructor(data) {
    this.root = new Node(data);
    this.count = 1;
  }

  size() {
    return this.count;
  }

  insert(data) {
    this.count++;

    let newNode = new Node(data);

    function searchTree(node) {
      if (data < node.data) {
        // if data to be inserted is less than the current node, go left.
        if (!node.left) {
          // if there's an empty spot here, append the data to be inserted
          node.left = newNode;
        } else {
          // if there's already a node here, search the left side again with current node ...
          searchTree(node.left);
        }
      } else if (data > node.data)
        if (!node.right) {
          // if data to be inserted is greater than the current node, go right.
          // if there's an empty spot here, append the data to be inserted
          node.right = newNode;
        } else {
          // if there's already a node here, search the right side again with current node ...
          searchTree(node.right);
        }
    }
    // to initialize searching, call it with the root node...
    searchTree(this.root);
  }

  // traverse the left side until it finds the last leaf
  min() {
    let currentNode = this.root;

    while (currentNode.left) {
      currentNode = currentNode.left;
    }

    return currentNode.data;
  }

  // traverse the right side until it finds the last leaf

  max() {
    let currentNode = this.root;

    while (currentNode.right) {
      currentNode = currentNode.right;
    }
    return currentNode.data;
  }

  contains(data) {
    let currentNode = this.root;

    while (currentNode) {
      if (data === currentNode.data) return true;

      if (data < currentNode.data) {
        currentNode = currentNode.left;
      } else {
        currentNode = currentNode.right;
      }
    }
    return false;
  }

  // search algorithms

  // DFS: search branch-by-branch

  dfsInOrder() {
    // process order: left, root, right
    let result = [];

    function traverse(node) {
      if (node.left) traverse(node.left);
      result.push(node.data);
      if (node.right) traverse(node.right);
    }

    traverse(this.root);

    return result;
  }

  dfsPreOrder() {
    // process order: root, left, right
    let result = [];
    function traverse(node) {
      result.push(node.data);

      if (node.left) traverse(node.left);
      if (node.right) traverse(node.right);
    }

    traverse(this.root);

    return result;
  }

  dfsPostOrder() {
    // process order: left, right, root
    let result = [];
    function traverse(node) {
      if (node.left) traverse(node.left);
      if (node.right) traverse(node.right);
      result.push(node.data);
    }

    traverse(this.root);

    return result;
  }

  // BFS: search level-by-level
  bfs() {
    let result = [];
    let queue = [];

    queue.push(this.root);

    while (queue.length) {
      let currentNode = queue.shift();
      result.push(currentNode.data);

      if (currentNode.left) {
        queue.push(currentNode.left);
      }

      if (currentNode.right) {
        queue.push(currentNode.right);
      }
    }

    return result;
  }
}

module.exports = { Node, BST };

let t = new BST(15);

t.insert(10);
t.insert(17);
t.insert(3);
t.insert(16);
t.insert(22);

// console.log(t.size());
// console.log(t.min());
// console.log(t.max());
// console.log(t.contains(22));
// console.log(t.dfsInOrder());
console.log(t.dfsPreOrder());
// console.log(t.dfsPostOrder());
// console.log(t.bfs());
// in order values are: [3, 10, 15, 16, 17, 22]