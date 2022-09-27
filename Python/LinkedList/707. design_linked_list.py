

class ListNode:
    def __init__(self, val: int):
        self.next = None
        self.val = val


class MyLinkedList:
    def __init__(self):
        self._dummy_head = ListNode(0)
        self._len = 0

    def get(self, index: int) -> int:
        if index < 0 or index > self._len - 1:
            return -1

        cur = self._dummy_head.next
        while index:
            cur = cur.next
            index -= 1

        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self._dummy_head.next
        self._dummy_head.next = new_node
        self._len += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)

        cur = self._dummy_head
        while cur.next is not None:
            cur = cur.next

        cur.next = new_node
        self._len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self._len or index < 0:
            return

        new_node = ListNode(val)

        cur = self._dummy_head
        while index:
            cur = cur.next
            index -= 1

        new_node.next = cur.next
        cur.next = new_node
        self._len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self._len - 1 or index < 0:
            return

        cur = self._dummy_head

        while index:
            cur = cur.next
            index -= 1

        cur.next = cur.next.next
        self._len -= 1

    def travel_listed_list(self):
        cur = self._dummy_head
        while cur.next is not None:
            print(cur.next.val, end=" ")
            cur = cur.next


if __name__ == "__main__":
    obj = MyLinkedList()

    obj.addAtHead(1)
    obj.addAtHead(2)
    obj.addAtTail(10)
    obj.addAtIndex(1, 3)
    obj.addAtIndex(1, 4)
    obj.deleteAtIndex(1)
    obj.travel_listed_list()
    print("\n")
    val = obj.get(0)
    print(val)
