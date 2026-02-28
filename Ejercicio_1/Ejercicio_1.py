class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Optimizada - Se realiza el cuento de las letras que compone cada palabra
        
        paso a paso:
        1. Chequeo largo primero
        2. El Counter cuenta cuántas 'a', 'b', 'c'... tiene cada palabra  
        3. por ultimo se comparan los contadores
             
        COMPLEJIDAD:
        - TIEMPO: O(n): solo se recore una sola vez
        - ESPACIO: O(1) → máximo 26 letras
        - Todos los casos son rápidos
        """
        if len(s) != len(t):
            return False
        from collections import Counter  
        return Counter(s) == Counter(t)