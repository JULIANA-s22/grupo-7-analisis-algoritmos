class Solution(object):
    def canJump(self, nums):
        """

        JUSTIFICACION GREEDY:
        Para no necesitamos recordar todas las posiciones, solo saber
        cuál es la posición más lejana alcanzable hasta el momento.
        Si puedo llegar a la posición 5, ya sé que puedo llegar a 1,2,3,4.
        Con eso, reemplazamos todo por una sola variable 'alcance'

        COMPLEJIDAD:
        - Tiempo: O(n) — recorremos el arreglo una sola vez.
        - Espacio: O(1)
        """

        alcance = 0
        n = len(nums)

        for i in range(n):
            if i > alcance:
                return False
            if i + nums[i] > alcance:
                alcance = i + nums[i]
            if alcance >= n - 1:
                return True
        return False