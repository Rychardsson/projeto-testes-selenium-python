from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Importar config de forma segura
try:
    from config.settings import config
    BASE_URL = config.BASE_URL
except ImportError:
    BASE_URL = "http://127.0.0.1:5001"

class SuccessPage(BasePage):
    """Page Object para a página de sucesso"""
    
    # Locators
    SUCCESS_MESSAGE = (By.ID, "mensagem-sucesso")
    PAGE_TITLE = (By.TAG_NAME, "h1")
    BACK_LINK = (By.LINK_TEXT, "Voltar")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = BASE_URL + "/sucesso"
    
    def navigate(self):
        """Navega para a página de sucesso"""
        self.navigate_to(self.url)
    
    def get_success_message(self) -> str:
        """Obtém a mensagem de sucesso"""
        return self.get_element_text(self.SUCCESS_MESSAGE)
    
    def get_page_title_text(self) -> str:
        """Obtém o texto do título da página"""
        return self.get_element_text(self.PAGE_TITLE)
    
    def click_back_link(self):
        """Clica no link de voltar (se presente)"""
        if self.is_element_present(self.BACK_LINK):
            self.click_element(self.BACK_LINK)
    
    def is_on_success_page(self) -> bool:
        """Verifica se está na página de sucesso"""
        return self.get_current_url() == self.url
    
    def has_success_message(self) -> bool:
        """Verifica se a mensagem de sucesso está presente"""
        return self.is_element_present(self.SUCCESS_MESSAGE)
    
    def verify_success_elements(self) -> bool:
        """Verifica se todos os elementos de sucesso estão presentes"""
        return (
            self.is_element_present(self.SUCCESS_MESSAGE) and
            self.is_element_present(self.PAGE_TITLE)
        )
    
    def verify_success_message_content(self, expected_text: str = "Cadastro realizado com sucesso!") -> bool:
        """Verifica se a mensagem de sucesso contém o texto esperado"""
        message = self.get_success_message()
        return expected_text in message
