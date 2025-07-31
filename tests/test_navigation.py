import pytest
from pages.home_page import HomePage
from pages.form_page import FormPage

@pytest.mark.smoke
class TestNavigation:
    """Testes de navegação entre páginas"""
    
    def test_navigate_to_home_page(self, driver):
        """Testa se a página inicial carrega corretamente"""
        home_page = HomePage(driver)
        home_page.navigate()
        
        assert home_page.is_on_home_page()
        assert home_page.verify_page_elements()
    
    def test_navigate_from_home_to_form(self, driver):
        """Testa a navegação da página inicial para o formulário"""
        home_page = HomePage(driver)
        form_page = FormPage(driver)
        
        # Vai para a página inicial
        home_page.navigate()
        assert home_page.is_on_home_page()
        
        # Clica no link do formulário
        home_page.click_form_link()
        
        # Verifica se chegou na página do formulário
        assert form_page.is_on_form_page()
        assert form_page.verify_page_elements()
    
    def test_direct_form_page_access(self, driver):
        """Testa o acesso direto à página do formulário"""
        form_page = FormPage(driver)
        form_page.navigate()
        
        assert form_page.is_on_form_page()
        assert form_page.verify_page_elements()
    
    @pytest.mark.regression
    def test_page_titles(self, driver):
        """Testa se os títulos das páginas estão corretos"""
        home_page = HomePage(driver)
        form_page = FormPage(driver)
        
        # Verifica título da página inicial
        home_page.navigate()
        assert "Página Inicial" in home_page.get_title()
        
        # Verifica título da página do formulário
        form_page.navigate()
        assert "Formulário de Teste" in form_page.get_title()
