class Solution(object):
    def maxProfit(self, prices):
        """
        JUSTIFICACION GREEDY:

        La idea del algoritmo es aprovechar cada vez que el precio sube de un día
        al siguiente. Para eso recorremos la lista `prices` y comparamos
        `precio_hoy` con `precio_ayer`.

        Si `precio_hoy` es mayor que `precio_ayer`, significa que hubo una subida
        de precio. Entonces calculamos la diferencia entre esos dos valores y
        la sumamos a `ganancia_total`.

        COMPLEJIDAD:
        - Tiempo: O(n)
        - Espacio: O(1)
        """
        ganancia_total = 0

        for i in range(1, len(prices)):
            precio_hoy = prices[i]
            precio_ayer = prices[i-1]

            if precio_hoy > precio_ayer:
                ganancia_total += precio_hoy - precio_ayer

        return ganancia_total