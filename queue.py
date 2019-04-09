from collections import deque


que = deque()
# push(右から)
for i in range(10):
    que.append(i)
print(que)

# pop(左から)
while len(que) > 0:
    print(que.popleft())