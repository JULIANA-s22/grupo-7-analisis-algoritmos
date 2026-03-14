class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        JUSTIFICACION GREEDY:
        Si ordenamos por el valor fin de cada intervalo,el
        que termina más temprano siempre es el que va convenir conservar,
        porque le deja más espacio libre a los siguientes.
        Con eso, solo necesitamos una variable 'fin_actual' que rastrea
        hasta dónde llegamos, y contamos cuántos intervalos no hacen parte del proceso.

        COMPLEJIDAD:
        - Tiempo: O(n log n) por el ordenamiento inicial.
        - Espacio: O(1)
        """

        intervals.sort(key=lambda x: x[1])

        intervalos_eliminados = 0
        fin_actual = intervals[0][1]

        for i in range(1, len(intervals)):
            inicio_intervalo = intervals[i][0]
            fin_intervalo = intervals[i][1]
            if inicio_intervalo < fin_actual:
                intervalos_eliminados += 1
            else:
                fin_actual = fin_intervalo

        return intervalos_eliminados