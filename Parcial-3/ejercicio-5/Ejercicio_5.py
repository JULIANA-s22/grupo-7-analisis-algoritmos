class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        """
        Bitset con entero nativo de Python
        PASO A PASO:
        - PASO 1: calcular total; si es impar → False inmediato
        - PASO 2: target = total // 2
        - PASO 3: dp = 1  (bit 0 encendido = suma 0 alcanzable)
        - PASO 4: para cada num: dp |= (dp << num)
        - PASO 5: aplicar máscara (dp & mask) para no crecer infinito
        - PASO 6: verificar si bit 'target' está encendido: (dp >> target) & 1

        TIEMPO:  O(n x target / 64) — operaciones de bits en bloques de 64 bits
        ESPACIO: O(target / 64)     — un solo entero comprimido
        """

        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = 1

        mask = (1 << (target + 1)) - 1
        for num in nums:
            dp |= (dp << num)  
            dp &= mask         
        return bool((dp >> target) & 1);
