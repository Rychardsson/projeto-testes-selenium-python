# Guia de Execução dos Testes

Este diretório contém todos os testes automatizados organizados por categoria.

## 📁 Estrutura de Testes

- `conftest.py` - Configurações e fixtures globais do Pytest
- `test_navigation.py` - Testes de navegação entre páginas
- `test_forms.py` - Testes de preenchimento e envio de formulários
- `test_errors.py` - Testes de validação e tratamento de erros
- `test_data_factory_example.py` - Exemplos usando Data Factory

## 🚀 Como Executar

### Todos os testes

```bash
pytest -v
```

### Por arquivo específico

```bash
pytest -v tests/test_navigation.py
pytest -v tests/test_forms.py
pytest -v tests/test_errors.py
```

### Por marcadores (tags)

```bash
pytest -v -m "smoke"       # Testes rápidos
pytest -v -m "critical"    # Testes críticos
pytest -v -m "regression"  # Testes completos
```

### Com diferentes navegadores

```bash
pytest -v --browser=chrome
pytest -v --browser=firefox
pytest -v --browser=chrome --headless
```

### Com relatórios

```bash
pytest -v --html=reports/report.html --self-contained-html
```

## 🔧 Opções Úteis

### Debug e desenvolvimento

```bash
pytest -v -s                    # Mostra prints
pytest -v --pdb                 # Para no debugger em falhas
pytest -v --lf                  # Executa apenas os últimos que falharam
pytest -v -x                    # Para na primeira falha
pytest -v --maxfail=3           # Para após 3 falhas
```

### Execução paralela (se instalado pytest-xdist)

```bash
pytest -v -n auto               # Executa em paralelo
```

### Filtragem por nome

```bash
pytest -v -k "navigation"       # Executa testes com "navigation" no nome
pytest -v -k "form and not error" # Executa testes com "form" mas não "error"
```

## 📊 Interpretando Resultados

- ✅ **PASSED** - Teste passou
- ❌ **FAILED** - Teste falhou
- ⚠️ **SKIPPED** - Teste foi pulado
- 🔄 **XFAIL** - Falha esperada
- ✨ **XPASS** - Passou mas era esperado falhar

## 🐛 Debugging

### Screenshots automáticos

- Screenshots são capturados automaticamente quando um teste falha
- Salvos em `screenshots/` com timestamp

### Logs detalhados

- Logs são salvos em `logs/test.log`
- Use `pytest -v --log-cli-level=INFO` para ver logs em tempo real

### Modo verbose

```bash
pytest -v -s --tb=long         # Traceback completo
pytest -v -s --tb=short        # Traceback resumido
```
