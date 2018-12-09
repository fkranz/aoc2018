import sys
class Node(object):
 
    def __init__(self, data, prev, next):
        self.value = data
        self.prev = prev
        self.next = next


players = int(sys.argv[1])
marbels = int(sys.argv[2])
scores = [0]*players

zero = Node(0, None, None)
one = Node(1,zero,zero)
zero.next = one
zero.prev = one

current = one

for i in range(2,marbels+1):
    if i % 23 == 0:
        scores[(i-1)%players] += i
        for j in range(7):
            current = current.prev

        scores[(i-1)%players] += current.value

        current.next.prev = current.prev
        current.prev.next = current.next

        current = current.next   


    else:
        current = current.next
        newnode = Node(i, current, current.next)
        current.next.prev = newnode
        current.next = newnode

        current = newnode

print("Highscore is:", max(scores))
