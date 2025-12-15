from my_package.order import calcul_total, valider_transition

def test_calcul_total_classique():
    articles = [
        {"prix": 10.0, "quantite": 2},
        {"prix": 5.5, "quantite": 1}
    ]
    assert calcul_total(articles) == 25.5

def test_calcul_total_vide():
    assert calcul_total([]) == 0.0

def test_transition_valide():
    assert valider_transition("en_attente", "en_cours") is True

def test_transition_invalide():
    assert valider_transition("en_cours", "en_attente") is False

