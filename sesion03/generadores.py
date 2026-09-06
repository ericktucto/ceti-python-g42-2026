def fib():
    a, b = 0, 1

    while True:
        a, b = b, a + b
        yield a

for numero in fib():
    print(numero)
    if numero > 200:
        break

def generador():
    #for n in range(10_000_000):
    for n in range(20):
        yield n

for numero in generador():
    print(numero)