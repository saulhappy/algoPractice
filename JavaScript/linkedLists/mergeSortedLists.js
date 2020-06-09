// source: https://leetcode.com/problems/merge-two-sorted-lists/

// Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

// Example:

// Input: 1->2->4, 1->3->4
// Output: 1->1->2->3->4->4

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

let l1 = new ListNode(1);
const l1Head = l1;
l1.next = new ListNode(2);
l1.next.next = new ListNode(4);

let l2 = new ListNode(1);
const l2Head = l2;
l2.next = new ListNode(3);
l2.next.next = new ListNode(4);

// while (l1 || l2) {
//   console.log(l1.val, l2.val);
//   l1 = l1.next;
//   l2 = l2.next;
// }

function mergeTwoLists(l1, l2) {
  let dummy = new ListNode(0);
  let head = dummy;

  while (l1 && l2) {
    if (l1.val <= l2.val) {
      dummy.next = l1;
      l1 = l1.next;
    } else {
      dummy.next = l2;
      l2 = l2.next;
    }
    dummy = dummy.next;
  }

  if (l1) {
    dummy.next = l1;
  } else {
    dummy.next = l2;
  }

  //   while (head) {
  //     console.log(head.val);
  //     head = head.next;
  //   }

  return head.next;
}

console.log(mergeTwoLists(l1, l2));
