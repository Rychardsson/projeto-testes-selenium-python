import pytest
from utils.data_factory import DataFactory
from pages.form_page import FormPage
from pages.success_page import SuccessPage

@pytest.mark.regression
class TestDataFactory:
    """Testes demonstrando o uso da Data Factory"""
    
    def test_form_with_random_data(self, driver):
        """Testa formulário com dados gerados dinamicamente"""
        # Gera dados aleatórios
        user_data = DataFactory.generate_valid_user_data()
        
        form_page = FormPage(driver)
        success_page = SuccessPage(driver)
        
        form_page.navigate()
        form_page.fill_form_and_submit(
            user_data["name"], 
            user_data["email"]
        )
        
        assert success_page.is_on_success_page()
        assert success_page.has_success_message()
    
    @pytest.mark.parametrize("data_type", [
        "empty_name",
        "empty_email", 
        "both_empty"
    ])
    def test_form_with_invalid_data_factory(self, driver, data_type):
        """Testa formulário com dados inválidos da factory"""
        invalid_data = DataFactory.generate_invalid_user_data()
        test_data = invalid_data[data_type]
        
        form_page = FormPage(driver)
        form_page.navigate()
        
        form_page.fill_form_and_submit(
            test_data["name"], 
            test_data["email"]
        )
        
        # Deve permanecer na página do formulário com erro
        assert form_page.is_on_form_page()
        assert form_page.has_error_message()
    
    def test_multiple_random_users(self, driver):
        """Testa múltiplos usuários com dados aleatórios"""
        form_page = FormPage(driver)
        success_page = SuccessPage(driver)
        
        for i in range(3):
            user_data = DataFactory.generate_valid_user_data()
            
            form_page.navigate()
            form_page.fill_form_and_submit(
                user_data["name"], 
                user_data["email"]
            )
            
            assert success_page.is_on_success_page()
            print(f"Usuário {i+1} cadastrado: {user_data['name']} - {user_data['email']}")
