from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple
import time

class BasePage:
    """Classe base para todas as páginas (Page Object Model)"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def navigate_to(self, url: str) -> None:
        """Navega para uma URL específica"""
        self.driver.get(url)
    
    def get_current_url(self) -> str:
        """Retorna a URL atual"""
        return self.driver.current_url
    
    def get_title(self) -> str:
        """Retorna o título da página"""
        return self.driver.title
    
    def wait_for_element(self, locator: Tuple[By, str], timeout: int = 10) -> WebElement:
        """Aguarda um elemento aparecer na página"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    def wait_for_element_clickable(self, locator: Tuple[By, str], timeout: int = 10) -> WebElement:
        """Aguarda um elemento ficar clicável"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def click_element(self, locator: Tuple[By, str]) -> None:
        """Clica em um elemento após aguardar ele ficar clicável"""
        element = self.wait_for_element_clickable(locator)
        element.click()
    
    def fill_field(self, locator: Tuple[By, str], text: str) -> None:
        """Preenche um campo de texto"""
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_element_text(self, locator: Tuple[By, str]) -> str:
        """Obtém o texto de um elemento"""
        element = self.wait_for_element(locator)
        return element.text
    
    def is_element_present(self, locator: Tuple[By, str]) -> bool:
        """Verifica se um elemento está presente na página"""
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False
    
    def wait_for_url_change(self, expected_url: str, timeout: int = 10) -> bool:
        """Aguarda mudança para uma URL específica"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.url_to_be(expected_url))
    
    def take_screenshot(self, filename: str) -> None:
        """Tira screenshot da página atual"""
        self.driver.save_screenshot(f"screenshots/{filename}")
    
    def scroll_to_element(self, locator: Tuple[By, str]) -> None:
        """Rola a página até um elemento específico"""
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)  # Pequena pausa para garantir que o scroll terminou
