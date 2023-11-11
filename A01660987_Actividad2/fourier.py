import numpy

def calcularTransformadaRapidaFourier(f, N):
    F = numpy.zeros(N, dtype=complex)
    if N == 1:
        return f
    W_n = numpy.exp(-2j*numpy.pi/N)
    W = 1
    f_par = f[::2]
    f_impar = f[1::2]
    A = calcularTransformadaRapidaFourier(f_par, N//2)
    B = calcularTransformadaRapidaFourier(f_impar, N//2)
    for k in range(N//2):
        F[k] = A[k] + W*B[k]
        F[k + N//2] = A[k] - W*B[k]
        W *= W_n
    return F

N = 16384
f = numpy.random.random(N)
print(f)

print(calcularTransformadaRapidaFourier(f, N))