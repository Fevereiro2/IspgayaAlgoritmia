def main():
    num = int(input("Digite um número entre 1 e 10: "))
    if 1 <= num <= 10:
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    else:
        print("Número inválido. Digite um número entre 1 e 10.")

if __name__ == "__main__":
    main()
