import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging

class TestHelpers:
    """Classe com métodos auxiliares para testes"""
    
    @staticmethod
    def wait_for_page_load(driver, timeout: int = 10):
        """Aguarda o carregamento completo da página"""
        wait = WebDriverWait(driver, timeout)
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
    
    @staticmethod
    def safe_click(driver, locator, timeout: int = 10):
        """Clica em um elemento de forma segura, aguardando ele estar clicável"""
        try:
            wait = WebDriverWait(driver, timeout)
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
            return True
        except TimeoutException:
            return False
    
    @staticmethod
    def safe_send_keys(driver, locator, text: str, timeout: int = 10):
        """Envia texto para um elemento de forma segura"""
        try:
            wait = WebDriverWait(driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            return True
        except TimeoutException:
            return False
    
    @staticmethod
    def is_element_visible(driver, locator, timeout: int = 5):
        """Verifica se um elemento está visível"""
        try:
            wait = WebDriverWait(driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    @staticmethod
    def take_screenshot(driver, filename: str = None):
        """Tira screenshot com nome automático se não especificado"""
        if not filename:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
        
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        
        filepath = os.path.join(screenshot_dir, filename)
        driver.save_screenshot(filepath)
        return filepath
    
    @staticmethod
    def scroll_to_element(driver, locator):
        """Rola a página até um elemento específico"""
        try:
            element = driver.find_element(*locator)
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.5)  # Pequena pausa para garantir que o scroll terminou
            return True
        except NoSuchElementException:
            return False
    
    @staticmethod
    def get_element_text_safe(driver, locator, timeout: int = 10):
        """Obtém texto de um elemento de forma segura"""
        try:
            wait = WebDriverWait(driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            return element.text
        except TimeoutException:
            return ""
    
    @staticmethod
    def wait_for_url_change(driver, expected_url: str, timeout: int = 10):
        """Aguarda mudança para uma URL específica"""
        try:
            wait = WebDriverWait(driver, timeout)
            return wait.until(EC.url_to_be(expected_url))
        except TimeoutException:
            return False
    
    @staticmethod
    def refresh_page_and_wait(driver, timeout: int = 10):
        """Atualiza a página e aguarda carregamento"""
        driver.refresh()
        TestHelpers.wait_for_page_load(driver, timeout)
    
    @staticmethod
    def get_current_timestamp():
        """Retorna timestamp atual formatado"""
        return time.strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def setup_logging(log_level=logging.INFO):
        """Configura logging para os testes"""
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/test.log'),
                logging.StreamHandler()
            ]
        )
        return logging.getLogger(__name__)

class BrowserHelpers:
    """Helpers específicos para operações do navegador"""
    
    @staticmethod
    def clear_browser_cache(driver):
        """Limpa cache do navegador (funciona com Chrome)"""
        try:
            driver.execute_script("window.localStorage.clear();")
            driver.execute_script("window.sessionStorage.clear();")
            return True
        except Exception:
            return False
    
    @staticmethod
    def set_window_size(driver, width: int = 1920, height: int = 1080):
        """Define o tamanho da janela do navegador"""
        try:
            driver.set_window_size(width, height)
            return True
        except Exception:
            return False
    
    @staticmethod
    def get_browser_console_logs(driver):
        """Obtém logs do console do navegador (Chrome)"""
        try:
            logs = driver.get_log('browser')
            return logs
        except Exception:
            return []
