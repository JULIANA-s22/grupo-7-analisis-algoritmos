class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        OPTIMIZADA - se usa el set para recordar los nuemeros vistos
        
        - se tiene Tengo un set vacío.
        - Para cada número:
          * Si ya lo vi antes es porque ya esta en el set 
          * Si no, lo guardo en el set

        COMPLEJIDAD:
        - TIEMPO: O(n): solo se hace un solo recorido
        - ESPACIO: O(n): puede que en el peor de los caso todos únicos
        - Rápida siempre

        """
        vistos = set()
        for num in nums:
            if num in vistos:
                return True
            vistos.add(num)
        return False