from node import Node

head = None

# Add five nodes to the beginning of the linked structure
for count in range(1, 6):
    head = Node(count, head)

# Print the contents of the structure
while head != None:
    print(head.data)
    head = head.next


lyst = [11, 12, 13, 14, 15]
lyst_reversed = list(reversed(lyst))

head2 = None
for i in lyst_reversed:
    head2 = Node(i, head2)

while head2:
    print(head2.data)
    head2 = head2.next