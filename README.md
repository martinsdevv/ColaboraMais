# ColaboraMais

Sistema interno de **gestão de chamados entre departamentos**.

O **ColaboraMais** centraliza solicitações dentro de uma empresa, permitindo comunicação estruturada entre setores com auditoria completa e histórico de ações.

---

# Visão Geral

O sistema permite que colaboradores:

* criem chamados para outros departamentos
* acompanhem o status das solicitações
* respondam tickets com comentários
* anexem arquivos
* tenham auditoria completa de ações
* acompanhem métricas de resolução

Exemplos de uso:

* Produto solicita feature ao time de desenvolvimento
* RH recebe atestados médicos
* Infraestrutura recebe pedidos de manutenção
* Financeiro solicita documentos

---

# Arquitetura

O sistema é dividido em **3 camadas principais**.

```
Frontend (React)
        ↓
Backend API (FastAPI)
        ↓
Banco de dados (SQLite)
```

Estrutura arquitetural do backend:

```
controllers → services → repositories → database
```

Separação de responsabilidades:

* **Controllers** → endpoints HTTP
* **Services** → regras de negócio
* **Repositories** → acesso ao banco
* **Schemas** → validação de dados
* **Security** → autenticação JWT
* **Domain** → entidades do sistema

---

# Stack Tecnológica

## Backend

* Python 3.11
* FastAPI
* SQLite
* JWT Authentication
* Uvicorn

## Frontend

* React 18
* Vite
* TypeScript
* TailwindCSS
* Axios
* React Router

## Infraestrutura

* Docker
* Docker Compose
* Nginx

---

# Estrutura do Projeto

```
colaboramais

apps
 ├ backend
 │   └ app
 │      ├ controllers
 │      ├ services
 │      ├ repositories
 │      ├ schemas
 │      ├ security
 │      ├ domain
 │      ├ db
 │      └ main.py
 │
 └ frontend
     └ src
        ├ api
        ├ components
        ├ pages
        ├ router
        └ main.tsx

infra
 ├ docker
 │   ├ Dockerfile.backend
 │   ├ Dockerfile.frontend
 │   └ nginx.conf
 │
 └ sql
     └ migrations

data
 └ colaboramais.db

docker-compose.yml
requirements.txt
```

---

# Rodando o Projeto (Docker)

A forma mais simples de rodar o sistema é usando **Docker Compose**.

## Build e start

```
docker compose up --build
```

Isso irá iniciar:

```
Backend API
Frontend
Banco SQLite
```

---

# Acessar o Sistema

Frontend:

```
http://localhost:5173
```

Backend:

```
http://localhost:8000
```

Swagger (documentação da API):

```
http://localhost:8000/docs
```

---

# Docker Compose

Serviços do sistema:

### Backend

* FastAPI
* exposto na porta **8000**
* volume persistente para banco SQLite

### Frontend

* React buildado
* servido via **Nginx**
* exposto na porta **5173**

Volume persistente:

```
db_data
```

responsável por armazenar o banco SQLite.

---

# Rodar Localmente (sem Docker)

## Backend

Criar ambiente virtual:

```
python -m venv venv
```

Ativar:

Windows

```
venv\Scripts\activate
```

Instalar dependências:

```
pip install -r requirements.txt
```

```
cd apps/backend
```

Rodar servidor:

```
uvicorn app.main:app --reload
```

API disponível em:

```
http://localhost:8000
```

---

## Frontend

Entrar na pasta:

```
cd apps/frontend
```

Instalar dependências:

```
npm install
```

Rodar:

```
npm run dev
```

Frontend disponível em:

```
http://localhost:5173
```

---

# Banco de Dados

Banco utilizado:

```
SQLite
```

Local do banco:

```
/data/colaboramais.db
```

Persistido através de volume Docker.

---

# Principais Entidades

## User

Representa um colaborador.

Campos principais:

```
id
name
email
password_hash
role_id
active
created_at
```

---

## Department

Representa um setor da empresa.

Exemplos:

```
Desenvolvimento
RH
Financeiro
Produto
Infraestrutura
```

---

## Ticket

Entidade central do sistema.

Campos:

```
id
title
description
author_id
department_target_id
status
created_at
updated_at
closed_at
```

Status possíveis:

```
OPEN
EM_ANALISE
EM_ANDAMENTO
CONCLUIDO
RECUSADO
```

---

## Ticket Replies

Mensagens dentro de um ticket.

Tipos:

```
COMENTARIO
ATUALIZACAO_STATUS
CONCLUSAO
JUSTIFICATIVA
```

---

## Audit Logs

Registro de ações importantes do sistema.

Exemplos:

```
LOGIN
CREATE_TICKET
ADD_REPLY
UPDATE_STATUS
UPLOAD_FILE
```

---

# Fluxo do Sistema

Criar ticket:

```
Usuário cria ticket
↓
Seleciona departamento
↓
Ticket é registrado
↓
Departamento responde
↓
Status é atualizado
↓
Histórico registrado
```

---

# Segurança

Autenticação baseada em **JWT**.

Fluxo:

```
Login
↓
Backend retorna token
↓
Frontend salva token
↓
Token enviado em todas requisições
```

Header utilizado:

```
Authorization: Bearer TOKEN
```

---

# Próximas Evoluções

Funcionalidades planejadas:

* página detalhada de ticket
* upload de anexos
* comentários em tempo real
* dashboard analítico
* Kanban de tickets
* notificações
* integração com Git
* SLA por departamento

---

# Licença

Projeto desenvolvido para fins educacionais.
ColaboraMais — Sistema interno de comunicação empresarial.
