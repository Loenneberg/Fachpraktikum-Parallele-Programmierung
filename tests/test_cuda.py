from numba import cuda

# Überprüfen, ob eine GPU verfügbar ist
print(cuda.is_available())

# Infos über die verfügbare GPU
if cuda.is_available():
    print(cuda.gpus)
