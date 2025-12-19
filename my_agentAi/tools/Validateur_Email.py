import re

def validate_email(email: str) -> bool:
    """Vérifie le format de l'email avec une Regex."""
    print(f">>> [CALLBACK TOOL] Vérification de l'email : {email}")
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))