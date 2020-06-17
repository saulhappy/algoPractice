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

class bst {
  constructor(data) {
    this.root = new Node(data);
    this.count = 0;
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

  min() {}

  max() {}

  contains() {}

  // search algorithms

  // DFS

  dfsInOrder() {}

  dfsPreOrder() {}

  dfsPostOrder() {}

  // BFS
  bfs() {}
}
