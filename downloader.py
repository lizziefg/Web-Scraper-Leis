import requests

# 1.Fazendo a requisição
url = "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange=v=b3;q=0.9',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
}

try:
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    response.encoding = 'iso-8859-1'

    # 2. Salvando o conteúdo em um arquivo local
    with open("pagina_completa.html", "w", encoding='utf-8') as f:
        f.write(response.text)
    
    print("\nSUCESSO!")
    print("O arquivo 'pagina_completa.html' foi salvo no diretório.")
    print("Por favor, verifique o arquivo para confirmar se o conteúdo da lei foi baixado.")

except Exception as e:
    print(f"\nOcorreu um erro durante o download: {e}")
