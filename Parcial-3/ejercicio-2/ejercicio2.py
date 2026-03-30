class Solution:
    def wordBreak(self, s, wordDict):
        """
        Estrategia DP:
        Usamos un arreglo dp donde dp[i] indica si el prefijo s[0:i]
        puede segmentarse en palabras del diccionario.

        Justificacion:
        Si existe un punto j < i tal que dp[j] es True y s[j:i] esta
        en el diccionario, entonces dp[i] tambien es True.

        Caso base: dp[0] = True (cadena vacia es segmentable).
        Respuesta: dp[n] indica si toda la cadena se puede segmentar.

        Complejidad:
        Tiempo: O(n^2) por evaluar todos los cortes posibles.
        Espacio: O(n) para el arreglo dp y el set del diccionario.
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]