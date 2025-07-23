from collections import deque
class MyStack:
    def __init__(self):
        self.queue = deque()
        self.queue_two = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.queue_two.appendleft(x)

    def pop(self) -> int:
        return self.queue_two.popleft()

    def top(self) -> int:
        return self.queue_two[0]

    def empty(self) -> bool:
        if not self.queue or not self.queue_two: #or because i did not pop from the first queue
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()