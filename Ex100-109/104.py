
def lenint(string=""):

    while True:
        num = str(input(string))
        if num.isnumeric():
            return int(num)
        else:
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")

n = lenint("Digite um número: ")
print(f"Você acabou de digitar o número  {n}")