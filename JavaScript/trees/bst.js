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
}
