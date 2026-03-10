# ColaboraMais — Frontend

## Visão Geral

O **ColaboraMais Frontend** é uma aplicação web desenvolvida em **React + Vite + TailwindCSS** que consome a API do backend FastAPI.

O sistema permite que colaboradores da empresa:

* façam login
* visualizem métricas do sistema
* visualizem tickets
* criem novos tickets
* gerenciem departamentos

Todas as requisições ao backend utilizam **autenticação JWT**.

---

# Stack Tecnológica

Frontend:

* React 18
* Vite
* TypeScript
* TailwindCSS
* Axios
* React Router DOM

Arquitetura:

* Layout persistente (Sidebar + Header)
* Camada de API separada
* Páginas organizadas por funcionalidade
* Componentes reutilizáveis

---

# Estrutura do Projeto

```
apps/frontend

src
 ├ api
 │  ├ client.ts
 │  ├ auth.ts
 │  ├ tickets.ts
 │  └ departments.ts
 │
 ├ components
 │  ├ layout
 │  │  ├ Layout.tsx
 │  │  ├ Sidebar.tsx
 │  │  └ Header.tsx
 │  │
 │  └ ui
 │     └ Card.tsx
 │
 ├ pages
 │  ├ Login.tsx
 │  ├ Register.tsx
 │  ├ Dashboard.tsx
 │  ├ Tickets.tsx
 │  ├ CreateTicket.tsx
 │  └ Departments.tsx
 │
 ├ router
 │  └ router.tsx
 │
 ├ App.tsx
 └ main.tsx
```

---

# Instalação

Criar o projeto:

```
npm create vite@latest frontend
```

Selecionar:

```
React
TypeScript
```

Entrar na pasta:

```
cd frontend
```

Instalar dependências:

```
npm install
```

---

# Dependências

Instalar router:

```
npm install react-router-dom
```

Instalar Axios:

```
npm install axios
```

Instalar Tailwind:

```
npm install -D tailwindcss@3 postcss autoprefixer
npx tailwindcss init -p
```

---

# Configuração do Tailwind

tailwind.config.js

```
content: [
 "./index.html",
 "./src/**/*.{js,ts,jsx,tsx}",
]
```

index.css

```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

---

# Cliente da API

Arquivo:

```
src/api/client.ts
```

```
import axios from "axios"

export const api = axios.create({
  baseURL: "http://localhost:8000",
})

api.interceptors.request.use((config) => {

  const token = localStorage.getItem("token")

  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }

  return config
})
```

Esse cliente injeta automaticamente o **JWT token** nas requisições.

---

# Autenticação

Endpoint utilizado:

```
POST /auth/login
```

Fluxo:

```
Usuário envia email e senha
↓
Backend retorna access_token
↓
Token salvo no localStorage
↓
Token enviado automaticamente nas requisições
```

---

# Layout do Sistema

O frontend utiliza um layout persistente:

```
┌───────────────┬────────────────────┐
│               │ Header             │
│   Sidebar     ├────────────────────┤
│               │                    │
│               │   Conteúdo         │
│               │                    │
└───────────────┴────────────────────┘
```

Componentes principais:

* Sidebar (navegação)
* Header (informações do usuário)
* Layout (estrutura base)

---

# Sidebar

Menu principal:

```
Dashboard
Tickets
Departamentos
```

---

# Dashboard

Página principal do sistema.

Endpoints utilizados:

```
GET /metrics
GET /tickets
```

Exibe:

* número de tickets abertos
* métricas do sistema
* tickets recentes

Cards são renderizados usando:

```
components/ui/Card.tsx
```

---

# Tickets

Página:

```
/tickets
```

Endpoint utilizado:

```
GET /tickets
```

Tabela exibida:

```
ID
Título
Status
Data de criação
```

Filtros suportados:

```
/tickets?status=OPEN
/tickets?department=2
/tickets?author=3
```

---

# Criar Ticket

Página:

```
/tickets/new
```

Fluxo:

```
GET /departments
↓
Usuário seleciona departamento
↓
POST /tickets
```

Payload enviado:

```
{
 "title": "...",
 "description": "...",
 "department_target_id": 2
}
```

O backend define automaticamente:

```
author_id
```

usando o usuário autenticado via JWT.

---

# Departamentos

Página:

```
/departments
```

Endpoints utilizados:

```
GET /departments
POST /departments
```

Funcionalidades:

* listar departamentos
* criar novos departamentos

---

# Router

Arquivo:

```
src/router/router.tsx
```

Rotas principais:

```
/
/login
/register
/tickets
/tickets/new
/departments
```

Rotas protegidas exigem **JWT token**.

---

# Comunicação com Backend

Principais endpoints consumidos:

```
GET /metrics
GET /tickets
POST /tickets
GET /departments
POST /departments
```

Todas as requisições utilizam:

```
Authorization: Bearer TOKEN
```

---

# Rodando o Frontend

Dentro da pasta frontend:

```
npm run dev
```

Aplicação disponível em:

```
http://localhost:5173
```

Backend:

```
http://localhost:8000
```

---

# Fluxo Completo do Sistema

```
Login
↓
Dashboard
↓
Criar departamento
↓
Criar ticket
↓
Tickets aparecem no sistema
↓
Atualização de status
↓
Histórico registrado
```

---

# Próximas Evoluções

Melhorias planejadas:

* página individual de ticket
* comentários em tickets
* upload de anexos
* dashboard com gráficos
* Kanban de tickets
* notificações em tempo real
* métricas avançadas

```
```
