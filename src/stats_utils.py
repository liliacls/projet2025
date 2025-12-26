def total_count_gene(data):

# Fonction qui calcule le nombre total de comptages pour chaque gène dans tous les tissus/cellules
# data --> dico {gène : liste des comptages pour chaque tissu/cellule}
# Exemple : {"GENE1": [2,10,15], "GENE2...]}
    
    return {gene: sum(counts) for gene, counts in data.items()}

# return (dico) --> {gène : somme des comptages des tissus/cellules}
# Exemple : {"GENE1" : [27], "GENE2" : [...]}

def total_count_tissue(data, tissues):

# Fonction qui calcule le nombre de comptages pour chaque tissu/cellule pour tous les gènes
# data (dico) --> {gène : comptages pour chaque tissu/cellule}
# tissues (liste) --> noms des tissus/cellules dans le même ordre que les comptages dans data
# Exemple : ["tissue-trachea", "tissue-lymphoblastic"...]

# Nouveau dico avec tous les tissus/cellules à 0

    totals = {t: 0 for t in tissues}

# Parcours chaque gène et additionne les comptages par tissu/cellule

    for counts in data.values():
        if len(counts) != len(tissues):
            raise ValueError

        for tissue, value in zip(tissues, counts):
            totals[tissue] += value

    return totals

# return (dico) --> {tissus/cellules : somme totale des comptages}
# Exemple : {"tissues-trachea" :[150], "tissue-lymphoblastic"...}

def min_max_items(d):

# Fonction qui identifie les clefs associées aux valeurs minimale et maximale dans un dico

    min_val = min(d.values())  
    max_val = max(d.values())

    min_items = [k for k, v in d.items() if v == min_val]
    max_items = [k for k, v in d.items() if v == max_val]

    return min_items, min_val, max_items, max_val

 # return (tuples) --> 
 # min_items (liste): clés avec la valeur minimale
 # min_val (float/int): valeur minimale
 # max_items (liste): clés avec la valeur maximale
 # max_val (float/int): valeur maximale 