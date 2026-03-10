# ColaboraMais — Especificação do Sistema

## 1. Objetivo

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

# 2. Conceitos principais

## 2.1 Colaborador

Representa um funcionário da empresa.

Campos:

* id
* nome
* email
* senha_hash
* cargo_id
* ativo
* created_at

---

## 2.2 Cargo

Define a função de um colaborador dentro da empresa.

Exemplos:

* Desenvolvedor
* Analista de RH
* Gerente
* Suporte
* Financeiro

Campos:

* id
* nome
* departamento_id

---

## 2.3 Departamento

Representa um setor da empresa.

Exemplos:

* Desenvolvimento
* RH
* Financeiro
* Produto
* Suporte
* Infraestrutura

Campos:

* id
* nome

Relacionamento:

Departamento -> Cargos -> Colaboradores

---

# 3. Chamados (Tasks)

Chamados são a entidade principal do sistema.

Um colaborador cria um chamado direcionado a um departamento.

Exemplo:

Criado por: João (Produto)
Destino: Desenvolvimento
Motivo: Nova tela no sistema X

Campos:

* id
* titulo
* descricao
* autor_id
* departamento_destino_id
* status
* prioridade
* created_at
* updated_at
* closed_at

Status possíveis:

* ABERTO
* EM_ANALISE
* EM_ANDAMENTO
* CONCLUIDO
* RECUSADO

---

# 4. Respostas do Chamado

Permite comunicação dentro do chamado.

Exemplo:

"Feature implementada no commit abc123"

Campos:

* id
* chamado_id
* autor_id
* mensagem
* tipo
* created_at

Tipos:

* COMENTARIO
* ATUALIZACAO_STATUS
* CONCLUSAO
* JUSTIFICATIVA

---

# 5. Anexos

Permite anexar arquivos ao chamado.

Exemplos:

* fotos
* PDFs
* atestados
* prints

Campos:

* id
* chamado_id
* arquivo_path
* tipo
* created_at

---

# 6. Auditoria

O sistema deve registrar todas as ações importantes para rastreabilidade.

Tabela: audit_logs

Campos:

* id
* usuario_id
* acao
* entidade
* entidade_id
* dados
* created_at

Exemplos de ações:

* CREATE_TICKET
* UPDATE_STATUS
* ADD_REPLY
* UPLOAD_FILE
* CLOSE_TICKET

---

# 7. Métricas

O sistema deve permitir medir:

* tempo médio de conclusão
* tempo por departamento
* tarefas por colaborador
* backlog de tarefas

Tempo de resolução:

closed_at - created_at

---

# 8. Permissões (MVP)

## Colaborador

Pode:

* abrir chamados
* comentar
* anexar arquivos

## Departamento responsável

Pode:

* responder chamados
* alterar status
* concluir tarefas

## Administrador

Pode:

* visualizar todos os chamados
* gerenciar usuários
* gerenciar cargos
* gerenciar departamentos

---

# 9. Arquitetura Técnica

## Backend

Sugestão:

* FastAPI

Responsável por:

* API REST
* autenticação
* regras de negócio
* auditoria

---

## Frontend

* React
* Vite

Responsável por:

* interface do usuário
* dashboards
* criação e acompanhamento de chamados

---

## Banco de Dados

* SQLite

Justificativa:

* simples para MVP
* fácil de rodar com Docker

Possível evolução:

* PostgreSQL

---

# 10. Monorepo

Estrutura sugerida:

```
colaboramais/

apps/
  backend/
  frontend/

packages/
  shared-types/
  ui/

infra/
  docker/
  migrations/

docs/
```

---

# 11. Docker Compose

Serviços:

* backend
* frontend
* banco

Responsabilidades:

Backend:

* API

Frontend:

* aplicação React

Banco:

* SQLite com volume persistente

---

# 12. Fluxo do Sistema

## Criar chamado

1. colaborador cria chamado
2. seleciona departamento destino
3. adiciona descrição e anexos

---

## Análise

Departamento responsável visualiza chamados abertos.

---

## Execução

Status alterado para:

EM_ANDAMENTO

---

## Conclusão

Responsável:

* adiciona comentário
* registra commit ou solução
* altera status para CONCLUIDO

---

## Auditoria

Todas as ações são registradas no log de auditoria.

---

# 13. Telas Principais

## Login

Autenticação de colaboradores.

---

## Dashboard

Mostra:

* chamados abertos
* chamados do meu departamento
* chamados criados por mim

---

## Criar chamado

Formulário:

* título
* descrição
* departamento destino
* prioridade
* anexos

---

## Página do chamado

Exibe:

* detalhes
* histórico
* comentários
* anexos

---

## Administração

Gerenciamento de:

* usuários
* cargos
* departamentos

---

# 14. Possíveis Evoluções

Funcionalidades futuras:

* notificações por email
* notificações em tempo real (WebSocket)
* SLA por departamento
* dashboards de analytics
* integração com Git
* automações de workflow
