import tkinter as tk

# arreglo que representa el laberinto; 0 representa un muro y 1 representa un espacio vacío

   #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
laberinto =  [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0], 
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0], 
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], 
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0], 
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0], 
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0], 
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], 
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

M = len(laberinto[0])
N = len(laberinto)

def valid(x, y, arreglo):
    if x < 0 or x >= M or y < 0 or y >= N or arreglo[y][x] != -2:
        return False
    else:
        return True
    
def valid2(x, y, arreglo):
    if x < 0 or x >= M or y < 0 or y >= N or arreglo[y][x] == -1:
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
    for j in range(M):
        if laberinto[i][j] == 0:
            row.append(-1)
        else:
            row.append(-2)
    arreglo.append(row)

arreglo = floodFill(13, 0, arreglo)

def navegar(arreglo):
    x = 0
    y = N - 1
    n = arreglo[y][x]
    camino = [[x, y]]
    while n != 0:
        vecinos = []
        if valid2(x + 1, y, arreglo):
            vecinos.append([x + 1, y, arreglo[y][x + 1]])
        if valid2(x - 1, y, arreglo):
            vecinos.append([x - 1, y, arreglo[y][x - 1]])   
        if valid2(x, y + 1, arreglo):
            vecinos.append([x, y + 1, arreglo[y + 1][x]])
        if valid2(x, y - 1, arreglo):
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
       

screen = tk.Tk()

width = M*30
height = N*30

canvas = tk.Canvas(screen, width=width, height=height, bg="white")
canvas.pack()

for i in range(1, M):
    canvas.create_line(i*30, 0, i*30, height, fill="#e3e3e3")
for i in range(1, N):
    canvas.create_line(0, i*30, width, i*30, fill="#e3e3e3")

while camino:
        pos = camino.pop(0)
        canvas.create_rectangle(pos[0]*30, pos[1]*30, pos[0]*30+30, pos[1]*30+30, fill="red")

for i in range(N):
    for j in range(M):
        if laberinto[i][j] == 0:
            canvas.create_rectangle(j*30, i*30, j*30+30, i*30+30, fill="black")
        elif laberinto[i][j] == 1:
            canvas.create_text(j*30+15, i*30+15, text=str(arreglo[i][j]), font=("Arial", 10))

screen.mainloop()