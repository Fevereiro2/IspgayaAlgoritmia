def main():
    soma = count = 0
    while True:
        num = float(input("Digite um número (0 para terminar): "))
        if num == 0:
            break
        soma += num
        count += 1
    media = soma / count if count > 0 else 0
    print(f"Média: {media:.2f}")

if __name__ == "__main__":
    main()
