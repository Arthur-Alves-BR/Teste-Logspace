### Os seguintes passos são necessários para executar o projeto:

1. Instalar o gerenciador de dependências [_poetry_](https://python-poetry.org/)
2. Clonar o repositório em um diretório de sua escolha
3. Abrir o arquivo _.env_ contido na pasta _teste_logspace_ e inserir sua _API KEY_
 
**Atenção:** Os comandos a seguir devem ser executados na pasta raíz do projeto

4. _poetry init_: cria o ambiente virtual
5. _poetry shell_: entra no ambiente virtual
6. _poetry install_: instala as dependências do projeto
7. _uvicorn test_logspace.main:app --port 8004_: inicia o servidor da API

Se tudo ocorreu conforme o esperado, a documentação da API, que pode ser utilizada como ferramenta de teste dos enpoints, estará disponível na seguinte URL: http://localhost:8004/docs

**Observação:** Após a primeira execução, apenas os passos 5 e 7 são necessários para rodar o projeto