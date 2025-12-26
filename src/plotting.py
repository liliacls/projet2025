import matplotlib.pyplot as plt

### TOP 10 des tissus/cellules ou  gènes avec le plus de comptes ###

# Tri du dico

def plot_top10(totals_dict, title, xlabel, ylabel, top_n=10, log_scale=True):
    items = sorted(totals_dict.items(), key=lambda x: x[1], reverse=True)[:top_n]
    labels = [k for k, _ in items]
    values = [v for _, v in items]

# Création de la figure

    plt.figure(figsize=(12, 6))
    bars = plt.bar(labels, values)

# Ajout des valeurs numériques au-dessus de chaque barre
   
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width() / 2,        
                 bar.get_height(),
                 "{:.2f}".format(value),
                 ha="center",
                 va="bottom",
                 fontsize=9)

# Axes et titres

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

# Mise en forme du plot

    if log_scale:
        plt.yscale("log")
        plt.ylabel(ylabel + "(log scale)")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
 
