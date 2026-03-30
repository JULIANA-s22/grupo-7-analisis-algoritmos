class Solution(object):
    def numDecodings(self, s):
        """
        Estado DP usado: dp[i]
        dp[i] representa el número de formas de decodificar la cadena desde la posición i hasta el final.

        Complejidad:
        Tiempo: O(n), porque recorremos la cadena una sola vez y en cada posición hacemos operaciones constantes.
        Espacio: O(n), porque usamos un arreglo dp de tamaño n+1 para guardar los resultados de los subproblemas.
        """
        n = len(s)
        
        dp = [0] * (n + 1)

        dp[n] = 1
        
        for i in range(n - 1, -1, -1):
            
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                
                if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                    dp[i] += dp[i + 2]
        
        return dp[0]