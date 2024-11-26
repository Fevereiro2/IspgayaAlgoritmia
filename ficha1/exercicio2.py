def main():

    a, b, c = float(input("Digite o lado a: ")), float(input("Digite o lado b: ")), float(input("Digite o lado c: "))
    if a + b > c and a + c > b and b + c > a:
        print("Os números podem ser os lados de um triângulo.")
    else:
        print("Os números NÃO podem ser os lados de um triângulo.")

if __name__ == "__main__":
    main()