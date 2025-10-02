from bs4 import BeautifulSoup

arquivo_html_entrada = "pagina_completa.html"
arquivo_txt_saida = "artigos_lgpd.txt"

# 3.Lendo o arquivo HTML local
try:
    with open(arquivo_html_entrada, "r", encoding='utf-8') as f_html:
        html_content = f_html.read()
    soup = BeautifulSoup(html_content, 'lxml')

    # 4.Encontrando os artigos
    artigos = soup.find_all('p', class_='Artigo')
    if not artigos:
        print('Não foram encontrados artigos')
    # 5.Criando o TXT com os artigos
    else:
        with open(arquivo_txt_saida, "w", encoding='utf-8') as f_txt:
            for artigo in artigos:
                texto_limpo = artigo.get_text(strip=True)
                f_txt.write(texto_limpo)
                f_txt.write("\n\n")
        print(f"Os artigos foram salvos com sucesso no arquivo: '{arquivo_txt_saida}'")


except FileNotFoundError:
    print("\nERRO: O arquivo 'pagina_completa.html' não foi encontrado.")
    print("Por favor, execute o script 'downloader.py' primeiro.")
except Exception as e:
    print(f"\nOcorreu um erro inesperado durante a extração: {e}")