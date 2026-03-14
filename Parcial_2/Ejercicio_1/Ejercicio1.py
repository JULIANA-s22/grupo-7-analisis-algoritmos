class Solution(object):
    def findContentChildren(self, avaricia_ninos, tamanos_galletas):
        """
        JUSTIFICACIÓN GREEDY:

            Primero se ordenó la lista de avaricia de los niños (avaricia_ninos)
            y también la lista de tamaños de galletas (tamanos_galletas).
            Luego se empezó a comparar al niño con menor avaricia con la galleta
            más pequeña disponible.

            Si la galleta alcanzaba para satisfacer al niño, se consideró
            satisfecho, se aumentó el contador de ninos_satisfechos y se avanzó
            al siguiente niño y a la siguiente galleta.

            Si la galleta no alcanzaba, entonces solo se avanzó a la siguiente
            galleta para intentar con una más grande.

            COMPLEJIDAD:
            - Tiempo: O(n log n + m log m).
            - Espacio: O(1)
        """

        avaricia_ninos.sort()
        tamanos_galletas.sort()

        indice_nino = 0
        indice_galleta = 0
        ninos_satisfechos = 0

        while indice_nino < len(avaricia_ninos) and indice_galleta < len (tamanos_galletas):

            if tamanos_galletas[indice_galleta] >= avaricia_ninos[indice_nino]:
                ninos_satisfechos += 1
                indice_nino += 1
                indice_galleta += 1
            else:
                indice_galleta += 1

        return ninos_satisfechos