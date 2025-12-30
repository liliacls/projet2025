"""
Unit test for the ARCHS4 count matrix loading function.

Uses a reduced ARCHS4 file (mini version) containing 5 genes and 14 tissues/cells.
 
Checks that:
- the file is correctly read
- the returned objects have the correct types
- the dimensions of the matrix are consistent

To run the test:
PYTHONPATH=src pytest -s -q tests/test_io_utils.py
"""

from io_utils import load_archs4

def test_load_archs4():

    # Load test file
    tissues, data = load_archs4("data/mini_archs4.tsv.gz")

    # Check returned object types --> tissues = list, data = dict
    assert isinstance(tissues, list)
    assert isinstance(data, dict)

    # Each gene must have as many counts as tissues/cells
    for gene, counts in data.items():
        assert len(counts) == len(tissues)

    # Printed ONLY if all assertions pass
    print("mini-ARCHS4 loading test passed successfully ✓")