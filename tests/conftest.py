import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import datetime

# Importar config de forma segura
try:
    from config.settings import config
except ImportError:
    # Fallback se config não estiver disponível
    class FallbackConfig:
        BASE_URL = "http://127.0.0.1:5001"
        HEADLESS = False
        TIMEOUT = 10
        SCREENSHOT_ON_FAILURE = True
        VALID_USER_DATA = {"name": "Test User", "email": "test@example.com"}
        INVALID_USER_DATA = {"empty_name": {"name": "", "email": "test@email.com"}}
    
    config = FallbackConfig()

def pytest_addoption(parser):
    """Adiciona opções de linha de comando customizadas"""
    parser.addoption(
        "--browser", 
        action="store", 
        default="chrome",
        help="Browser para executar os testes: chrome ou firefox"
    )
    parser.addoption(
        "--headless", 
        action="store_true", 
        default=False,
        help="Executar os testes em modo headless"
    )

@pytest.fixture(scope="session")
def browser_type(request):
    """Fixture para definir o tipo de browser"""
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def headless_mode(request):
    """Fixture para definir se deve executar em modo headless"""
    return request.config.getoption("--headless") or config.HEADLESS

@pytest.fixture(scope="function")
def driver(browser_type, headless_mode):
    """
    Fixture principal para criar e gerenciar o WebDriver
    Executada antes de cada teste
    """
    driver_instance = None
    
    try:
        if browser_type.lower() == "chrome":
            driver_instance = _create_chrome_driver(headless_mode)
        elif browser_type.lower() == "firefox":
            driver_instance = _create_firefox_driver(headless_mode)
        else:
            raise ValueError(f"Browser '{browser_type}' não suportado. Use 'chrome' ou 'firefox'")
        
        # Configurações gerais
        driver_instance.implicitly_wait(config.TIMEOUT)
        driver_instance.maximize_window()
        
        yield driver_instance
        
    finally:
        if driver_instance:
            driver_instance.quit()

def _create_chrome_driver(headless: bool = False):
    """Cria uma instância do Chrome WebDriver"""
    options = ChromeOptions()
    
    if headless:
        options.add_argument("--headless")
    
    # Opções essenciais para CI/CD
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-web-security")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--ignore-certificate-errors")
    
    try:
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print(f"Erro ao criar Chrome driver: {e}")
        # Fallback: tentar usar Chrome do sistema
        try:
            return webdriver.Chrome(options=options)
        except Exception as e2:
            print(f"Erro no fallback Chrome: {e2}")
            raise

def _create_firefox_driver(headless: bool = False):
    """Cria uma instância do Firefox WebDriver"""
    options = FirefoxOptions()
    
    if headless:
        options.add_argument("--headless")
    
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    
    service = FirefoxService(GeckoDriverManager().install())
    return webdriver.Firefox(service=service, options=options)

@pytest.fixture(scope="function")
def screenshot_on_failure(request, driver):
    """Fixture para tirar screenshot em caso de falha"""
    yield
    
    if request.node.rep_call.failed and config.SCREENSHOT_ON_FAILURE:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        screenshot_name = f"{test_name}_{timestamp}.png"
        screenshot_path = os.path.join("screenshots", screenshot_name)
        
        try:
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot salvo: {screenshot_path}")
        except Exception as e:
            print(f"Erro ao salvar screenshot: {e}")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para capturar informações do resultado do teste"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# Fixtures de dados para testes
@pytest.fixture
def valid_user_data():
    """Dados válidos de usuário para testes"""
    return config.VALID_USER_DATA.copy()

@pytest.fixture
def invalid_user_data():
    """Dados inválidos de usuário para testes"""
    return config.INVALID_USER_DATA.copy()

@pytest.fixture
def base_url():
    """URL base da aplicação"""
    return config.BASE_URL
