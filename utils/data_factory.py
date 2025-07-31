import random
import string
from typing import Dict, Any
from datetime import datetime

class DataFactory:
    """Factory para gerar dados de teste dinâmicos"""
    
    @staticmethod
    def generate_random_string(length: int = 8) -> str:
        """Gera uma string aleatória"""
        return ''.join(random.choices(string.ascii_letters, k=length))
    
    @staticmethod
    def generate_random_email(domain: str = "teste.com") -> str:
        """Gera um email aleatório"""
        username = DataFactory.generate_random_string(10).lower()
        return f"{username}@{domain}"
    
    @staticmethod
    def generate_random_name() -> str:
        """Gera um nome aleatório"""
        first_names = ["João", "Maria", "Pedro", "Ana", "Carlos", "Lucia", "Paulo", "Fernanda"]
        last_names = ["Silva", "Santos", "Oliveira", "Souza", "Costa", "Pereira", "Almeida"]
        
        first = random.choice(first_names)
        last = random.choice(last_names)
        return f"{first} {last}"
    
    @staticmethod
    def generate_valid_user_data() -> Dict[str, Any]:
        """Gera dados válidos de usuário"""
        return {
            "name": DataFactory.generate_random_name(),
            "email": DataFactory.generate_random_email(),
            "timestamp": datetime.now().isoformat()
        }
    
    @staticmethod
    def generate_invalid_user_data() -> Dict[str, Dict[str, Any]]:
        """Gera diversos tipos de dados inválidos"""
        return {
            "empty_name": {
                "name": "",
                "email": DataFactory.generate_random_email()
            },
            "empty_email": {
                "name": DataFactory.generate_random_name(),
                "email": ""
            },
            "invalid_email_format": {
                "name": DataFactory.generate_random_name(),
                "email": "email_sem_arroba"
            },
            "both_empty": {
                "name": "",
                "email": ""
            },
            "only_spaces_name": {
                "name": "   ",
                "email": DataFactory.generate_random_email()
            }
        }
    
    @staticmethod
    def generate_long_strings() -> Dict[str, str]:
        """Gera strings muito longas para teste de limites"""
        return {
            "very_long_name": "A" * 1000,
            "very_long_email": f"{'a' * 500}@teste.com"
        }
    
    @staticmethod
    def generate_special_characters_data() -> Dict[str, str]:
        """Gera dados com caracteres especiais"""
        return {
            "name_with_numbers": "João123",
            "name_with_symbols": "João@#$",
            "email_with_symbols": "test+user@email.com"
        }
