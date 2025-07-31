# Projeto de Testes End-to-End com Selenium e Python

Este é um projeto de demonstração para a criação de testes automatizados end-to-end de uma aplicação web simples. A aplicação foi construída com Flask e os testes utilizam Selenium WebDriver, Pytest e WebDriver Manager, implementando as melhores práticas como Page Object Model, Data Factory e configurações avançadas.

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **Flask**: Micro-framework web para a aplicação simulada.
- **Selenium**: Ferramenta de automação de navegadores.
- **Pytest**: Framework de testes para organizar e executar os casos de teste.
- **WebDriver Manager**: Para gerenciar automaticamente os drivers dos navegadores (Chrome, Firefox, etc.).
- **Page Object Model**: Padrão de design para estruturar testes de forma maintível.
- **Data Factory**: Geração dinâmica de dados de teste.
- **pytest-html**: Para gerar relatórios HTML detalhados.

## 📂 Estrutura do Projeto

```
/projeto-testes-selenium-python
|-- app.py                # Aplicação web em Flask
|-- test_app.py           # Arquivo com os casos de teste do Selenium (legado)
|-- requirements.txt      # Lista de dependências do projeto
|-- pytest.ini           # Configurações do Pytest
|-- .env.example          # Exemplo de arquivo de configuração
|-- README.md             # Este arquivo
|-- config/               # Configurações centralizadas
|   |-- settings.py       # Configurações dos testes
|-- pages/                # Page Object Model
|   |-- base_page.py      # Classe base para páginas
|   |-- home_page.py      # Page Object da página inicial
|   |-- form_page.py      # Page Object do formulário
|   |-- success_page.py   # Page Object da página de sucesso
|-- tests/                # Testes organizados por categoria
|   |-- conftest.py       # Configurações e fixtures do Pytest
|   |-- test_navigation.py # Testes de navegação
|   |-- test_forms.py     # Testes de formulários
|   |-- test_errors.py    # Testes de tratamento de erros
|-- utils/                # Utilitários e helpers
|   |-- data_factory.py   # Geração de dados de teste
|   |-- helpers.py        # Funções auxiliares
|-- templates/            # Pasta com os arquivos HTML da aplicação
|   |-- index.html
|   |-- formulario.html
|   |-- sucesso.html
|-- reports/              # Relatórios de teste gerados
|-- screenshots/          # Screenshots de falhas
|-- logs/                 # Logs de execução
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

```powershell
# Executar todos os testes
pytest -v

# Executar testes por categoria
pytest -v -m "smoke"      # Testes de fumaça
pytest -v -m "regression" # Testes de regressão
pytest -v -m "critical"   # Testes críticos

# Executar com diferentes navegadores
pytest -v --browser=firefox
pytest -v --browser=chrome --headless

# Gerar relatório HTML
pytest -v --html=reports/report.html --self-contained-html
```

O Pytest irá iniciar o navegador, executar todas as automações e exibir os resultados no terminal.

## 🧪 Tipos de Teste e Marcadores

O projeto utiliza marcadores (markers) do Pytest para categorizar os testes:

- `@pytest.mark.smoke`: Testes básicos e rápidos
- `@pytest.mark.regression`: Testes completos de regressão
- `@pytest.mark.critical`: Testes de funcionalidades essenciais
- `@pytest.mark.slow`: Testes que demoram mais para executar

## 📊 Relatórios e Logs

- **Relatórios HTML**: Gerados automaticamente na pasta `reports/`
- **Screenshots**: Capturas de tela de falhas são salvas em `screenshots/`
- **Logs detalhados**: Disponíveis em `logs/test.log`

## 🔧 Configurações Avançadas

### Variáveis de Ambiente

Copie o arquivo `.env.example` para `.env` e ajuste as configurações:

```bash
cp .env.example .env
```

### Executando com Opções Customizadas

```powershell
# Modo headless (sem interface gráfica)
pytest -v --headless

# Navegador específico
pytest -v --browser=firefox

# Executar apenas testes que falharam na última execução
pytest -v --lf

# Parar na primeira falha
pytest -v -x

# Executar com debug
pytest -v -s --pdb
```

## 🏗️ Estrutura do Page Object Model

O projeto implementa o padrão Page Object Model para melhor organização:

- **BasePage**: Classe base com métodos comuns
- **HomePage**: Métodos específicos da página inicial
- **FormPage**: Métodos para interação com formulários
- **SuccessPage**: Métodos da página de sucesso

## 🎯 Data Factory

Geração dinâmica de dados de teste para:
- Nomes aleatórios
- Emails válidos
- Dados inválidos para testes de erro
- Strings longas para testes de limite

## 🔍 Debugging e Troubleshooting

### Para debug detalhado:
```powershell
pytest -v -s --capture=no
```

### Para ver logs em tempo real:
```powershell
pytest -v --log-cli-level=INFO
```

### Screenshots automáticos em falhas:
As screenshots são automaticamente capturadas quando um teste falha e salvas na pasta `screenshots/` com timestamp.

## 🚀 CI/CD Integration

Exemplo de configuração para GitHub Actions:

```yaml
name: E2E Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Start Flask app
        run: |
          python app.py &
          sleep 5
      - name: Run tests
        run: |
          pytest -v --headless --browser=chrome
      - name: Upload test reports
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: test-reports
          path: reports/
```

## ✅ Casos de Teste Implementados

### Testes de Navegação (`test_navigation.py`)
- `test_navigate_to_home_page`: Verifica se a página inicial carrega corretamente
- `test_navigate_from_home_to_form`: Valida a navegação da página inicial para a de formulário
- `test_direct_form_page_access`: Testa o acesso direto à página do formulário
- `test_page_titles`: Verifica se os títulos das páginas estão corretos

### Testes de Formulários (`test_forms.py`)
- `test_successful_form_submission`: Testa o preenchimento e envio bem-sucedido do formulário
- `test_form_submission_with_individual_fields`: Testa preenchimento individual dos campos
- `test_multiple_valid_submissions`: Testa múltiplas submissões válidas com dados diferentes
- `test_form_field_clearing`: Testa se os campos podem ser limpos e preenchidos novamente

### Testes de Validação e Erros (`test_errors.py`)
- `test_empty_name_field_error`: Testa erro quando o campo nome está vazio
- `test_empty_email_field_error`: Testa erro quando o campo email está vazio
- `test_both_fields_empty_error`: Testa erro quando ambos os campos estão vazios
- `test_error_message_display_and_disappear`: Testa se a mensagem de erro aparece e desaparece adequadamente
- `test_form_resubmission_after_error`: Testa reenvio do formulário após correção de erro
