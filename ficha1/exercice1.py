def main():
    a, b, c = int(input()), int(input()), int(input())

    maior = a if a > b and a > c else b if b > c else c
    print(maior)

if __name__ == '__main__':
    main()