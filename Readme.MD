# TaskFlow – API de Gerenciamento de Tarefas

Um sistema básico de **gerenciamento de tarefas pessoais**, ideal para treinar **rotas**, **modelos**, **autenticação** e **integração com banco de dados** usando **FastAPI**.

## Objetivo do Projeto

- Criar usuários e autenticar com token.
- Criar, listar, atualizar e excluir tarefas.
- Filtrar tarefas por status (pendente, em andamento, concluída).


### Estrutura das Rotas

Dividir as rotas em arquivos dentro da pasta `routers` ajuda a manter o projeto limpo e escalável.

- **auth.py** → login, registro  
- **tasks.py** → CRUD das tarefas  
- **users.py** → perfil e configurações

### Autenticação JWT

A autenticação será feita por **JWT (JSON Web Token)**, garantindo segurança e controle de acesso.

Fluxo:
1. O usuário se registra com email e senha.
2. A senha é **criptografada** e armazenada no banco.
3. No login, o servidor retorna um **token JWT**.
4. Apenas usuários autenticados poderão acessar rotas protegidas (como criar ou listar tarefas).


## Etapas de Desenvolvimento

1. **Definir cada rota** de usuários e tarefas.  
2. **Modelar o banco de dados** (User e Task).  
3. **Implementar autenticação** (hash e JWT).  
4. **Criar o CRUD** completo das tarefas.  
5. **Adicionar validações** com Pydantic.


## Tecnologias Utilizadas

- **FastAPI** → Framework backend principal.  
- **SQLAlchemy** → ORM para manipular o banco de dados.  
- **SQLite** → Banco de dados leve para desenvolvimento local.  
- **Pydantic** → Validação e tipagem de dados.  
- **JWT (PyJWT)** → Autenticação e controle de acesso.  
- **Uvicorn** → Servidor ASGI para rodar a aplicação.  


## Como Rodar o Projeto

1. Criar e ativar um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows

2. Instalar dependencias:
    ```bash
    pip install -r requirements.txt

3. Executar o servidor:
    ```bash
    uvicorn app.main:app --reload

