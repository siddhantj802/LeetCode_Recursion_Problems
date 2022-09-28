class Solution:
    def fib(self, n: int) -> int:
        assert n >= 0 and int(n) == n, "Error"
        if n in [0,1]:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
        
