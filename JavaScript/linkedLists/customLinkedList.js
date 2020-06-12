// --- Directions
// Implement classes Node and Linked Lists
// See 'directions' document

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
    // this works, but with code reuse, we could've done...
    // this.head = new Node(data, this.head);
    this.insertAt(data, 0);
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
    // this works, but with code re use, we could do...
    // if (!this.head) {
    //   return null;
    // }

    // let node = this.head;

    // while (node) {
    //   if (!node.next) {
    //     return node;
    //   }
    //   node = node.next;
    // }

    return this.getAt(this.size() - 1);
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
    while (node) {
      if (counter === index) {
        return node;
      }

      counter++;
      node = node.next;
    }
    return null;
  }

  removeAt(index) {
    // SAUL SOLUTION
    if (!this.head) {
      return;
    }
    if (index === 0) {
      this.head = this.head.next;
      return;
    }

    let prevNode = this.getAt(index - 1);
    let node = this.head;
    let nextNode = this.head.next;
    let counter = 0;
    let last = this.getLast();

    if (node === last) {
      prevNode.next = null;
    }

    if (index > this.size() - 1) {
      return;
    }

    while (node) {
      if (index === counter) {
        prevNode.next = nextNode;
        return;
      }
      counter++;
      node = node.next;
      nextNode = nextNode.next;
    }
  }

  // Instructor Solution
  //   if (!this.head) {
  //     return;
  //   }

  //   if (index === 0) {
  //     this.head = this.head.next;
  //     return;
  //   }

  //   const previous = this.getAt(index - 1);
  //   if (!previous || !previous.next) {
  //     return;
  //   }
  //   previous.next = previous.next.next;
  // }

  insertAt(data, index) {
    //insert at empty list
    if (!this.head) {
      this.head = new Node(data);
      return;
    }
    // insert at 0
    if (index === 0) {
      this.head = new Node(data, this.head);
      return;
    }
    // insert at out of bounds, make it last node
    if (index > this.size() - 1) {
      const lastNode = this.getLast();
      lastNode.next = new Node(data);
      return;
    }
    // all other cases
    const prevNode = this.getAt(index - 1);
    const node = new Node(data, prevNode.next);
    prevNode.next = node;
    return;
  }

  // prints the list items
  printList() {
    if (!this.head) {
      return;
    }

    let node = this.head;
    let str = "";

    while (node) {
      str += node.data + " ";
      node = node.next;
    }

    return str;
  }

  // delete node
  deleteNode(node) {
    node.data = node.next.data;
    node.next = node.next.next;
  }

  // reverse the list
  reverseList(head) {
    if (!head) {
      return head;
    }

    let stack = [];

    while (head) {
      stack.push(head);
      head = head.next;
    }

    let node = stack.pop();
    head = node;

    while (stack) {
      node.next = stack.pop();
      node = node.next;
    }

    node.next = null;

    return head;
  }
}

module.exports = { Node, LinkedList };
