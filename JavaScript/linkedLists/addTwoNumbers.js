// source: https://leetcode.com/problems/add-two-numbers/

const L = require("./customLinkedList");
const List = L.LinkedList;
const Node = L.Node;

const l = new List();

l.insertLast(1);
l.insertLast(2);
l.insertLast(3);
l.insertLast(4);
l.insertLast(5);

console.log(l.printList());
