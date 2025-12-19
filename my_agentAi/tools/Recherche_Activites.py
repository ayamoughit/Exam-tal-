def search_activities(city: str) -> dict:
    """Recherche les activités touristiques pour une destination donnée."""
    print(f">>> [CALLBACK TOOL] Recherche d'activités à : {city}")
    # Simulation de données pour les activités
    activities = {
        "casablanca": ["Mosquée Hassan II", "Corniche", "Quartier Habous", "Morocco Mall", "Parc de la Ligue Arabe"],
        "marrakech": ["Place Jemaa el-Fna", "Jardins Majorelle", "Palais Bahia", "Médina", "Souks"],
        "rabat": ["Tour Hassan", "Kasbah des Oudayas", "Mausolée Mohammed V", "Zoo de Rabat"],
        "fes": ["Médina de Fès", "Tanneries Chouara", "Bab Boujloud", "Médersa Bou Inania"],
    }
    city_lower = city.lower()
    if city_lower in activities:
        return {"city": city, "activities": activities[city_lower]}
    else:
        return {"city": city, "activities": ["Visite de la médina", "Découverte gastronomique", "Excursion locale"]}
