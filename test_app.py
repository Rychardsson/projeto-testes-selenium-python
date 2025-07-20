import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# URL base da nossa aplicação Flask
BASE_URL = "http://127.0.0.1:5001"

@pytest.fixture
def driver():
    """
    Fixture do Pytest para inicializar e finalizar o WebDriver.
    Isso será executado antes de cada função de teste.
    """
    # Configura o WebDriver para o Chrome usando o WebDriver Manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)  # Espera implícita de 5 segundos
    
    yield driver
    
    driver.quit()

# ----------------- NOSSOS CASOS DE TESTE -----------------

def test_fluxo_de_navegacao_inicial(driver):
    """
    Testa a navegação da página inicial para o formulário.
    """
    driver.get(BASE_URL + "/")
    
    assert "Página Inicial" in driver.title
    
    link_formulario = driver.find_element(By.LINK_TEXT, "Ir para o formulário de cadastro")
    link_formulario.click()
    
    assert driver.current_url == BASE_URL + "/formulario"
    assert "Formulário de Teste" in driver.title

def test_preenchimento_e_envio_sucesso(driver):
    """
    Testa o preenchimento correto e envio do formulário.
    """
    driver.get(BASE_URL + "/formulario")
    
    driver.find_element(By.ID, "nome").send_keys("Usuário Teste")
    driver.find_element(By.ID, "email").send_keys("teste@exemplo.com")
    
    driver.find_element(By.ID, "botao-enviar").click()
    
    time.sleep(1) 
    
    assert driver.current_url == BASE_URL + "/sucesso"
    
    mensagem = driver.find_element(By.ID, "mensagem-sucesso").text
    assert "Cadastro realizado com sucesso!" in mensagem

def test_erro_campo_obrigatorio_vazio(driver):
    """
    Testa a mensagem de erro quando um campo obrigatório (nome) não é preenchido.
    """
    driver.get(BASE_URL + "/formulario")
    
    driver.find_element(By.ID, "email").send_keys("outro.teste@exemplo.com")
    
    driver.find_element(By.ID, "botao-enviar").click()
    
    assert driver.current_url == BASE_URL + "/formulario"
    
    mensagem_erro = driver.find_element(By.ID, "mensagem-erro").text
    assert "O campo nome é obrigatório." in mensagem_erro