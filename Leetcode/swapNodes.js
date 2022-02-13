var swapPairs = function (head) {
  if (head.next === null) {
    return head;
  }
  if (head.next !== null && head !== null) {
    var p1 = head.val;
    head.val = head.next.valhead.next.cal = p1;
    if (head.next.next !== null) {
      head.next.next = swapPairs(head.next.next);
    }
  }
  return head;
};
