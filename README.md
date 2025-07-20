# Projeto de Testes End-to-End com Selenium e Python

Este é um projeto de demonstração para a criação de testes automatizados end-to-end de uma aplicação web simples. A aplicação foi construída com Flask e os testes utilizam Selenium WebDriver, Pytest e WebDriver Manager.

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **Flask**: Micro-framework web para a aplicação simulada.
- **Selenium**: Ferramenta de automação de navegadores.
- **Pytest**: Framework de testes para organizar e executar os casos de teste.
- **WebDriver Manager**: Para gerenciar automaticamente os drivers dos navegadores (Chrome, Firefox, etc.).

## 📂 Estrutura do Projeto

```
/projeto_selenium
|-- app.py                # Aplicação web em Flask
|-- test_app.py           # Arquivo com os casos de teste do Selenium
|-- requirements.txt      # Lista de dependências do projeto
|-- .gitignore            # Arquivos e pastas a serem ignorados pelo Git
|-- README.md             # Este arquivo
|-- templates/            # Pasta com os arquivos HTML da aplicação
|   |-- index.html
|   |-- formulario.html
|   |-- sucesso.html
```

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação e os testes na sua máquina local.

### 1. Pré-requisitos

- Python 3 instalado
- Git instalado
- Um navegador como Google Chrome ou Firefox

### 2. Configuração do Ambiente

**Clone o repositório:**

```bash
git clone [https://github.com/SEU-USUARIO/projeto-testes-selenium-python.git](https://github.com/Rychardsson/projeto-testes-selenium-python.git)
cd projeto-testes-selenium-python
```

**(Recomendado) Crie e ative um ambiente virtual:**

```bash
# Criar o ambiente
python -m venv venv

# Ativar no Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Ativar no Linux/macOS
source venv/bin/activate
```

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

### 3. Execução

Você precisará de **dois terminais** abertos na pasta do projeto.

**No Terminal 1 - Rode a Aplicação Flask:**

```bash
python app.py
```

O servidor web estará rodando em `http://127.0.0.1:5001`.

**No Terminal 2 - Rode os Testes com Pytest:**

```bash
pytest -v
```

O Pytest irá iniciar o navegador, executar todas as automações e exibir os resultados no terminal.

## ✅ Casos de Teste Implementados

- `test_fluxo_de_navegacao_inicial`: Valida a navegação da página inicial para a de formulário.
- `test_preenchimento_e_envio_sucesso`: Testa o caminho feliz, preenchendo o formulário corretamente e verificando a mensagem de sucesso.
- `test_erro_campo_obrigatorio_vazio`: Garante que uma mensagem de erro é exibida se um campo obrigatório for deixado em branco.
