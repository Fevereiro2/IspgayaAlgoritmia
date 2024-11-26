def calcular_ia(nome_comprador, marca, modelo, cilindrada):
    if cilindrada <= 1250:
        taxa = 3.74
        parcelas = 2417.56
    else:
        taxa = 8.86
        parcelas = 8813.22

    ia = (taxa * cilindrada) - parcelas
    return ia


def main():
    nome_comprador = input("Qual é o nome do comprador? ")
    marca = input("Qual é a marca do veículo? ")
    modelo = input("Qual é o modelo do veículo? ")
    cilindrada = int(input("Qual é a cilindrada do motor? "))

    ia = calcular_ia(nome_comprador, marca, modelo, cilindrada)

    print(f"Nome do comprador: {nome_comprador}")
    print(f"Marca do veículo: {marca}")
    print(f"Modelo do veículo: {modelo}")
    print(f"Cilindrada do motor: {cilindrada} cm³")
    print(f"Imposto Automóvel (IA): {ia:.2f} €")


if __name__ == "__main__":
    main()
