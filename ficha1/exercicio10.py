def main():
    while True:
        num = int(input("Digite um número positivo (<= 0 para sair): "))
        if num <= 0:
            break
        num_str = str(num)
        qtd_algarismos = len(num_str)
        soma_algarismos = sum(int(digit) for digit in num_str)
        print(f"Número: {num}, Algarismos: {qtd_algarismos}, Soma dos Algarismos: {soma_algarismos}")

if __name__ == "__main__":
    main()
