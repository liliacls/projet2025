"""
Unit tests for statistical computation functions on a count matrix.

An artificial dataset is used.

Functions tested 
----------------
- total_count_gene : computation of the total number of counts per gene
- total_count_tissue : computation of the total number of counts per tissue/cell
- min_max_items : verification of minimum and maximum values and associated key

This validates :
- Correct computation of total counts per gene
- Crrect computation of total counts per tissue
- Handling of floating-point values
- Handling of tie cases

Run 
---
PYTHONPATH=src pytest -s -q tests/test_stats_utils.py
"""

import pytest
from stats_utils import total_count_gene, total_count_tissue, min_max_items

def test_total_count_gene():
    data = {
        "GENE1": [150.3, 25.0 , 7.1, 5.0],     # total = 187.4
        "GENE2": [734.9, 36.0, 2.0, 4.5],      # total = 777.4
        "GENE3": [333.0, 54.2, 5.0, 4.6],      # total = 396.8
        "GENE4": [180.0, 0.0, 7.4, 0.0]        # total = 187.4
        }       
    
    result = total_count_gene(data)
    
    # Verification of total counts computed for each gene
    assert result == { 'GENE1': pytest.approx(187.4),
                       'GENE2': pytest.approx(777.4),
                       'GENE3': pytest.approx(396.8),
                       'GENE4': pytest.approx(187.4)}


def test_total_count_tissue():
    tissues = ["tissue1", "tissue2", "tissue3", "tissue4"]
    data = {
        "GENE1": [150.3, 25.0, 7.1, 5.0],
        "GENE2": [734.9, 36.0, 2.0, 4.5],
        "GENE3": [333.0, 54.2, 5.0, 4.6],
        "GENE4": [180.0, 0.0, 7.4, 0.0]
        }
    
    result = total_count_tissue(tissues, data)
    
    # Expected total counts per tissue: 
    # tissue1 : 150.3 + 734.9 + 333.0 + 180.0 = 1398.2
    # tissue2 : 25.0 + 36.0 + 54.2 + 0.0 = 115.2
    # tissue3 : 7.1 + 2.0 + 5.0 + 7.4 = 21.5
    # tissue4 : 5.0 + 4.5 + 4.6 + 0.0 = 14.1
    
    assert result == {
        "tissue1": pytest.approx(1398.2),
        "tissue2": pytest.approx(115.2),
        "tissue3": pytest.approx(21.5),
        "tissue4": pytest.approx(14.1)
        }

def test_min_max_items_tissues():
    tissue_totals = { 'tissue1': 1398.2,
                      'tissue2': 1398.2,
                      'tissue3': 21.5,
                      'tissue4': 14.1}
    
    min_items, min_val, max_items, max_val = min_max_items(tissue_totals)
    
    assert min_val == pytest.approx(14.1)
    assert set(min_items) == {"tissue4"}
    assert max_val == pytest.approx(1398.2)
    assert set(max_items) == {"tissue1", "tissue2"}

def test_min_max_items_genes():
    gene_totals = { 'GENE1': 187.4,
                    'GENE2': 777.4,
                    'GENE3': 396.8,
                    'GENE4': 187.4}
     
    min_items, min_val, max_items, max_val = min_max_items(gene_totals)
    
    assert min_val == pytest.approx(187.4)
    assert set(min_items) == {"GENE1", "GENE4"}
    assert max_val == pytest.approx(777.4)
    assert set(max_items) == {"GENE2"}