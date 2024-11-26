def main():
    pares = impares = 0
    while True:
        num = int(input("Digite um número (<= 0 para sair): "))
        if num <= 0:
            break
        pares += num % 2 == 0
        impares += num % 2 != 0
    print(f"Pares: {pares}, Ímpares: {impares}")

if __name__ == "__main__":
    main()
