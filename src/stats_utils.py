### En entrée : 
### --> dico {gène : liste des comptages par tissus/cellules}
### --> liste des tissus/cellules (même ordre que les comptages)
### En sortie : 
### --> dico {gène : somme des comptages sur tous les tissus/cellules}
### --> listes des gènes/tissus associés aux valeurs min et max 

def total_count_gene(data):

### Fonction qui calcul le nombre total de comptages pour chaque tissu/cellule tous gènes confondus

    return {gene: sum(counts) for gene, counts in data.items()}


def total_count_tissue(data, tissues):

    totals = {t: 0 for t in tissues}

    for counts in data.values():
        for i, value in enumerate(counts):
            totals[tissues[i]] = totals[tissues[i]] + value

    return totals

def min_max_items(d):

### Fonction qui identifie les clefs associées aux valeurs minimale et maximale dans le dico

    min_val = min(d.values())  
    max_val = max(d.values())

    min_items = [k for k, v in d.items() if v == min_val]
    max_items = [k for k, v in d.items() if v == max_val]

    return min_items, min_val, max_items, max_val
