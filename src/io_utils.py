
""" 
Entrée : Lecture de la matrice de comptage ARCHS4

Le fichier d'entrée peut être au format .tsv ou .tsv.gz

La mise en forme doit être :

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

Seules les lignes avec stat = "count" sont conservées
Les statistiques (mean, std, min, ...) sont ignorées

return (tuple):
- tissues (liste) --> nom des tissus/cellules (colonnes)
- data (dict) --> { gene : [ comptages par tissu/cellule ]}

Exemple : (["tissue1, tissue2"], { "GENE1" : [2,10,15], "GENE2" : [...]})
Note : par convention, les cellules sont implicitement considérées comme des tissus.
"""

# Module permettant de lire des fichiers .gz sans décompression

import gzip

# Chemin vers le fichier ARCHS4 (.tsv ou tsv.gz)

def load_archs4_counts_only(path="ARCHS4.tsv.gz"):

# CAS 1 : Fichier compressé (.tsv.gz)

 if path.endswith(".gz"):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            
# Lecture de l'en tête pour extraire les tissus et cellules

            header = f.readline().rstrip("\n").split("\t")
            tissues = header[2:]
        
            data = {}
            
# Parcours des lignes du fichier une à une 

            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) < 3:
                    continue
                
                gene = parts[0]
                stat = parts[1].strip()

# Seules les lignes "count" sont conservées

                if stat != "count":
                    continue
                
# Gestion des différents formats des valeurs de comptage

                counts = []
                for x in parts[2:]:
                    try:
                        counts.append(int(x))
                    except ValueError:
                        try:
                            counts.append(int(float(x)))
                        except ValueError:
                            counts.append(0)
                
                data[gene] = counts
            
            return tissues, data
        
        
# CAS 2 : Fichier non compressé (.tsv)  
   
 else:
        with open(path, "r", encoding="utf-8") as f:
            
# Lecture de l'en-tête pour ectraire les tissues et cellules

            header = f.readline().rstrip("\n").split("\t")
            tissues = header[2:]
            data = {}

# Parcours des lignes du fichier une à une

            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) < 3:
                    continue
                
                gene = parts[0]
                stat = parts[1].strip()

# Seules les lignes "count" sont conservées
                
                if stat != "count":
                    continue
                
# Gestion des différents formats des valeurs de comptage

                counts = []
                for x in parts[2:]:
                    try:
                        counts.append(int(x))
                    except ValueError:
                        try:
                            counts.append(int(float(x)))
                        except ValueError:
                            counts.append(0)
                
                data[gene] = counts
            
            return tissues, data

