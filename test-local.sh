#!/bin/bash

echo "🚀 Script de teste local para simular CI/CD"
echo "==========================================="

# Verificar se Python está instalado
if ! command -v python &> /dev/null; then
    echo "❌ Python não encontrado"
    exit 1
fi

echo "✅ Python versão: $(python --version)"

# Verificar se pip está instalado
if ! command -v pip &> /dev/null; then
    echo "❌ pip não encontrado"
    exit 1
fi

echo "✅ pip versão: $(pip --version)"

# Verificar se Google Chrome está instalado
if command -v google-chrome &> /dev/null; then
    echo "✅ Chrome versão: $(google-chrome --version)"
elif command -v chromium-browser &> /dev/null; then
    echo "✅ Chromium versão: $(chromium-browser --version)"
else
    echo "⚠️  Chrome/Chromium não encontrado - pode causar falhas"
fi

# Instalar dependências
echo ""
echo "📦 Instalando dependências..."
pip install -r requirements.txt

# Criar diretórios necessários
echo ""
echo "📁 Criando diretórios..."
mkdir -p reports screenshots logs

# Iniciar aplicação Flask em background
echo ""
echo "🌐 Iniciando aplicação Flask..."
python app.py &
FLASK_PID=$!

# Aguardar aplicação iniciar
sleep 10

# Verificar se aplicação está respondendo
echo ""
echo "🔍 Verificando se aplicação está rodando..."
if curl -f http://127.0.0.1:5001/ > /dev/null 2>&1; then
    echo "✅ Aplicação Flask está respondendo"
else
    echo "❌ Aplicação Flask não está respondendo"
    kill $FLASK_PID 2>/dev/null
    exit 1
fi

# Executar testes
echo ""
echo "🧪 Executando testes..."
pytest -v --browser=chrome --headless --html=reports/local-test-report.html --self-contained-html

# Capturar código de saída dos testes
TEST_EXIT_CODE=$?

# Parar aplicação Flask
echo ""
echo "🛑 Parando aplicação Flask..."
kill $FLASK_PID 2>/dev/null

# Mostrar resultados
echo ""
echo "📊 Resultados:"
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "✅ Todos os testes passaram!"
    echo "📄 Relatório disponível em: reports/local-test-report.html"
else
    echo "❌ Alguns testes falharam"
    echo "📄 Verifique o relatório em: reports/local-test-report.html"
    echo "📸 Screenshots de falhas em: screenshots/"
fi

echo ""
echo "🏁 Teste local finalizado!"
exit $TEST_EXIT_CODE
