def escreva(texto):
    tam = (len(texto)+4)
    print("~"*tam)
    print(texto.center(tam))
    print("~"*tam)


escreva("Olá Mundo!")
escreva("Curso de Python no Youtube")
escreva("CEV")
escreva(str(input("Escreva qualquer coisa: ")))