# Script de teste local para Windows (PowerShell)
# Execute com: .\test-local.ps1

Write-Host "🚀 Script de teste local para simular CI/CD" -ForegroundColor Green
Write-Host "==========================================="

# Verificar se Python está instalado
try {
    $pythonVersion = python --version
    Write-Host "✅ Python versão: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python não encontrado" -ForegroundColor Red
    exit 1
}

# Verificar se pip está instalado
try {
    $pipVersion = pip --version
    Write-Host "✅ pip versão: $pipVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ pip não encontrado" -ForegroundColor Red
    exit 1
}

# Verificar se Google Chrome está instalado
$chromeExists = Get-Command "chrome" -ErrorAction SilentlyContinue
if ($chromeExists -or (Test-Path "${env:ProgramFiles}\Google\Chrome\Application\chrome.exe") -or (Test-Path "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe")) {
    Write-Host "✅ Google Chrome encontrado" -ForegroundColor Green
} else {
    Write-Host "⚠️  Google Chrome não encontrado - pode causar falhas" -ForegroundColor Yellow
}

# Instalar dependências
Write-Host ""
Write-Host "📦 Instalando dependências..." -ForegroundColor Blue
pip install -r requirements.txt

# Criar diretórios necessários
Write-Host ""
Write-Host "📁 Criando diretórios..." -ForegroundColor Blue
New-Item -ItemType Directory -Force -Path "reports", "screenshots", "logs" | Out-Null

# Iniciar aplicação Flask em background
Write-Host ""
Write-Host "🌐 Iniciando aplicação Flask..." -ForegroundColor Blue
$flaskProcess = Start-Process python -ArgumentList "app.py" -PassThru

# Aguardar aplicação iniciar
Start-Sleep -Seconds 10

# Verificar se aplicação está respondendo
Write-Host ""
Write-Host "🔍 Verificando se aplicação está rodando..." -ForegroundColor Blue
try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:5001/" -TimeoutSec 5
    if ($response.StatusCode -eq 200) {
        Write-Host "✅ Aplicação Flask está respondendo" -ForegroundColor Green
    } else {
        throw "Status code: $($response.StatusCode)"
    }
} catch {
    Write-Host "❌ Aplicação Flask não está respondendo: $_" -ForegroundColor Red
    Stop-Process -Id $flaskProcess.Id -Force -ErrorAction SilentlyContinue
    exit 1
}

# Executar testes
Write-Host ""
Write-Host "🧪 Executando testes..." -ForegroundColor Blue
$testResult = & pytest -v --browser=chrome --headless --html=reports/local-test-report.html --self-contained-html
$testExitCode = $LASTEXITCODE

# Parar aplicação Flask
Write-Host ""
Write-Host "🛑 Parando aplicação Flask..." -ForegroundColor Blue
Stop-Process -Id $flaskProcess.Id -Force -ErrorAction SilentlyContinue

# Mostrar resultados
Write-Host ""
Write-Host "📊 Resultados:" -ForegroundColor Blue
if ($testExitCode -eq 0) {
    Write-Host "✅ Todos os testes passaram!" -ForegroundColor Green
    Write-Host "📄 Relatório disponível em: reports/local-test-report.html" -ForegroundColor Cyan
} else {
    Write-Host "❌ Alguns testes falharam (Exit Code: $testExitCode)" -ForegroundColor Red
    Write-Host "📄 Verifique o relatório em: reports/local-test-report.html" -ForegroundColor Cyan
    Write-Host "📸 Screenshots de falhas em: screenshots/" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "🏁 Teste local finalizado!" -ForegroundColor Green
exit $testExitCode
