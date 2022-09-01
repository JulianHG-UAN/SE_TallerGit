def main():
    n = int(input("introduce el valor de n: "))
    fact = 1

    if n < 0:
        print("El factorial no existe")
    elif n == 0:
        print("El factorial de 0 es 1")
    else:
        for i in range(1, n+1):
            fact *= i

        print(f"El factorial de {n} es {fact}")

if __name__ == "__main__":
    main()