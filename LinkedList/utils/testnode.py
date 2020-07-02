from node import ListNode

head = None

# Add five nodes to the beginning of the linked structure
for count in range(1, 6):
    head = ListNode(count, head)

# Print the contents of the structure
while head is not None:
    print(head.val)
    head = head.next_


lyst = [11, 12, 13, 14, 15]
lyst_reversed = list(reversed(lyst))

head2 = None
for i in lyst_reversed:
    head2 = ListNode(i, head2)

while head2:
    print(head2.val)
    head2 = head2.next_