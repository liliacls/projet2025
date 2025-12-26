import matplotlib.pyplot as plt

from io_utils import load_archs4_counts_only
from stats_utils import total_count_tissue
from stats_utils import total_count_gene


# PART 1 : TOP 10 des tissus/cellules avec le plus de comptes

def plot_tissue_total(tissue_totals, top_n=10, log_scale=True):
    
# Tri décroissant
    
    items = sorted(tissue_totals.items(), key=lambda x: x[1], reverse=True)
    if top_n :
        items = items[:top_n]

    tissues = [t for t, _ in items]
    values = [v for _, v in items]

# Caractéristiques et axe du plot

    plt.figure(figsize=(12, 6))
    colors = plt.cm.tab10(range(len(values)))
    bars = plt.bar(tissues, values, color=colors)

# Mise en forme du plot visuellement
   
    for bar, value in zip(bars, values):
        plt.text(                                     
            bar.get_x() + bar.get_width() / 2,        
            bar.get_height(),
            f"{value:.2f}",
            ha="center",
            va="bottom",
            fontsize=9
        )

    plt.xlabel("Tissues / Cells")
    plt.ylabel("Total read counts")
    plt.title("Total read counts per tissue")

    if log_scale:
        plt.yscale("log")
        plt.ylabel("Total read counts (log scale)")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

#### PART 2 : TOP 10 des gènes avec le plus de comptes ####

def plot_gene_total(gene_totals, top_n=10, log_scale=True):
    
#tri décroissant
    
    items = sorted(gene_totals.items(), key=lambda x: x[1], reverse=True)
    if top_n :
        items = items[:top_n]

    genes = [g for g, _ in items]
    values = [v for _, v in items]

# Caractéristiques et axe du plot

    plt.figure(figsize=(12, 6))
    colors = plt.cm.tab10(range(len(values)))
    bars = plt.bar(genes, values, color=colors)

# Mise en forme du plot visuellement
   
    for bar, value in zip(bars, values):
        plt.text(                                     
            bar.get_x() + bar.get_width() / 2,        
            bar.get_height(),
            f"{value:.2f}",
            ha="center",
            va="bottom",
            fontsize=9
        )

    plt.xlabel("Genes")
    plt.ylabel("Total read counts")
    plt.title("Top genes by total read count")

    if log_scale:
        plt.yscale("log")
        plt.ylabel("Total read counts (log scale)")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

if __name__ == "__main__":
    # Chargement des données
    tissues, data = load_archs4_counts_only("data/mini_archs4.tsv.gz")

    # Plot TOP 10 tissus
    tissue_totals = total_count_tissue(data, tissues)
    plot_tissue_total(tissue_totals)

    # Plot TOP 10 gènes
    gene_totals = total_count_gene(data)
    plot_gene_total(gene_totals)
    
    plt.show()

