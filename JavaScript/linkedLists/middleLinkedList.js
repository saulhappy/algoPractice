// source: https://leetcode.com/problems/middle-of-the-linked-list/

const L = require("./customLinkedList");
const List = L.LinkedList;
const Node = L.Node;

const l = new List();

l.insertLast(1);
l.insertLast(2);
l.insertLast(3);
l.insertLast(4);
l.insertLast(5);
// l.insertLast(6);

console.log(l.printList());

function middleNode(l) {
  let slow = l.getFirst();
  let fast = l.getFirst();

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  return slow;
}

console.log(middleNode(l));
