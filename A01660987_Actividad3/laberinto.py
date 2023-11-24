import tkinter as tk
import random

N = 50

laberinto = []
for i in range(N):
    row = []
    for j in range(N):
        if i == N - 1 and j == 0:
            row.append(1)
            continue
        if i == 0 and j == N - 1:
            row.append(1)
            continue
        k = random.random()
        if k < 0.20:
            row.append(0)
        else:
            row.append(1)
    laberinto.append(row)

def valid(x, y, arreglo):
    if x < 0 or x >= N or y < 0 or y >= N or arreglo[y][x] != -2:
        return False
    else:
        return True
    
def valid2(x, y, arreglo):
    if x < 0 or x >= N or y < 0 or y >= N or arreglo[y][x] == -1:
        return False
    else:
        return True

def floodFill(x, y, arreglo):
    queue = []
    n = 0
    queue.append([x, y, n])
    arreglo[y][x] = n

    while queue:
        pos = queue.pop(0)
        posX = pos[0]
        posY = pos[1]
        n = pos[2] + 1

        if valid(posX + 1, posY, arreglo):
            arreglo[posY][posX + 1] = n
            queue.append([posX + 1, posY, n])
        
        if valid(posX - 1, posY, arreglo):
            arreglo[posY][posX - 1] = n
            queue.append([posX - 1, posY, n])

        if valid(posX, posY + 1, arreglo):
            arreglo[posY + 1][posX] = n
            queue.append([posX, posY + 1, n])

        if valid(posX, posY - 1, arreglo):
            arreglo[posY - 1][posX] = n
            queue.append([posX, posY - 1, n])

    return arreglo

arreglo = []
for i in range(N):
    row = []
    for j in range(N):
        if laberinto[i][j] == 0:
            row.append(-1)
        else:
            row.append(-2)
    arreglo.append(row)

arreglo = floodFill(N - 1, 0, arreglo)

def navegar(arreglo):
    x = 0
    y = N - 1
    n = arreglo[y][x]
    camino = [[x, y]]
    while n != 0:
        vecinos = []
        if valid2(x + 1, y, arreglo) and arreglo[y][x + 1] < n:
            vecinos.append([x + 1, y, arreglo[y][x + 1]])
        if valid2(x - 1, y, arreglo) and arreglo[y][x - 1] < n:
            vecinos.append([x - 1, y, arreglo[y][x - 1]])   
        if valid2(x, y + 1, arreglo) and arreglo[y + 1][x] < n:
            vecinos.append([x, y + 1, arreglo[y + 1][x]])
        if valid2(x, y - 1, arreglo) and arreglo[y - 1][x] < n:
            vecinos.append([x, y - 1, arreglo[y - 1][x]])
        if not vecinos:
            return camino
        vecinos.sort(key=lambda x: x[2])
        x = vecinos[0][0]
        y = vecinos[0][1]
        n = vecinos[0][2]
        camino.append([x, y])
    return camino

camino = navegar(arreglo)
       
# representación gráfica del laberinto
screen = tk.Tk()

CELL = 20
SIZE = N*CELL

canvas = tk.Canvas(screen, width=SIZE, height=SIZE, bg="white")
canvas.pack()

for i in range(1, N):          # se dibuja la cuadrícula
    canvas.create_line(i*CELL, 0, i*CELL, SIZE, fill="#e3e3e3")
for i in range(1, N):
    canvas.create_line(0, i*CELL, SIZE, i*CELL, fill="#e3e3e3")


while camino:
        pos = camino.pop(0)
        canvas.create_rectangle(pos[0]*CELL, pos[1]*CELL, pos[0]*CELL+CELL, pos[1]*CELL+CELL, fill="red")

for i in range(N):
    for j in range(N):
        if laberinto[i][j] == 0:
            canvas.create_rectangle(j*CELL, i*CELL, j*CELL+CELL, i*CELL+CELL, fill="black")


screen.mainloop()