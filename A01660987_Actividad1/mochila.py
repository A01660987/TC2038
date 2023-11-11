import random as r
import sys

sys.setrecursionlimit(100000)   # Incrementar el límite de recursión de Python

def mochila(n, a, p, v, u, pmax, vmax, u_total, m, articulos_mochila):
    if not n or not pmax or not vmax:   # Terminar si ya no hay artículos o si se excedieron los límites
        return u_total, m, articulos_mochila
    max_u = max(u)  # Obtener el artículo con mayor utilidad
    max_index = u.index(max_u) # Obtener el índice del artículo con mayor utilidad
    if (pmax - p[max_index]) >= 0 or (vmax - v[max_index]) >= 0: # Revisar si el artículo cabe en la mochila
        m += 1
        articulos_mochila.append(a[max_index])
        u_total += max_u
        pmax -= p[max_index]
        vmax -= v[max_index]
    p.pop(max_index)    # Eliminar el artículo de las listas
    v.pop(max_index)
    u.pop(max_index)
    a.pop(max_index)
    n -= 1  
    return mochila(n, a, p, v, u, pmax, vmax, u_total, m, articulos_mochila)    # Llamada recursiva

def main():
    n = 100   # Número de artículos a generar
    a = [i for i in range(1, n + 1)]    # Lista de identificadores de artículos, de 1 a n
    p = [r.randint(1, 100) for i in range(n)]   # Listas de pesos, volúmenes y utilidades de los artículos, entre 1 y 100
    v = [r.randint(1, 100) for i in range(n)]
    u = [r.randint(1, 100) for i in range(n)]
    pmax = n*10     # Peso máximo y volumen máximo de la mochila, 10 veces el número de artículos
    vmax = n*10

    print("Número de artículos:", n)
    print("Lista de artículos:", a)
    print("Lista de pesos:", p)
    print("Lista de volúmenes:", v)
    print("Lista de utilidades:", u)
    print("Peso máximo:", pmax)
    print("Volumen máximo:", vmax)

    u_total, m, articulos_mochila = mochila(n, a, p, v, u, pmax, vmax, 0, 0, [])    # Llamada a la función mochila con los parámetros iniciales

    print("Número de artículos en la mochila:", m)
    print("Lista de artículos en la mochila:", articulos_mochila)
    print("Utilidad máxima obtenida:", u_total)

if __name__ == "__main__":
    main()