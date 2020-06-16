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
