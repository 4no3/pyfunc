from collections import deque


stk = deque()
# push(右から)
for i in range(10):
    stk.append(i)
print(stk)

# pop(右から)
while len(stk) > 0:
    print(stk.pop())
