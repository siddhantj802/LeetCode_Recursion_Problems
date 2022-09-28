class Solution:
    def isPowerOfFour(self, n: int) -> bool:
         
            while n >= 1:
                if n == 1 :
                    return True
                if n!=4 and n in range(2,8):
                    return False
                
                if  n%2 != 0:
                     return False
                else:
                    return self.isPowerOfFour(n/4)
