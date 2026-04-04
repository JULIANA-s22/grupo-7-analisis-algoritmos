class Solution(object):
    def lengthOfLIS(self, nums):
        """
        Estado DP: dp[i] = longitud de la subsecuencia
        creciente mas larga que termina en nums[i]
        Recurrencia: dp[i] = 1 + max(dp[j]) para todo j < i
        donde nums[j] < nums[i]
        Caso base: dp[i] = 1 para todo i
        Complejidad: Tiempo O(n^2), Espacio O(n)
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)