import pytest
from pages.form_page import FormPage

@pytest.mark.critical
class TestFormValidation:
    """Testes de validação e tratamento de erros do formulário"""
    
    def test_empty_name_field_error(self, driver):
        """Testa erro quando o campo nome está vazio"""
        form_page = FormPage(driver)
        form_page.navigate()
        
        # Preenche apenas o email, deixa nome vazio
        form_page.fill_email("teste@email.com")
        form_page.click_submit()
        
        # Verifica se permanece na página do formulário
        assert form_page.is_on_form_page()
        
        # Verifica mensagem de erro
        assert form_page.has_error_message()
        error_message = form_page.get_error_message()
        assert "O campo nome é obrigatório." in error_message
    
    def test_empty_email_field_error(self, driver):
        """Testa erro quando o campo email está vazio"""
        form_page = FormPage(driver)
        form_page.navigate()
        
        # Preenche apenas o nome, deixa email vazio
        form_page.fill_name("João Silva")
        form_page.click_submit()
        
        # Verifica se permanece na página do formulário
        assert form_page.is_on_form_page()
        
        # Verifica mensagem de erro
        assert form_page.has_error_message()
        error_message = form_page.get_error_message()
        assert "O campo email é obrigatório." in error_message
    
    def test_both_fields_empty_error(self, driver):
        """Testa erro quando ambos os campos estão vazios"""
        form_page = FormPage(driver)
        form_page.navigate()
        
        # Envia formulário sem preencher nada
        form_page.click_submit()
        
        # Verifica se permanece na página do formulário
        assert form_page.is_on_form_page()
        
        # Verifica se há mensagem de erro (deve aparecer para o primeiro campo obrigatório)
        assert form_page.has_error_message()
    
    @pytest.mark.parametrize("test_data", [
        {"name": "", "email": "teste@email.com", "expected_error": "nome é obrigatório"},
        {"name": "João", "email": "", "expected_error": "email é obrigatório"},
    ])
    def test_field_validation_parametrized(self, driver, test_data):
        """Testa validação de campos usando parâmetros"""
        form_page = FormPage(driver)
        form_page.navigate()
        
        if test_data["name"]:
            form_page.fill_name(test_data["name"])
        if test_data["email"]:
            form_page.fill_email(test_data["email"])
        
        form_page.click_submit()
        
        # Verifica se permanece na página do formulário
        assert form_page.is_on_form_page()
        
        # Verifica mensagem de erro
        assert form_page.has_error_message()
        error_message = form_page.get_error_message()
        assert test_data["expected_error"] in error_message
    
    @pytest.mark.regression
    def test_error_message_display_and_disappear(self, driver):
        """Testa se a mensagem de erro aparece e desaparece adequadamente"""
        form_page = FormPage(driver)
        form_page.navigate()
        
        # Primeiro envia formulário inválido
        form_page.fill_email("teste@email.com")  # Só email, sem nome
        form_page.click_submit()
        
        # Verifica erro
        assert form_page.has_error_message()
        
        # Agora preenche corretamente
        form_page.fill_name("João Silva")
        form_page.click_submit()
        
        # Deve ir para página de sucesso (erro deve ter desaparecido)
        from pages.success_page import SuccessPage
        success_page = SuccessPage(driver)
        assert success_page.is_on_success_page()
    
    def test_form_resubmission_after_error(self, driver):
        """Testa reenvio do formulário após correção de erro"""
        form_page = FormPage(driver)
        form_page.navigate()
        
        # Primeira tentativa com erro
        form_page.fill_name("")  # Nome vazio
        form_page.fill_email("teste@email.com")
        form_page.click_submit()
        
        assert form_page.has_error_message()
        
        # Corrige o erro e reenvia
        form_page.fill_name("Nome Correto")
        form_page.click_submit()
        
        # Deve ter sucesso agora
        from pages.success_page import SuccessPage
        success_page = SuccessPage(driver)
        assert success_page.is_on_success_page()
