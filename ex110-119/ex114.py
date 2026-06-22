import urllib.request
import urllib.error

# Hoje em dia sites bloqueiam scripts automáticos então temos que "fingir" ser um navegador/browser normal
url = 'https://www.pudim.com.br' # Site
requisicao = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})#Máscara de browser
#Agora sim
try:
    site = urllib.request.urlopen(requisicao)
except urllib.error.URLError as erro:
    print(f'\033[31mO site não está acessível no momento. Erro: {erro} 🔴\033[m')
else:
    print('\033[32mConsegui acessar o site com sucesso! 🟢\033[m')