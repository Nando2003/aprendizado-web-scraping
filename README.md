# Emissão DARJ
Essa pequena automação foi feita para acessar o site [portal de pagamentos da fazenda do Rio de Janeiro](https://www1.fazenda.rj.gov.br/portaldepagamentos) e gera uma DARJ.

# Tecnologias usadas
- Selenium: Para abrir o navegador e navegar dentro da pagína através de XPATH.
- PyAutoGui: Para clicar em botões que estão fora da web para salvar os PDFs gerados.
- Python-Dotenv: Para armazenar os CNPJs em variáveis de ambiente.
# Como instalar?
Primeiramente, clone este repositório e crie no mesmo diretorio um arquivo .env com a variavel de ambiente CNPJS que armazenará os CNPJS das empresas que você deseja gerar o DARJ.
Segundamente, crie um ambiente virtual dentro desse diretorio:
```bash
$ python -m venv venv
```
Após cria-lo, ative-o:
```bash
$ source venv/Scripts/activate
```
Agora é só baixar as dependencias (libraries):
```bash
$ pip install -r requirements.txt
```

# Como usar?
A patir das etapas realizadas no tópico anterior, agora é só rodar.
```bash
$ python main.py 
```
> OBS: Faça isso estando com o venv ativo
