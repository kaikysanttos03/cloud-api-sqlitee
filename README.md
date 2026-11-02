# Cloud API - SQLite

## Sobre o projeto

Este projeto consiste no desenvolvimento de uma API REST utilizando Python e Flask, integrada a um banco de dados SQLite e preparada para hospedagem em ambiente de computação em nuvem.

A aplicação permite realizar o gerenciamento de usuários por meio das operações CRUD (Create, Read, Update e Delete).

## Tecnologias utilizadas

- Python 3.13.7
- Flask 3.1.3
- Werkzeug 3.1.9
- SQLite
- Visual Studio Code
- Microsoft Azure (hospedagem planejada)

## Funcionalidades

- Cadastro de usuários.
- Listagem de usuários.
- Consulta individual por ID.
- Atualização de informações.
- Exclusão de usuários.
- Validação de dados.
- Tratamento de erros e duplicidade de e-mail.

## Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| GET | / | Verificar funcionamento da API |
| POST | /usuarios | Cadastrar usuário |
| GET | /usuarios | Listar usuários |
| GET | /usuarios/{id} | Consultar usuário |
| PUT | /usuarios/{id} | Atualizar usuário |
| DELETE | /usuarios/{id} | Excluir usuário |

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual no Windows

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Executar a aplicação

```bash
python run.py
```

A API estará disponível em:

http://127.0.0.1:5000

## Banco de dados

O projeto utiliza SQLite para armazenar os dados dos usuários. A tabela é criada automaticamente durante a inicialização da aplicação.

## Status do projeto

API desenvolvida e testada localmente. Publicação no GitHub e implantação na infraestrutura Microsoft Azure previstas como próximas etapas.

## Autor

Kaiky Silva dos Santos