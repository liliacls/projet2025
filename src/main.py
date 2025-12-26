import matplotlib.pyplot as plt

from io_utils import load_archs4
from stats_utils import total_count_gene, total_count_tissue, min_max_items
from plotting import plot_top10


def main():
    path = "ARCHS4.tsv.gz"

# PARTIE 1 : Lecture matrice

    tissues, data = load_archs4(path)

    print("Nombre de tissus/cellules :", len(tissues))
    print("Nombre de gènes :", len(data))

# PARTIE 2 : Totaux + min/max

    gene_totals = total_count_gene(data)
    tissue_totals = total_count_tissue(tissues, data)

    min_genes, min_gene_val, max_genes, max_gene_val = min_max_items(gene_totals)
    min_tissues, min_tissue_val, max_tissues, max_tissue_val = min_max_items(tissue_totals)

    print("Gène(s) min  (total =", min_gene_val, ") :", min_genes)
    print("Gène(s) max  (total =", max_gene_val, ") :", max_genes)
    print("Tissu(x) min (total =", min_tissue_val, ") :", min_tissues)
    print("Tissu(x) max (total =", max_tissue_val, ") :", max_tissues)

 # PARTIE 3 : Plots TOP 10

    plot_top10(
        gene_totals,
        title="Top 10 gènes avec le plus de comptes",
        xlabel="Genes",
        ylabel="Total read counts",
        top_n=10,
        log_scale=True
    )

    plot_top10(
        tissue_totals,
        title="Top 10 tissus/cellules avec le plus de comptes",
        xlabel="Tissues / Cells",
        ylabel="Total read counts",
        top_n=10,
        log_scale=True
    )

    plt.show()


if __name__ == "__main__":
    main()
