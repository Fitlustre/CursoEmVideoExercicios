def escreva(texto):
    print("~"*(len(texto)+2))
    print(texto.center(len(texto)+2))
    print("~"*(len(texto)+2))


escreva("Olá Mundo!")
escreva("Curso de Python no Youtube")
escreva("CEV")
escreva(str(input("Escreva qualquer coisa: ")))