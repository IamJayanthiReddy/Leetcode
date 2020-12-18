"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
there are such that A[i] + B[j] + C[k] + D[l] is zero.
"""

class Solution:
    def fourSumCount(self, A,B,C,D):
        d = {}
        answer = 0

        for num in A:
            for num2 in B:
                d[num + num2] = d.get(num + num2, 0) + 1
        for num in C:
            for num2 in D:
                answer += d.get(-(num + num2), 0)
        return answer


A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
s =Solution()
print(s.fourSumCount(A,B,C,D))