class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        f = {}
        for x in arr:
            if x%k in f:
                f[x%k] += 1
            else:
                f[x%k] = 1
        
        for y in f.keys():
            if y == 0 and f[y] % 2 != 0:
                return False
            elif y != 0 and y != k-y:
                if f.get(y, 0) != f.get(k-y, 0):
                    return False
            elif y == k-y and f[y] % 2 != 0:
                return False
        
        return True
