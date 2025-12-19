def calculate_budget(nights: int, hotel_stars: int) -> float:
    """Calcule le coût total estimé de l'hôtel."""
    print(f">>> [CALLBACK TOOL] Calcul budget : {nights} nuits en {hotel_stars}*")
    return float(nights * (hotel_stars * 55))