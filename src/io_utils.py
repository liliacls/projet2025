
""" 
Input : Reading an ARCHS4-like gene expression matrix

The input file can be provide in either .tsv ou .tsv.gz format

The expected matrix structure is the following :

                 tissue1    tissu2    tissu3    ...
GENE1   count     63         ...
GENE1   mean      181.159
GENE1   std       423.159
GENE1   min       0
GENE1   max       2120
GENE1   25%       0.5
GENE1   50%       21
GENE1   75%       99
GENE2   ...       ...

Only rows with stat = "count" are retained
All other statistics are ignored

return (tuple) :
- tissues (list)--> Names of tissues/cells corresponding to the columns of the matrix
- data (dict)--> Dictionary mapping each gene to a list of counts per tissue/cell.

 Example : 
- tissues = ['tissue1', 'tissue2', 'tissue3']
- data = { 'GENE1': [63, 120, 5],
           'GENE2': [0, 15, 2],
           'GENE3': [42, 87, 10]}

Note : 
- Each value in the count list corresponds to a tissue/cell in the same positional order as the 'tissues' list.
- By convention, cells are implicitly considered as tissues.
"""

 # Module for reading .gz files without manual decompression
import gzip

def load_archs4(path="ARCHS4.tsv.gz"):
    opener = gzip.open if path.endswith(".gz") else open

    with opener(path, "rt", encoding="utf-8") as f:
            
             # Read header
            header = f.readline().rstrip("\n").split("\t")
            if len(header) < 3:
                    raise ValueError
           
            tissues = header[2:]
            data = {}
            
             # Iterate over file lines
            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) < 3:
                    continue
                
                gene = parts[0]
                stat = parts[1].strip()

                 # Keep only "count" rows
                if stat != "count":
                    continue

                 # Replace missing values with 0
                counts = []
                for value in parts[2:]:
                    try:
                        counts.append(int(value))
                    except ValueError:
                        try:
                            counts.append(float(value))
                        except ValueError:
                            counts.append(0)
                
                data[gene] = counts
            
            return tissues, data