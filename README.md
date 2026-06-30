# 🖥️ Sistema de Monitoria Colaborativa

Este projeto foi desenvolvido como trabalho final da disciplina de **Fundamentos de Banco de Dados**. O objetivo foi criar uma solução prática para organizar o fluxo de atendimentos entre alunos e monitores, aplicando na prática conceitos de modelagem relacional e persistência de dados.

## A Proposta

Durante a disciplina, compreendemos que a teoria sobre normalização e integridade de dados se torna mais clara quando aplicada a problemas reais. Desenvolver este sistema foi o desafio de traduzir a dinâmica de uma monitoria acadêmica — com suas disciplinas, horários e interações — em uma estrutura de banco de dados sólida e eficiente, integrando a lógica em **Python** ao **PostgreSQL**.

## Principais Entregas

- **Modelagem de Dados:** Criação de um esquema relacional focado em minimizar redundâncias e garantir a integridade das informações.
- **Integração:** Conexão robusta entre a aplicação e o banco de dados, utilizando boas práticas de manipulação de dados.
- **Funcionalidades:** Implementação das operações de **CRUD** para o gerenciamento de usuários, disciplinas e histórico de atendimentos.

## Sobre o Processo

O desenvolvimento foi realizado em grupo por **José Mayson**, **Moacir Neto** e **Matheus Eugênio**.

O maior aprendizado foi compreender como as decisões de design no banco de dados impactam diretamente a consistência e a usabilidade do sistema, consolidando os conhecimentos adquiridos sobre modelagem relacional, integridade de dados e arquitetura de bancos de dados ao longo da disciplina.

## Tecnologias Utilizadas

- Python
- PostgreSQL
- SQL
- Git e GitHub

## Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Acesse a pasta do projeto

```bash
cd seu-repositorio
```

### 3. Configure o banco de dados

Execute o script localizado em:

```text
database/schema.sql
```

para criar todas as tabelas e demais objetos necessários no PostgreSQL.

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
python main.py
```

## 💡 Observações

Este projeto foi desenvolvido com fins acadêmicos e tem como objetivo colocar em prática os conceitos estudados na disciplina de **Fundamentos de Banco de Dados**.

Feedbacks, sugestões de melhorias ou dúvidas sobre a modelagem e implementação são sempre bem-vindos.
