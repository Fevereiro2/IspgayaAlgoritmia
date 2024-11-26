def main():
    mensagem, n = input("Digite a mensagem: "), int(input("Digite o número de repetições: "))
    for _ in range(n):
        print(mensagem)

if __name__ == "__main__":
    main()
