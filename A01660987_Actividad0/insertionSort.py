from numpy import random

def insertionSort(size):
    array = random.randint(100, size=(size))
    n = 0
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1
            n += 1
    return "Tamaño: " + str(size) + " Pasos: " + str(n)

print(insertionSort(10))
print(insertionSort(100))
print(insertionSort(1000))
print(insertionSort(10000))