# Sistema de Ouvidoria da Universidade XYZ 

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Unifacisa](https://img.shields.io/badge/Unifacisa-2026-blue?style=for-the-badge)

Sistema de gerenciamento de manifestações (ouvidoria) desenvolvido em **Python** com integração ao banco de dados **MySQL**.

Projeto acadêmico do curso de **Análise e Desenvolvimento de Sistemas (ADS)** - Unifacisa.

---

## Sobre o Projeto

O sistema permite o registro, listagem, pesquisa e exclusão de manifestações da universidade, simulando um canal de ouvidoria. 

Possui interface em console com menu interativo e persistência completa de dados no MySQL.

---

## Funcionalidades

- **Cadastrar** nova manifestação
- **Listar** todas as manifestações
- **Pesquisar** manifestação por código
- **Excluir** manifestação
- **Contagem** de registros com concordância gramatical (singular/plural)
- **Menu interativo** com validações
- **Tratamento de erros** (try-except)

---

## Tecnologias Utilizadas

- **Python 3.x**
- **MySQL** (Banco de Dados)
- **mysql-connector-python**
- **Programação Estruturada** e modularização
- **CRUD** completo (Create, Read, Update, Delete)

---

## Estrutura do Projeto

```bash
/
├── menu.py              # Menu principal e interface do usuário
├── ouvidoria.py         # Lógica principal do sistema
├── operacoesbd.py       # Operações de conexão e consultas no banco de dados
└── README.md
```

## Como Executar
# 1. Configuração do Banco de Dados

1. Certifique-se de ter o MySQL instalado e rodando.

2. Crie o banco de dados:
```
CREATE DATABASE ouvidoriaxyz;
```
3. Crie a tabela:
```
CREATE TABLE Manifestacoes (
    codigo INT AUTO_INCREMENT,
    manifestacao VARCHAR(150),
    PRIMARY KEY (codigo)
);
```

# 2. Execução do Projeto

1. Clone o repositório
git clone https://github.com/ssanctorum/ouvidoria-universidade-xyz.git

2. Entre na pasta
cd ouvidoria-universidade-xyz

3. Instale a dependência
pip install mysql-connector-python

4. Execute o sistema
python menu.py

Não esqueça de alterar as credenciais de conexão no arquivo `menu.py` (usuário e senha do MySQL).
