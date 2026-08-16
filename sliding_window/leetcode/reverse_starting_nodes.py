class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# 10 → 20 → 30 → 40 → 50

prev = None
t = 1
before = n1
temp = n1

# starting position
start = 1

while t < start:
    before = temp
    temp = temp.next
    t += 1

# number of nodes to reverse
k = 3

while temp and k >= 1:
    nxt = temp.next
    temp.next = prev
    prev = temp
    temp = nxt
    k -= 1

# reconnect
if start == 1:
    n1.next = temp
    head = prev
else:
    before.next = prev
    before.next.next = temp
    head = n1

# print
headd = head

while headd:
    print(headd.data, end=" ")
    headd = headd.next