from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import config

class FormPage(BasePage):
    """Page Object para a página do formulário"""
    
    # Locators
    NAME_INPUT = (By.ID, "nome")
    EMAIL_INPUT = (By.ID, "email")
    SUBMIT_BUTTON = (By.ID, "botao-enviar")
    ERROR_MESSAGE = (By.ID, "mensagem-erro")
    FORM_TITLE = (By.TAG_NAME, "h1")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = config.BASE_URL + "/formulario"
    
    def navigate(self):
        """Navega para a página do formulário"""
        self.navigate_to(self.url)
    
    def fill_name(self, name: str):
        """Preenche o campo nome"""
        self.fill_field(self.NAME_INPUT, name)
    
    def fill_email(self, email: str):
        """Preenche o campo email"""
        self.fill_field(self.EMAIL_INPUT, email)
    
    def click_submit(self):
        """Clica no botão de enviar"""
        self.click_element(self.SUBMIT_BUTTON)
    
    def fill_form_and_submit(self, name: str, email: str):
        """Preenche o formulário completo e envia"""
        self.fill_name(name)
        self.fill_email(email)
        self.click_submit()
    
    def get_error_message(self) -> str:
        """Obtém a mensagem de erro, se presente"""
        try:
            return self.get_element_text(self.ERROR_MESSAGE)
        except:
            return ""
    
    def has_error_message(self) -> bool:
        """Verifica se há mensagem de erro"""
        return self.is_element_present(self.ERROR_MESSAGE)
    
    def is_on_form_page(self) -> bool:
        """Verifica se está na página do formulário"""
        return "Formulário de Teste" in self.get_title()
    
    def get_form_title_text(self) -> str:
        """Obtém o texto do título do formulário"""
        return self.get_element_text(self.FORM_TITLE)
    
    def verify_page_elements(self) -> bool:
        """Verifica se todos os elementos principais estão presentes"""
        return (
            self.is_element_present(self.NAME_INPUT) and
            self.is_element_present(self.EMAIL_INPUT) and
            self.is_element_present(self.SUBMIT_BUTTON)
        )
    
    def clear_form(self):
        """Limpa todos os campos do formulário"""
        self.fill_field(self.NAME_INPUT, "")
        self.fill_field(self.EMAIL_INPUT, "")
