#deque
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()
print(queue)

deque(['Michael', 'Terry', 'Graham'])
print(queue) 