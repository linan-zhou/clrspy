class Solution():
    def GaussianElimination(self,equation):
        n = len(equation)
        m = len(equation[0])
        for i in range(0, n-1):
            if equation[i][i] == 0:
                k = i
                while k < n and equation[k][i] == 0:
                    k += 1
                if k < n:
                    equation.insert(i, equation(k))
            for k in range(i+1, n):
                b = equation[k][i] / equation[i][i]
                for j in range(i, m):
                    equation[k][j] = equation[k][j]-b*equation[i][j]
        #完成上三角矩阵的转换，下面开始各个未知数求值
        ans = [0] * n
        for i in range(0, n):
            ans[n-1-i] = equation[n-1-i][m-1]
            for j in range(0, i):
                ans[n-1-i] -= ans[n-1-j]*equation[n-1-i][n-1-j]
            ans[n-1-i] = ans[n-1-i]/equation[n-1-i][n-1-i]
        return ans

s = Solution()
print(s.GaussianElimination([[2,3,1,11],[1,1,1,6],[1,-1,-1,-4]]))
