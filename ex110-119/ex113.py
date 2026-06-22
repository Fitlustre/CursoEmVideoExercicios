"""

"""


def lenint(string=""):

    while True:
        try:
            valor = int(input(string))
        except ValueError, TypeError:
            print("\033[31mERRO: por favor, digite um número INTEIRO válido.\033[m")
        except KeyboardInterrupt:
            print("\n\033[31mUtilizador preferiu não digitar esse número.\033[m")
            return 0
        else:
            return valor


def leiafloat(string=""):

    while True:
        try:
            valor = float(input(string))
        except ValueError, TypeError:
            print("\033[31mERRO: por favor, digite um número DECIMAL válido.\033[m")
        except KeyboardInterrupt:
            print("\n\033[31mUtilizador preferiu não digitar esse número.\033[m")
            return 0.0
        else:
            return valor


inteiro = lenint("Digite um número Inteiro: ")
decimal = leiafloat("Digite um número Decimal: ")

print(f"O valor inteiro digitado foi {inteiro} e o decimal foi {decimal}")
