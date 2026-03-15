# Solution 2 - 1005 runtime and 100% memory
# Single monotonic stack solution
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            _, prev_span = self.stack.pop()
            span += prev_span

        self.stack.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Solution 1 - 100% runtime and 98.63% memory
# Monotnic implementation through an indices stack
class StockSpanner:

    def __init__(self):
        self.prices=[] # store the prices
        self.indices=[] # maintain the largest numbers in the order that they appear

    def next(self, price: int) -> int:
        index=len(self.prices)
        # span = 1
        # if self.prices and price>=self.prices[-1]:
        while self.indices and price>=self.prices[self.indices[-1]]:
            self.indices.pop()
        span = index+1 if not self.indices else index - self.indices[-1]
        self.indices.append(index)
        self.prices.append(price)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)