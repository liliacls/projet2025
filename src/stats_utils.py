"""
Statistical utility functions for gene expression matrix analysis.

This module provides functions to compute summary statistics from an expression count matrix:
- Total read counts per gene
- Total read counts per tissue/cell
- Identification of minimum and maximum total counts
- Structured summaries of statistical results

The math module is used to perform robust floating-point comparisons.
"""

import math

def total_count_gene(data):

    """
    Compute the total number of counts for each gene across all tissues/cells.

    Returns
    -------
    dict[str, float]
    Dictionary mapping each gene to the sum of its counts across all tissues/cells.
    
    Example
    -------
    {"GENE1" : 188.0, "GENE2" : ...}
    """

    return {gene: sum(counts) for gene, counts in data.items()}

def total_count_tissue(tissues, data):

    """ 
    Compute the total number of counts for each tissue/cell across all genes.

    Returns 
    -------
    dict[str, float] 
    Dictionary mapping each tissue/cell to the total count across all genes.

    Example
    -------
    {"tissue1": 145.0, "tissue2": 367.0, "tissue3": 12.0 ...}
    """

    # Initialize a dictionary with all tissues/cells set to 0.0
    totals = {t: 0.0 for t in tissues}

    # Iterate over each gene and accumulate counts per tissue/cell
    for counts in data.values():
        if len(counts) != len(tissues):
            raise ValueError("Counts length does not match number of tissues/cells")
        
        # Add each count to the corresponding tissue/cell total
        for tissue, value in zip(tissues, counts):
            totals[tissue] += float(value)

    return totals

def min_max_items(d: dict, max_limit: int = 10, rel_tol: float = 1e-9, abs_tol: float = 1e-12):

    """
    Identify the keys associated with the minimum and maximum values in a dictionary.

    If multiple keys share the same minimum or maximum value, up to 'max_limit' keys are returned.
    Floating-point comparisons are performed using a numerical tolerance to ensure robust detection of ties.
    
    Returns
    ------
    tuple :
    - min_items (list): Keys with the minimum value (up to max_limit)
    - min_val (float): Minimum value found in the dictionary
    - max_items (list): Keys with the maximum value (up to max_limit)
    - max_val (float): maximum value found in the dictionary
    """
    
    if not d:
        raise ValueError("Input dictionary is empty")
   
    # Determine the minimum and maximum values in the dictionary
    min_val = min(d.values())  
    max_val = max(d.values())

    # Lists to store keys associated with min and max values
    min_items = []
    max_items = []

    for k, v in d.items():

        # Collect keys whose value is numerically equal to the minimum
        if math.isclose(v, min_val, rel_tol=rel_tol, abs_tol=abs_tol) and len(min_items) < max_limit: 
            min_items.append(k)
            
        # Collect keys whose value is numerically equal to the maximum
        if math.isclose(v, max_val, rel_tol=rel_tol, abs_tol=abs_tol) and len(max_items) < max_limit:
            max_items.append(k)

    return min_items, min_val, max_items, max_val

def summarize(tissues, data, max_limit=10):

    """
    Summarize minimum and maximum total counts for both genes and tissues/cells.
    
    This function computes total counts per gene and per tissue/cell, 
    then identifies the genes and tissues with the minimum and maximum total counts.

    Returns
    -------
    dict --> Structured summary dictionary with the following format:
        {
            "genes": {
                "min": {"names": [...], "value": float},
                "max": {"names": [...], "value": float}
            },
            "tissues": {
                "min": {"names": [...], "value": float},
                "max": {"names": [...], "value": float}
            }
        }
    """
    
    gene_totals = total_count_gene(data)

    # Identify genes with minimum and maximum total counts
    min_genes, min_gene_val, max_genes, max_gene_val = min_max_items(gene_totals, max_limit) 

    tissue_totals = total_count_tissue(tissues, data)

    # Identify tissues/cells with minimum and maximum total counts
    min_tissues, min_tissue_val, max_tissues, max_tissue_val = min_max_items(tissue_totals, max_limit)

    return {
        "genes": {
            "min": {"names": min_genes, "value": min_gene_val},
            "max": {"names": max_genes, "value": max_gene_val}
        },
        "tissues": {
            "min": {"names": min_tissues, "value": min_tissue_val},
            "max": {"names": max_tissues, "value": max_tissue_val}
        }
    }