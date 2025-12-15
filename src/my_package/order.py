def calcul_total(articles):
    if not articles:
        return 0.0
    total = 0
    for article in articles:
        total += article["prix"] * article["quantite"]
    return round(total, 2)


def valider_transition(statut_actuel, statut_suivant):
    transitions_valides = {
        "en_attente": ["en_cours", "annulee"],
        "en_cours": ["livree", "annulee"],
        "livree": [],
        "annulee": []
    }
    return statut_suivant in transitions_valides.get(statut_actuel, [])

