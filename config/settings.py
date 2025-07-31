import os
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class TestConfig:
    """Configurações centralizadas para os testes"""
    BASE_URL: str = os.getenv("BASE_URL", "http://127.0.0.1:5001")
    BROWSER: str = os.getenv("BROWSER", "chrome")
    HEADLESS: bool = os.getenv("HEADLESS", "false").lower() == "true"
    TIMEOUT: int = int(os.getenv("TIMEOUT", "10"))
    SCREENSHOT_ON_FAILURE: bool = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"
    
    # Dados de teste válidos
    VALID_USER_DATA: Dict[str, Any] = {
        "name": "João Silva",
        "email": "joao@teste.com",
        "phone": "(11) 99999-9999"
    }
    
    # Dados de teste inválidos
    INVALID_USER_DATA: Dict[str, Any] = {
        "empty_name": {"name": "", "email": "teste@email.com"},
        "empty_email": {"name": "Nome Teste", "email": ""},
        "invalid_email": {"name": "Nome Teste", "email": "email_invalido"}
    }

# Instância global de configuração
config = TestConfig()
