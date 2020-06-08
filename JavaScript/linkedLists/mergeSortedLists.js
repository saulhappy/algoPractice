// source: https://leetcode.com/problems/merge-two-sorted-lists/

// Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

// Example:

// Input: 1->2->4, 1->3->4
// Output: 1->1->2->3->4->4

// const L = require("./customLinkedList");
// const List = L.LinkedList;
// const Node = L.Node;

// const l1 = new List();
// const l2 = new List();

// l1.insertLast(1);
// l1.insertLast(2);
// l1.insertLast(4);
// l2.insertLast(1);
// l2.insertLast(3);
// l2.insertLast(4);

// console.log(l1.printList(), l2.printList());

// function mergeTwoLists(l1, l2) {
// }

// console.log(mergeTwoLists(l1, l2));

function listNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

let l1 = new listNode(1);
const l1Head = l1;

l1.next = new listNode(2);
l1.next.next = new listNode(3);

while (l1) {
  console.log(l1.val);
  l1 = l1.next;
}

console.log(l1Head);
