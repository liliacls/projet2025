import matplotlib.pyplot as plt

#### PART 1 : TOP 10 des tissus/cellules avec le plus de comptes ###

def plot_tissue_total(tissue_totals, top_n=10, log_scale=True, output_path=None):
    # Tri décroissant
    items = sorted(tissue_totals.items(), key=lambda x: x[1], reverse=True)
    if top_n:
        items = items[:top_n]

    tissues = [t for t, _ in items]
    values = [v for _, v in items]

    # Caractéristiques et axe du plot
    plt.figure(figsize=(12, 6))
    colors = plt.cm.tab10(range(len(values)))
    bars = plt.bar(tissues, values, color=colors)

    # Mise en forme du plot visuellement
    for bar, value in zip(bars, values):
        label = f"{int(value):,}".replace(",", " ")
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            label,
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold"
        )

    plt.xlabel("Tissues / Cells", fontsize=12, fontweight="bold")
    plt.ylabel("Total read counts", fontsize=12, fontweight="bold")
    plt.title("Total read counts per tissue", fontsize=14, fontweight="bold", pad=15)

    if log_scale:
        plt.yscale("log")
        plt.ylabel("Total read counts (log scale)", fontsize=12, fontweight="bold")

    plt.xticks(fontsize=10, rotation=45, ha="right")
    plt.yticks(fontsize=10)

    ax = plt.gca()
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)

    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300)
        plt.close()
    else:
        plt.show()
    

### PART 2 : TOP 10 des gènes avec le plus de comptes ###

def plot_gene_total(gene_totals, top_n=10, log_scale=True, output_path=None):
    # Tri décroissant
    items = sorted(gene_totals.items(), key=lambda x: x[1], reverse=True)
    if top_n:
        items = items[:top_n]

    genes = [g for g, _ in items]
    values = [v for _, v in items]

    # Caractéristiques et axe du plot
    plt.figure(figsize=(12, 6))
    colors = plt.cm.tab10(range(len(values)))
    bars = plt.bar(genes, values, color=colors)

    # Mise en forme du plot visuellement
    for bar, value in zip(bars, values):
        label = f"{int(value):,}".replace(",", " ")
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            label,
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold"
        )

    plt.xlabel("Genes", fontsize=12, fontweight="bold")
    plt.ylabel("Total read counts (log scale)", fontsize=12, fontweight="bold")
    plt.title("Top genes by total read count", fontsize=14, fontweight="bold", pad=15)

    if log_scale:
        plt.yscale("log")
        plt.ylabel("Total read counts (log scale)")

    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.yticks(fontsize=10)

    ax = plt.gca()
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)

    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300)
        plt.close()
    else:
        plt.show()