from urllib.request import Request, urlopen
from urllib.error import URLError

url = 'http://pudim.com.br'

# Adiciona o cabeçalho de um navegador real para evitar o bloqueio 403
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

try:
    requisicao = Request(url, headers=headers)
    comunicacao = urlopen(requisicao)
except URLError:
    print('\033[31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
