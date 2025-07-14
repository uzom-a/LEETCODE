class StockSpanner:

    def __init__(self):
        self.stack = []  # Each element is a pair: (price, span)


    def next(self, price: int) -> int:
        span = 1  # Current day always counts

        # Pop while the stack's top price is less than or equal to current price
        while self.stack and self.stack[-1][0] <= price:
            _, prev_span = self.stack.pop()
            span += prev_span

        self.stack.append((price, span))
        return span
    
#Time Complexity is amortized O(1)
#Space Complexity is O(n)
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)