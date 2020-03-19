// --- Directions
// Return the 'middle' node of a linked list.
// If the list has an even number of elements, return
// the node at the end of the first half of the list.
// *Do not* use a counter variable, *do not* retrieve
// the size of the list, and only iterate
// through the list one time.
// --- Example
//   const l = new LinkedList();
//   l.insertLast('a')
//   l.insertLast('b')
//   l.insertLast('c')
//   midpoint(l); // returns { data: 'b' }

function midpoint(list) {
  let slow = list.head;
  let fast = list.head;

  while (fast.next && fast.next.next) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow;
}

// LOGIC
// if the fast node, moving two nodes at a time gets to a point where its at the end of the list
// or one step behind the end of the list, then that means it's at or near the end of the list
// and then the slow node must be at the mid point because it's moving at half the speed as
// the fast node.
