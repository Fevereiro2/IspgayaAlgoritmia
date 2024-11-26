def main():
    soma = 0
    for _ in range(10):
        soma += float(input("Digite um número: "))
    print(f"Média: {soma / 10:.2f}")

if __name__ == "__main__":
    main()
