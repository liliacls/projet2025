""" 
Test unitaire de la fonction de lecture de la matrice de comptage ARCHS4

Utilisation du fichier ARCHS4 mini --> version réduite de ARCHS4
Contient 5 gènes et 14 tissus/cellules
Vérifie que : 
- le fichier ARCHS4 mini est correctement lu
- les structures retournées ont le bon type
- les dimensions de la matrices sont correctes 

Pour lancer le test : PYTHONPATH=src pytest -s -q tests/test_io_utils.py
"""
import pytest
from io_utils import load_archs4_counts_only

def test_load_archs4_counts_only():

# Chargement du fichier de test 
   tissues, data = load_archs4_counts_only("data/mini_archs4.tsv.gz")

# Type des objets retournés --> tissues = liste, data = dico
   assert isinstance(tissues, list)
   assert isinstance(data, dict)

# Chaque gène doit posseder un nombre de comptages égal au nombre de tissus/cellules
   for gene, counts in data.items():
     assert len(counts) == len(tissues)