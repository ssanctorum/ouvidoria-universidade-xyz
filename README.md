# Sistema de Ouvidoria da Universidade XYZ (Backend Python/SQL)

Este é um sistema de gerenciamento de manifestações em console desenvolvido em Python, com integração a um banco de dados MySQL para persistência dos dados.

## Funcionalidades Principais

* **Criação, Listagem, Pesquisa e Remoção:** Permite Cadastrar, Listar, Pesquisar e Remover (Excluir) manifestações.
* **Controle de Fluxo:** Menu interativo e seguro com validação de opções.
* **Robustez:** Implementação de tratamento de exceções (`try-except`) para entradas inválidas (ex: letras em códigos numéricos).
* **Lógica Adaptativa:** O sistema ajusta a concordância gramatical (singular/plural) ao exibir a contagem de registros.

## Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Banco de Dados:** MySQL
* **Driver:** `mysql.connector`

## Como Executar o Projeto

### 1. Configuração do Banco de Dados

1.  Garanta que você tenha um servidor MySQL rodando (Localhost).
2.  Crie um banco de dados chamado `ouvidoriaxyz` (ou altere o nome no `menu.py`).
3.  Crie a tabela `Manifestacoes` dentro deste banco de dados.

    **Exemplo:**
    ```sql
    CREATE TABLE Manifestacoes (
        codigo INT AUTO_INCREMENT,
        manifestacao VARCHAR(150),
        PRIMARY KEY (codigo)
    );
    ```

### 2. Instalação e Execução

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/ssanctorum/ouvidoria-universidade-xyz
    cd ouvidoria-universidade-xyz
    ```
2.  **Instale as dependências:**
    ```bash
    pip install mysql-connector-python
    ```
3.  **Ajuste as Credenciais:**
    Abra o arquivo `menu.py` e altere a linha de conexão com suas credenciais:
    ```python
    conexao = criarConexao('localhost', 'root', 'SUA_SENHA', 'ouvidoriaxyz')
    ```
4.  **Execute o sistema:**
    ```bash
    python menu.py
    ```

---

## Créditos

* **`menu.py`, `ouvidoria.py`:** [Warlley](https://github.com/ssanctorum/), Júnior, Carol, Ester, Mirelly, Pedro
* **Módulo de Operações de Banco de Dados (`operacoesbd.py`):** [Daniel Abella](https://github.com/daniel-abella)
