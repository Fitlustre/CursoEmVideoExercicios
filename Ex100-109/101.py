
def voto(ano_de_nascimento=False):
    """
    param \033[33mano_de_nascimento\033[m: recebe um valor inteiro representando o ano de nascimento de uma pessoa
                                            se estiver falso

    essa função devolve uma string com:
    - VOTO NEGADO
    - VOTO OPCIONAL
    - VOTO OBRIGATÓRIO
    """
    from datetime import datetime 


    txt_error_idade = "Erro, ano de nascimento inválido."
    txt_error_ano = "Erro, ano de nascimento não encontrado"
    
    if not ano_de_nascimento or not type(ano_de_nascimento) == int:
            return   txt_error_ano
    
    idade = int(datetime.now().year) - ano_de_nascimento
    txt = f"Com {idade} anos: "
    
    if idade < 0:          return txt_error_idade
    elif 18 <= idade < 65: return f"{txt} VOTO OBRIGATÓRIO."
    elif 120 >= idade > 61 or 16 <= idade < 18:       
                           return f"{txt} VOTO OPCIONAL."
    elif 0 <= idade <  18: return f"{txt} VOTO NEGADO."
    elif idade > 120:      return txt_error_idade
    else:                  return f"Erro desconhecido"


# =====Execução=====
print("-"*40)
op = voto(int(input("Em que ano você nasceu? ")))
print(op)

if "VOTO" in op:
    print(op)