class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}
class LinkedList {
  constructor() {
    this.head = null;
  }
  insertFirst(data) {
    this.head = new Node(data, this.head);
  }
  size() {
    let counter = 0;
    let node = this.head;
    while (node) {
      counter++;
      node = node.next;
    }
    return counter;
  }
  getFirst() {
    return this.head;
  }
  getLast() {
    if (!this.head) {
      return null;
    }
    let node = this.head;
    while (node) {
      if (!node.next) {
        return node;
      }
      node = node.next;
    }
  }
  clear() {
    this.head = null;
  }
  removeFirst() {
    if (!this.head) {
      return null;
    }
    this.head = this.head.next;
  }
  removeLast() {
    if (!this.head) {
      return null;
    }
    if (!this.head.next) {
      this.head = null;
      return;
    }
    let prevNode = this.head;
    let node = this.head.next;
    while (node.next) {
      prevNode = node;
      node = node.next;
    }
    prevNode.next = null;
  }
  insertLast(data) {
    const last = this.getLast();
    if (last) {
      // there are nodes in the chain, point next prop of last one to new node
      last.next = new Node(data);
    } else {
      // chain is empty, create new node, set the head to it
      this.head = new Node(data);
    }
  }
  getAt(index) {
    let counter = 0;
    let node = this.head;
    if (!this.head) {
      return null;
    }
    while (node) {
      if (index === counter) {
        return node;
      }
      counter++;
      node = node.next;
    }
  }
  removeAt(index) {
    // SAUL SOLUTION - DIDN'T WORK
    //   if (!this.head) {
    //     return;
    //   }
    //   if (index === 0) {
    //     this.head = this.head.next;
    //     return
    //   }
    //   let prevNode = this.getAt(index - 1);
    //   let node = this.head;
    //   let nextNode = this.head.next;
    //   let counter = 0;
    //   while (node) {
    //     if (index === counter) {
    //       prevNode.next = nextNode;
    //       return
    //     }
    //     counter++;
    //     node = node.next;
    //   }
    // }
    // If there is nothing, no need to continue.
    if (!this.head) return;
    // If 'index' is 0, use .removeFirst() method.
    if (index === 0) {
      this.removeFirst();
      return;
    }
    // If there is no 'prevNode', no need to continue, invalid 'index'.
    const prevNode = this.getAt(index - 1);
    if (!prevNode) return;
    // If 'currNode' exists, 'prevNode' must exist.
    const currNode = this.getAt(index);
    currNode ? (prevNode.next = currNode.next) : (prevNode.next = null);
  }
  insertAt(data, index) {
    if (!this.head) {
      this.head = new Node(data);
      return;
    }
    // // SAUL ORIGINAL APPROACH FAILED 2 TESTS
    // const prevNode = this.getAt(index - 1);
    // const currNode = this.getAt(index);
    // const newNode = new Node(data);
    // const nextNode = this.getAt(index + 1);
    // if (currNode) {
    //   this.head = newNode;
    //   newNode.next = currNode;
    //   return;
    // }
    // if (index > 0) {
    //   prevNode.next = newNode;
    //   newNode.next = nextNode;
    //   return;
    // }
    // if (index > this.size()) {
    //   this.insertLast(data);
    //   return;
    // }
    if (index === 0) {
      this.head = new Node(data, this.head);
      return;
    }
    const prevNode = this.getAt(index - 1);
    const node = new Node(data, prevNode.next);
    prevNode.next = node;
  }
}
