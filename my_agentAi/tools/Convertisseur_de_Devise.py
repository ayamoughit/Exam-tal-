def convert_currency(amount: float, rate: float = 11.0) -> str:
    """Convertit un montant selon un taux de change."""
    print(f">>> [CALLBACK TOOL] Conversion de {amount} avec un taux de {rate}")
    result = amount * rate
    return f"{amount} EUR équivaut à {result} MAD."