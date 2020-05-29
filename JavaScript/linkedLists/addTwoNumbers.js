// source: https://leetcode.com/problems/add-two-numbers/

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
  printList() {
    var curr = this.head;
    var str = "";
    while (curr) {
      str += curr.element + " ";
      curr = curr.next;
    }
    console.log(str);
  }
}

let l1 = new LinkedList((data = 2));

console.log(l1.printList());

// function addTwoNumbers(l1, l2) {}

// console.log(addTwoNumbers(l1, l2));
