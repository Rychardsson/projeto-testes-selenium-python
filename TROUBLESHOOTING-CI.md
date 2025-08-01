# 🔧 Troubleshooting GitHub Actions

## Problemas Comuns e Soluções

### ❌ Erro: Instalação de dependências Python falha

**Sintomas:**

- `pip install` falha no CI
- Erro de conflito de versões
- Timeout durante instalação

**Soluções:**

1. **Use o workflow minimal:**

   ```bash
   mv .github/workflows/minimal-ci.yml .github/workflows/ci.yml
   ```

2. **Requirements simplificados:**

   - O projeto agora tem `requirements-ci.txt` com dependências mínimas
   - Page objects têm fallback para importações

3. **Instalação manual:**
   ```yaml
   - name: Install Python packages
     run: |
       pip install Flask selenium pytest webdriver-manager pytest-html
   ```

### ❌ Erro: Chrome não encontrado

**Soluções:**

```yaml
- name: Install Chrome
  run: |
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
    sudo apt-get update
    sudo apt-get install -y google-chrome-stable
```

### ❌ Erro: Flask não inicia

**Soluções:**

```yaml
- name: Start Flask app
  run: |
    python app.py &
    sleep 10
    curl http://127.0.0.1:5001/ || exit 1
```

### ❌ Erro: Importação de módulos

**Problema:** `ModuleNotFoundError: No module named 'config'`

**Solução:** Os arquivos agora têm fallback:

```python
try:
    from config.settings import config
    BASE_URL = config.BASE_URL
except ImportError:
    BASE_URL = "http://127.0.0.1:5001"
```

## 🚀 Workflows Disponíveis

1. **`minimal-ci.yml`** ⭐ **RECOMENDADO**

   - Instalação manual das dependências
   - Sem matriz de versões
   - Mais robusto

2. **`basic-ci.yml`**

   - Apenas teste de navegação
   - Para debug inicial

3. **`simple-ci.yml`**

   - Versão intermediária

4. **`ci.yml`**
   - Versão completa
   - Pode falhar em algumas configurações

## 📋 Checklist para CI que Funciona

- ✅ Use Python 3.11 (mais estável)
- ✅ Instale Chrome manualmente
- ✅ Use dependências mínimas
- ✅ Aguarde Flask iniciar (10-15s)
- ✅ Use `--headless` nos testes
- ✅ Configure `DISPLAY=:99` se necessário

## 🆘 Último Recurso - Workflow Mínimo

Se tudo falhar, use este workflow básico:

```yaml
name: Test Basic
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: |
          sudo apt-get update
          sudo apt-get install -y google-chrome-stable
          pip install Flask selenium pytest webdriver-manager
          python app.py &
          sleep 15
          pytest tests/test_navigation.py::TestNavigation::test_navigate_to_home_page -v --browser=chrome --headless
```
