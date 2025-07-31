import pytest
from pages.form_page import FormPage
from pages.success_page import SuccessPage

@pytest.mark.critical
class TestFormSubmission:
    """Testes de preenchimento e envio do formulário"""
    
    def test_successful_form_submission(self, driver, valid_user_data):
        """Testa o preenchimento e envio bem-sucedido do formulário"""
        form_page = FormPage(driver)
        success_page = SuccessPage(driver)
        
        # Navega para o formulário
        form_page.navigate()
        assert form_page.is_on_form_page()
        
        # Preenche e envia o formulário
        form_page.fill_form_and_submit(
            valid_user_data["name"], 
            valid_user_data["email"]
        )
        
        # Verifica se chegou na página de sucesso
        assert success_page.is_on_success_page()
        assert success_page.has_success_message()
        assert success_page.verify_success_message_content()
    
    def test_form_submission_with_individual_fields(self, driver):
        """Testa preenchimento individual dos campos"""
        form_page = FormPage(driver)
        success_page = SuccessPage(driver)
        
        form_page.navigate()
        
        # Preenche campo por campo
        form_page.fill_name("Maria Silva")
        form_page.fill_email("maria@teste.com")
        form_page.click_submit()
        
        # Verifica sucesso
        assert success_page.is_on_success_page()
        assert "Cadastro realizado com sucesso!" in success_page.get_success_message()
    
    @pytest.mark.regression
    def test_form_elements_presence(self, driver):
        """Testa se todos os elementos do formulário estão presentes"""
        form_page = FormPage(driver)
        form_page.navigate()
        
        assert form_page.verify_page_elements()
        assert form_page.get_form_title_text()  # Verifica se tem título
    
    @pytest.mark.parametrize("name,email", [
        ("João Silva", "joao@exemplo.com"),
        ("Maria Santos", "maria.santos@teste.com"),
        ("Pedro Oliveira", "pedro123@email.org"),
    ])
    def test_multiple_valid_submissions(self, driver, name, email):
        """Testa múltiplas submissões válidas com dados diferentes"""
        form_page = FormPage(driver)
        success_page = SuccessPage(driver)
        
        form_page.navigate()
        form_page.fill_form_and_submit(name, email)
        
        assert success_page.is_on_success_page()
        assert success_page.has_success_message()
    
    def test_form_field_clearing(self, driver):
        """Testa se os campos podem ser limpos e preenchidos novamente"""
        form_page = FormPage(driver)
        
        form_page.navigate()
        
        # Preenche os campos
        form_page.fill_name("Nome Inicial")
        form_page.fill_email("inicial@email.com")
        
        # Limpa e preenche novamente
        form_page.clear_form()
        form_page.fill_name("Novo Nome")
        form_page.fill_email("novo@email.com")
        
        # Verifica se pode submeter
        form_page.click_submit()
        
        success_page = SuccessPage(driver)
        assert success_page.is_on_success_page()
