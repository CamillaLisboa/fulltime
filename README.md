# Finance
Controle de Finanças Doméstica

## Descrição
O Finance é um app para controle de finanças de um ambiente residencial, onde é possivel ver os dados das pessoas e suas rendas, e as contas e gastos da casa, além do balanço com o total de entrada e saida de caixa, através de um CRUD (Create, Read, Update, Delete).

## Funcionalidades
- Visualização dados pessoais e da gastos.
- Adição, edição e exclusão de pessoas e contas.
- Balanço de total de membros da família, total de renda bruta e liquida, e total de saida.

## Tecnologias Utilizadas
- Django
- PostgreSQL

## Configuração do Ambiente Local
1. Clone o repositório: `git clone https://github.com/CamillaLisboa/fulltime.git`
2. Crie e ative um ambiente virtual: `python -m venv env` e `source env/bin/activate` (ou use `Scripts\activate` no Windows).
3. Instale as dependências: `pip install -r requirements.txt`
4. Aplique as migrações: `python manage.py migrate`
5. Crie um superusuário: `python manage.py createsuperuser`
6. Inicie o servidor: `python manage.py runserver`

Acesse a aplicação em (http://localhost:8000/) e o painel de administração em (http://localhost:8000/admin/).

## Cadastro de Pessoas
1. Todos os campos são obrigatórios
2. Ao cadastrar o documento, NÃo utilizar nenhum ponto ou traço, somente números
3. A renda a ser cadastrada possui casa decimal no sistema americano, centavos separados por ponto ( . )

## Cadastro de Contas
1. Todos os campos são obrigatórios
2. O valor da fatura a ser cadastrada possui casa decimal no sistema americano, centavos separado por ponto ( . ) 

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, propor melhorias ou fazer pull requests.
