
#### Lecture de la matrice de comptage ARCHS4
### Le fichier d'ntrée peut être au format .tsv ou tsv.gz
### En sortie  : 
### - tissues : liste des tissus/cellules (noms des colonnes)
### - data : dictionnaire {gène : liste des comptages par tissus/cellules}

import gzip

def load_archs4_counts_only(path="ARCHS4.tsv.gz"):

### Chargement de la matrice de comptage
### Seules les lignes correspondant aux "counts" sont conservées. 
### tissues : list --> Liste des tissus/cellules 
### data : dict --> Dictionnaire {gene : [counts par tissu/cellule]}

### Fichier compressé (.tsv.gz)

    if path.endswith(".gz"):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            
            ### Lecture de l'en tête
            header = f.readline().rstrip("\n").split("\t")
            tissues = header[2:]
            data = {}
            
            ### Parcours des lignes du fichier
            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) < 3:
                    continue
                
                gene = parts[0]
                stat = parts[1].strip()
                
                if stat != "count":
                    continue
                
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
        
### Fichier non compressé (.tsv)  
   
    else:
        with open(path, "r", encoding="utf-8") as f:
            
            ### Lecture de l'en-tête
            header = f.readline().rstrip("\n").split("\t")
            tissues = header[2:]
            data = {}

            ### Parcours des lignes du fichier
            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) < 3:
                    continue
                
                gene = parts[0]
                stat = parts[1].strip()
                
                if stat != "count":
                    continue
                
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

