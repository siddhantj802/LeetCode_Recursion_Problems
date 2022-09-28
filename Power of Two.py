class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n >= 1:
            if n == 1 :
                return True
                
            if n != 1 and n%2 != 0:
                return False
            
             
            else:
                return self.isPowerOfTwo(int(n/2))
        
