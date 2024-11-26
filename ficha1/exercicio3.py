def main():
    a, b, c = float(input("Digite o lado a: ")), float(input("Digite o lado b: ")), float(input("Digite o lado c: "))
    if a + b > c and a + c > b and b + c > a:
        print("Equilátero" if a == b == c else "Isósceles" if a == b or a == c or b == c else "Escaleno")
    else:
        print("Não é um triângulo")

if __name__ == "__main__":
    main()