"""
Function that computes the total number of counts for each gene across all tissues/cells
Return (dict) --> {gene: total count across all tissues/cells}
Example : {'GENE1' : 188, 'GENE2' : ...}
"""

def total_count_gene(data):
    return {gene: sum(counts) for gene, counts in data.items()}

""" 
Function that computes the total number of counts for each tissue/cell across all genes
Return (dict) --> {tissue/cell: total count across all genes}
Example : { 'tissue1': 145,
            'tissue2': 367,
            'tissue3': 12}
"""

def total_count_tissue(tissues, data):

     # Initialize a dictionary with all tissues/cells set to 0
    totals = {t: 0 for t in tissues}

     # Iterate over each gene and accumulate counts per tissue/cell
    for counts in data.values():
        if len(counts) != len(tissues):
            raise ValueError("Counts length does not match number of tissues")

        for tissue, value in zip(tissues, counts):
            totals[tissue] += value

    return totals

"""
Function that identifies the keys associated with the minimum and maximum values in a dictionary

If multiple keys share the same minimum or maximum value, only the first entries are returned (up to a maximum of 10)

Return (tuples) --> 
- min_items (list): keys with the minimum value (max 10)
- min_val (int/float): minimum value
- max_items (list): keys with the maximum value (max 10)
- max_val (int/float): maximum value 
"""

def min_max_items(d, max_limit = 10):
   
    min_val = min(d.values())  
    max_val = max(d.values())

    min_items = []
    max_items = []

    for k, v in d.items():
        if v == min_val and len(min_items) < max_limit: 
            min_items.append(k)
        if v == max_val and len(max_items) < max_limit:
            max_items.append(k)

    return min_items, min_val, max_items, max_val

"""
Function that summarizes minimum and maximum total counts for both genes and tissues/cells

"""

def summarize_min_max(tissues, data, max_limit = 10):
    
    gene_totals = total_count_gene(data)
    min_genes, min_gene_val, max_genes, max_gene_val = min_max_items(gene_totals, max_limit) 

    tissue_totals = total_count_tissue(tissues, data)
    min_tissues, min_tissue_val, max_tissues, max_tissue_val = min_max_items(tissue_totals, max_limit)

    return {
        'genes': {
            'min': {'names': min_genes, 'value': min_gene_val},
            'max': {'names': max_genes, 'value': max_gene_val}
        },
        'tissues': {
            'min': {'names': min_tissues, 'value': min_tissue_val},
            'max': {'names': max_tissues, 'value': max_tissue_val}
        }
    }