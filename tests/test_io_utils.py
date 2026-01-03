"""
Unit test for the gene expression matrix loading function

Uses a reduced ARCHS4 file (mini version) containing 5 genes and 14 tissues/cells.
 
Checks that:
- the file is correctly read
- returned objects have the correct types
- matrix dimensions are consistent
- all counts are floats (normalization)


To run the test:
PYTHONPATH=src pytest -s -q tests/test_io_utils.py
"""

from io_utils import load_matrix

def test_load_matrix():

    # Load test file
    tissues, data = load_matrix("data/mini_archs4.tsv.gz")

    # Check the types of returned objects
    assert isinstance(tissues, list)
    assert isinstance(data, dict)

    # Check that each gene is associated with :
    # - a string identifier
    # - one numerical value per tissue/cell
    # - expression values stored as floats
    for gene, counts in data.items():
        assert isinstance(gene, str)
        assert len(counts) == len(tissues)
        assert all(isinstance(x, float) for x in counts)

    # Printed only if all assertions pass
    print("Loading test passed successfully ✓")