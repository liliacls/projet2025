
"""
Tests unitaires des fonctions de calcul statistique sur la matrice de comptage
- total_count_gene : calcul du nombre total de comptes par gène
- total_count_tissue : calcul du nombre total de comptes par tissu/cellule
- min_max_items : # Vérification de la valeur maximale/minimale et du/des tissu(s) associé(s) + avec gestion des égalités

Utilisation d'un jeu de données artificiel 
Permet de valider :
- le calcul correct des totaux par gène
- le calcul correct des totaux par tissu
- la gestion des valeurs flottantes
- la prise en compte des cas d'égalité 

Pour lancer les tests : PYTHONPATH=src pytest -s -q tests/test_stats_utils.py
"""

import pytest
from stats_utils import total_count_gene, total_count_tissue, min_max_items

# Test unitaire pour vérifier la fonction total_count_gene

def test_total_count_gene ():
    data1 = {
        "GENE1" : [150.3, 25, 7.1, 5],  # total = 187.4
        "GENE2" : [734.9, 36, 2, 4.5],  # total = 777.4
        "GENE3" : [333, 54.2, 5, 4.6 ]  # total = 396.8
    }
    result = total_count_gene(data1)
    
# Vérification des totaux calculés pour chaque gène
    
    assert result == {"GENE1" : pytest.approx(187.4), 
                      "GENE2" : pytest.approx(777.4), 
                      "GENE3" : pytest.approx(396.8) }

# Test unitaire pour vérifier la fonction total_count_tissue

def test_total_count_tissue():
    tissues = ["tissue1", "tissue2", "tissue3", "tissue4"]
    data1 = {
        "GENE1" : [150.3, 25, 7.1, 5], 
        "GENE2" : [734.9, 36, 2, 4.5],     
        "GENE3" : [333, 54.2, 5, 4.6 ]    
    }
    result = total_count_tissue(data1, tissues)

# Totaux attendues par tissu : 
# - tissue1 : 150.3 + 734.9 + 333 = 1218.2
# - tissue2 : 25 + 36 + 54.2 = 115.2
# - tissue3 : 7.1 + 2 + 5 = 14.1
# - tissue4 : 5 + 4.5 + 4.6 = 14.1

    assert result == {"tissue1" : pytest.approx(1218.2), 
                      "tissue2" : pytest.approx(115.2) , 
                      "tissue3" : pytest.approx(14.1), 
                      "tissue4" : pytest.approx(14.1)}

# Test unitaire pour vérifier la fonction min_max_items

def test_min_max_items():
    tissue_totals = {
        "tissue1": 1218.2,
        "tissue2": 115.2,
        "tissue3": 14.1,
        "tissue4": 14.1,
    }

    min_items, min_val, max_items, max_val = min_max_items(tissue_totals)
    
    assert min_val == pytest.approx(14.1)
    assert set(min_items) == {"tissue3", "tissue4"}

    assert max_val == pytest.approx(1218.2)
    assert set(max_items) == {"tissue1"}
