def main():
    peso, altura = float(input("Escreva o seu peso (kg): ")), float(input("Escreva a sua altura (m): "))
    imc = peso / (altura ** 2)
    print(f"IMC: {imc:.2f}", "Classificação:",
          "Abaixo do peso" if imc < 18.5 else
          "Peso normal" if imc < 25 else
          "Sobrepeso" if imc < 30 else "Obesidade")

if __name__ == "__main__":
    main()
