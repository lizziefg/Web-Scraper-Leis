#Web-Scraper de Leis Brasileiras

Este é um projeto desenvolvido para a disciplina de Linguagem de Programação II, com o objetivo de realizar a extração de dados (web scraping) do texto integral de leis hospedadas no portal do Planalto.

A versão atual do projeto está configurada para extrair o conteúdo da Lei Geral de Proteção de Dados (LGPD) - LEI Nº 13.709, DE 14 DE AGOSTO DE 2018, salvando todos os seus artigos num arquivo de texto limpo.

Arquitetura e Funcionamento
Para garantir robustez e facilitar a depuração (especialmente devido às inconsistências do servidor de origem), o projeto foi dividido em dois scripts principais, separando as responsabilidades de download e de extração.

downloader.py: Este script é responsável por se conectar ao servidor do Planalto e baixar o código-fonte HTML da página da lei. Ele foi cuidadosamente ajustado para:

Simular um navegador real através de headers, evitando bloqueios simples.

Lidar com a codificação de caracteres específica do servidor (iso-8859-1), convertendo o resultado para o padrão universal utf-8 para evitar erros com acentuação e símbolos.

Salvar o conteúdo HTML completo e corrigido no arquivo pagina_completa.html.

extrator.py: Este script trabalha de forma offline, lendo o arquivo pagina_completa.html gerado anteriormente. As suas responsabilidades são:

Analisar (fazer o parsing) o conteúdo HTML utilizando a biblioteca BeautifulSoup com o robusto parser lxml.

Identificar e extrair o texto de todos os parágrafos que pertencem à classe "Artigo", que corresponde aos artigos da lei.

Salvar o texto limpo e formatado no arquivo artigos_lgpd.txt.

Tecnologias Utilizadas
Python 3

Requests: Para realizar as requisições HTTP.

BeautifulSoup4: Para a análise e extração de dados do HTML.

lxml: Como o parser HTML para o BeautifulSoup, garantindo performance e robustez.

Como Executar o Projeto
Pré-requisitos:

Python 3.x instalado.

pip (gestor de pacotes do Python).

1. Clone o Repositório

git clone [https://github.com/seu-usuario/Web-Scraper-Leis.git](https://github.com/seu-usuario/Web-Scraper-Leis.git)
cd Web-Scraper-Leis

2. Crie e Ative um Ambiente Virtual (Recomendado)

# Windows
python -m venv .venv
.\.venv\Scripts\Activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

3. Instale as Dependências
Com o ambiente virtual ativado, instale as bibliotecas necessárias a partir do arquivo requirements.txt:

pip install -r requirements.txt

4. Execute o Downloader
Este passo irá baixar o HTML da lei e salvá-lo localmente.

python downloader.py

5. Execute o Extractor
Este passo irá ler o arquivo baixado e criar o .txt com os artigos.

python extrator.py

Ao final, o arquivo artigos_lgpd.txt estará no diretório do projeto com o texto completo da lei.

Próximos Passos (Roadmap)
Este projeto, embora funcional, foi construído como uma prova de conceito focada numa única lei. No futuro, pretendo evoluir o código para incluir as seguintes funcionalidades:

Entrada de URL pelo Utilizador: Modificar os scripts para que o utilizador possa fornecer qualquer link de uma lei do portal do Planalto via terminal, tornando a ferramenta flexível.

Nomes de Arquivo Dinâmicos: Gerar o nome do arquivo .txt de saída automaticamente com base no número ou nome da lei que está a ser extraída.

Unificação dos Scripts: Criar uma versão unificada e robusta do código que executa o download e a extração num único comando, mantendo as verificações de segurança para lidar com a instabilidade do servidor.