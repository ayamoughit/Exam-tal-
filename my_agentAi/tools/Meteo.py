def get_weather(city: str) -> dict:
    """Récupère la météo pour une destination donnée."""
    print(f">>> [CALLBACK TOOL] Recherche météo pour : {city}")
    return {"city": city, "temp": "24°C", "sky": "Ensoleillé"}