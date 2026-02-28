"""
Ejercicio 4: Cuenta piedras adyacentes IGUALES que hay que quitar
 
Paso a Paso:
- Leo n y la cadena s
- Se hace el recorrido desde la segunda piedra hasta la última
- Cada vez que s[i] == s[i-1] se incrementa +1
- Al se imprime el total
 
 
COMPLEJIDAD:
- TIEMPO: O(n): se hace solo una pasada por la cadena
- ESPACIO: O(1): solo usamos un contador
- Mejor/peor caso: siempre O(n)
 
"""
 
n = int(input())        
s = input().strip()   
 
contador = 0            
for i in range(1, n):   
    if s[i] == s[i-1]: 
        contador += 1   
 
print(contador)         