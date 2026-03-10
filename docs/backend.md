# ColaboraMais — Backend Documentation

## Visão Geral

O **ColaboraMais** é um sistema interno de comunicação estruturada entre colaboradores de uma empresa.

O objetivo é centralizar solicitações entre departamentos, permitindo:

* abertura de chamados entre setores
* acompanhamento de tarefas
* comunicação registrada
* auditoria completa
* mensuração de tempo de resolução

Exemplos de uso:

* Produto solicita nova funcionalidade ao time de desenvolvimento
* Colaborador envia atestado ao RH
* Infraestrutura recebe solicitação de manutenção
* Financeiro solicita documentos

Todas as interações ficam registradas e auditáveis.

---

# Stack Tecnológica

Backend:

* Python
* FastAPI
* SQLite
* JWT Authentication
* Docker

Frontend (planejado):

* React
* Vite

Infraestrutura:

* Docker
* Docker Compose

---

# Arquitetura do Backend

O backend segue uma arquitetura em camadas:

controllers → services → repositories → database

Separação de responsabilidades:

Controllers: Recebem requisições HTTP
Services: Regras de negócio
Repositories: Acesso ao banco de dados
Domain: Modelos de domínio
Schemas: Validação de entrada
Security: Autenticação JWT
DB: Conexão e migrations

---

# Estrutura do Projeto

```
colaboramais

apps
 └ backend
    └ app
       ├ controllers
       ├ services
       ├ repositories
       ├ schemas
       ├ domain
       ├ security
       ├ db
       └ main.py

infra
 ├ docker
 │  └ Dockerfile
 └ sql
    └ migrations

data
 └ colaboramais.db

docker-compose.yml
requirements.txt
```

---

# Entidades do Sistema

## Colaborador (User)

Representa um funcionário da empresa.

Campos:

* id
* name
* email
* password_hash
* role_id
* active
* created_at

---

## Cargo (Role)

Define a função do colaborador.

Exemplos:

* Desenvolvedor
* Analista de RH
* Gerente
* Suporte

Campos:

* id
* name
* department_id

---

## Departamento (Department)

Representa um setor da empresa.

Exemplos:

* Desenvolvimento
* RH
* Financeiro
* Produto
* Infraestrutura

Campos:

* id
* name

Relacionamento:

Department → Roles → Users

---

## Ticket (Chamado)

Entidade central do sistema.

Campos:

* id
* title
* description
* author_id
* department_target_id
* status
* created_at
* updated_at
* closed_at

Status possíveis:

OPEN
EM_ANALISE
EM_ANDAMENTO
CONCLUIDO
RECUSADO

---

## Ticket Replies

Representam comunicação dentro do ticket.

Campos:

* id
* ticket_id
* author_id
* message
* type
* created_at

Tipos:

COMENTARIO
ATUALIZACAO_STATUS
CONCLUSAO
JUSTIFICATIVA

---

## Attachments

Permite anexar arquivos ao chamado.

Campos:

* id
* ticket_id
* file_path
* type
* created_at

Exemplos:

* PDFs
* fotos
* prints
* atestados

---

## Audit Logs

Registra ações importantes do sistema.

Campos:

* id
* user_id
* action
* entity
* entity_id
* data
* created_at

Exemplos:

LOGIN
CREATE_TICKET
ADD_REPLY
UPDATE_STATUS
UPLOAD_FILE

---

# Autenticação

Autenticação baseada em **JWT**.

Fluxo:

login → JWT token → Authorization Header → rotas protegidas

---

# Endpoints da API

## Health Check

GET /

Resposta:

```
{ "status": "ok" }
```

---

# Auth

POST /auth/login

Request:

```
{
 "email": "user@empresa.com",
 "password": "123456"
}
```

Response:

```
{
 "access_token": "JWT_TOKEN"
}
```

---

GET /me

Headers:

Authorization: Bearer TOKEN

---

# Departments

POST /departments

GET /departments

---

# Roles

POST /roles

GET /roles

---

# Users

POST /users

GET /users

---

# Tickets

POST /tickets

GET /tickets

PATCH /tickets/{id}/status

---

# Ticket Replies

POST /tickets/{id}/replies

GET /tickets/{id}/replies

---

# Attachments

POST /tickets/{id}/attachments

GET /tickets/{id}/attachments

---

# Metrics

GET /metrics

Exemplo:

```
{
 "open_tickets": 5
}
```

---

# Como Rodar o Projeto

## Rodar localmente

Criar ambiente virtual:

```
python -m venv venv
```

Ativar (Windows):

```
venv\\Scripts\\activate
```

Instalar dependências:

```
pip install -r requirements.txt
```

Rodar servidor:

```
uvicorn app.main:app --reload
```

---

## Swagger

A documentação automática estará disponível em:

```
http://localhost:8000/docs
```

---

# Rodando com Docker

Build e start:

```
docker compose up --build
```

API disponível em:

```
http://localhost:8000
```

---

# Banco de Dados

Banco utilizado:

SQLite

Local:

```
data/colaboramais.db
```

No Docker:

```
/data/colaboramais.db
```

Persistência via volume Docker.

---

# Migrations

As migrations SQL ficam em:

```
infra/sql
```

Executadas automaticamente no startup do backend.

Tabela de controle:

```
migrations
```

---

# Testando a API

Exemplo login:

```
curl -X POST http://localhost:8000/auth/login \\
-H "Content-Type: application/json" \\
-d '{"email":"user@empresa.com","password":"123456"}'
```

Exemplo listar tickets:

```
curl http://localhost:8000/tickets \\
-H "Authorization: Bearer TOKEN"
```

---

# Fluxo do Sistema

## Criar chamado

1. usuário cria ticket
2. escolhe departamento destino
3. adiciona descrição

---

## Responder chamado

Usuário responsável:

* comenta no ticket
* adiciona anexos

---

## Atualizar status

OPEN → EM_ANALISE → EM_ANDAMENTO → CONCLUIDO

---

## Auditoria

Toda ação gera um registro em:

audit_logs

Exemplo:

CREATE_TICKET
ADD_REPLY
UPDATE_STATUS

---

# Possíveis Evoluções

Funcionalidades futuras:

* upload real de arquivos
* notificações em tempo real
* dashboards analíticos
* SLA por departamento
* integração com Git
* autenticação OAuth

---