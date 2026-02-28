class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        OPTIMIZADA - se va guardando el precio más bajo
        
        Paso a Paso:
        - Mantengo 'minimo_visto' = precio más barato hasta ahora
        - Para cada día:
          * Si hoy es MÁS barato actualizo minimo_visto
          * Si no, calculo ganancia = hoy - minimo_visto
          * por ultimo lo Guardo si es la mejor hasta ahora

        
        COMPLEJIDAD:
        - TIEMPO: O(n): solo se recorre una sola vez
        - ESPACIO: O(1): se manejan solo 2 variables
        - Siempre se valida rápido
        """
        if not prices:
            return 0
        
        minimo_visto = prices[0]
        max_ganancia = 0
        
        for precio in prices[1:]:
            if precio < minimo_visto:
                minimo_visto = precio  # Nuevo mínimo
            else:
                ganancia = precio - minimo_visto
                if ganancia > max_ganancia:
                    max_ganancia = ganancia
        
        return max_ganancia