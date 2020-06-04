// source: https://leetcode.com/problems/add-two-numbers/

const L = require("./customLinkedList");
const List = L.LinkedList;
const Node = L.Node;

const l = new List();

l.insertFirst(3);
l.insertFirst(2);
l.insertFirst(1);

console.log(l.printList());
