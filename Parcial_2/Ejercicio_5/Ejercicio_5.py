from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        VERSIÓN ÓPTIMA - Greedy: sort por start y fusionar adyacentes
        PASO A PASO:
        - PASO 1: sort(key=start)
        - PASO 2: merged = [intervals[0]]
        - Para CADA current en intervals[1:]:
          - Si current[0] <= merged[-1][1]: extender merged[-1][1] = max()
          - Sino: append current
        
        TIEMPO: O(n log n) sort + O(n) pasada
        ESPACIO: O(n) merged

        """
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])  # PASO 1
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:  # Solapa
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
        
        return merged
