import re

def validate_phone(phone: str) -> bool:
    """Vérifie si le numéro de téléphone est au format international."""
    print(f">>> [CALLBACK TOOL] Vérification du téléphone : {phone}") 
    return bool(re.match(r"^\+?[0-9]{10,15}$", phone))