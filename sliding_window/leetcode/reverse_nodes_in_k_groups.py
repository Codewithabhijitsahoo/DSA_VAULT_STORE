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

prev = None

# 10 → 20 → 30 → 40 → 50

t = 1
before = n1
temp = n1

while t < 2:
    temp = temp.next
    t += 1


k = 1

while temp and k <= 3:
    nxt = temp.next
    temp.next = prev
    prev = temp
    temp = nxt
    k += 1

j = prev

before.next.next = temp
before.next = prev


headd = n1

while headd:
    print(headd.data)
    headd = headd.next