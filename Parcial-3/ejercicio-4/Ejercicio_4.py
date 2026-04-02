class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
   DP con 1 sola fila + variable diagonal
        PASO A PASO:
        - PASO 1: dp = [0] * (n+1), una sola fila
        - PASO 2: para cada i, recorremos j:
          - Guardamos diag = dp[j] ANTES de modificarlo (era dp[i-1][j-1])
          - Si coinciden:    dp[j] = diag + 1
          - Si no coinciden: dp[j] = max(dp[j], dp[j-1])
          - Actualizamos diag para la siguiente j

        TIEMPO:  O(m x n) — igual que siempre
        ESPACIO: O(n)     — una sola fila + variable auxiliar
        """
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            diag = 0  # representa dp[i-1][j-1]
            for j in range(1, n + 1):
                temp = dp[j]  # guardamos dp[i-1][j] antes de pisar
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = diag + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                diag = temp  # el antiguo dp[j] será el diagonal de la próxima j

        return dp[n]