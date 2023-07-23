class Solution:
    def getRowN(self, n):
        result = [1]
        ans = 1
        mult = n
        for j in range(n):
            ans = ans * mult
            ans = ans // (j+1)
            mult = mult - 1
            result.append(ans)
        return result

    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            result.append(self.getRowN(i))   

        return result 
    
           