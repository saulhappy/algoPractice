// source: https://leetcode.com/problems/reverse-linked-list/

// Reverse a singly linked list.

// Example:

// Input: 1->2->3->4->5->NULL
// Output: 5->4->3->2->1->NULL

const L = require("./customLinkedList");
const List = L.LinkedList;
const Node = L.Node;

const l = new List();

const a = new Node(1);
const b = new Node(2);
const c = new Node(3);
const d = new Node(4);

l.head = a;
a.next = b;
b.next = c;
c.next = d;

console.log(l.size());
console.log(l.printList());

console.log(l.reverseList(a));
