// class Node {
//   constructor(val, next = null, random = null) {
//       this.val = val;
//       this.next = next;
//       this.random = random;
//   }
// }

class Solution {
    /**
     * @param {Node} head
     * @return {Node}
     */
    copyRandomList(head: Node | null): Node {
        if (head === null) {
            return null;
        }
        const oldToCopy = new Map<Node | null, Node | null>();
        oldToCopy.set(null, null);

        let cur: Node | null = head;
        while(cur !== null) {
            oldToCopy.set(cur,new Node(cur.val));
            cur = cur.next;
        }
        let curr = head;
        while(curr !== null) {
            const copy = oldToCopy.get(curr);
            copy.next = oldToCopy.get(curr.next);
            copy.random = oldToCopy.get(curr.random);
            curr = curr.next;
        }
        return oldToCopy.get(head);
    }
}
