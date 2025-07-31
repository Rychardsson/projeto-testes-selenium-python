from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import config

class HomePage(BasePage):
    """Page Object para a página inicial"""
    
    # Locators
    FORM_LINK = (By.LINK_TEXT, "Ir para o formulário de cadastro")
    PAGE_TITLE = (By.TAG_NAME, "h1")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = config.BASE_URL + "/"
    
    def navigate(self):
        """Navega para a página inicial"""
        self.navigate_to(self.url)
    
    def click_form_link(self):
        """Clica no link para ir ao formulário"""
        self.click_element(self.FORM_LINK)
    
    def get_page_title_text(self) -> str:
        """Obtém o texto do título da página"""
        return self.get_element_text(self.PAGE_TITLE)
    
    def is_on_home_page(self) -> bool:
        """Verifica se está na página inicial"""
        return "Página Inicial" in self.get_title()
    
    def verify_page_elements(self) -> bool:
        """Verifica se todos os elementos principais estão presentes"""
        return (
            self.is_element_present(self.FORM_LINK) and
            self.is_element_present(self.PAGE_TITLE)
        )
