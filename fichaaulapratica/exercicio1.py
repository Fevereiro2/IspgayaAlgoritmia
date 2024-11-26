def main():
    tempo = float(input("Digite um temperatura em graus: "))
    print("Muito Frio" if tempo < 5 else "Frio" if tempo >= 5 and tempo < 10 else "Ameno" if tempo >= 10 and tempo < 20 else "Quente "if tempo >= 20 and tempo < 30 else "Muito quente")

if __name__ == '__main__':
    main()