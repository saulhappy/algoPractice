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

  size() {
    let counter = 0;
    let node = this.head;

    while (node) {
      counter++;
      node = node.next;
    }
    return counter;
  }

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
}

const a = new Node(1);
const b = new Node(2);
const c = new Node(3);
const d = new Node(4);

l = new LinkedList();

l.head = a;
a.next = b;
b.next = c;
c.next = d;

console.log(l.size());
console.log(l.printList());
