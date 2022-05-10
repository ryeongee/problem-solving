class Solution:
    def kWeakestRows(self, mat, k):
        ans = {}
        for i in range(len(mat)):
            ans[i] = sum(mat[i])
        ans = sorted(ans, key=ans.get)
        return ans[:k]
