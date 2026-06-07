from time import sleep

def maior(*num):
    
    printt(30)
    for n in num:
        if not type(n) == int:
            print("Um dos valores não é um numero!")
            return 0
    
    print("Analisando valores passados...")
    
    for n in num:
        print(n, end=" ", flush=True)
        sleep(0.5)
    
    print(f"Foram informados {len(num)} valores ao todo." if len(num) != 1 else f"Foi informado {len(num)} valor ao todo.")
    print(f"O maior valor informado foi {max(num)}.") 

    return 1

def printt(vezes):
    print("=_="*vezes)


maior(10,20,4)
maior(2, 2, "três")
maior(0)

