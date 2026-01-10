"""
Module dedicated to data visualization for gene expression analysis.

This module provides functions to generate bar plots illustrating:
- The top tissues/cells by total read counts
- The top genes by total read counts

Matplotlib is used to produce publication-quality figures that can be displayed interactively or saved as PNG files for inclusion in an HTML report.

The plotting functions are designed to be reusable and configurable: number of items displayed, logarithmic scale, etc.
"""

import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
# PART 1 : Top 10 tissues / cells with the highest read counts
# ---------------------------------------------------------------------

def plot_tissue_total(tissue_totals, top_n=10, log_scale=True, output_path=None):
    
    # Sort tissues/cells by total counts in descending order
    items = sorted(tissue_totals.items(), key=lambda x: x[1], reverse=True)
    if top_n:
        items = items[:top_n]

    tissues = [t for t, _ in items]
    values = [v for _, v in items]

    # Create the figure and bar plot
    plt.figure(figsize=(12, 6))
    colors = plt.cm.tab10(range(len(values)))
    bars = plt.bar(tissues, values, color=colors)

    # Add numerical labels above each bar
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

    # Set axis labels and plot title
    plt.xlabel("Tissues/Cells", fontsize=12, fontweight="bold")
    plt.ylabel("Total counts", fontsize=12, fontweight="bold")
    plt.title("Top tissues/cells by total count", fontsize=14, fontweight="bold", pad=15)

    # Apply logarithmic scale to the y-axis if requested
    if log_scale:
        plt.yscale("log")
        plt.ylabel("Total counts (log scale)", fontsize=12, fontweight="bold")

    # Format tick labels
    plt.xticks(fontsize=10, rotation=45, ha="right")
    plt.yticks(fontsize=10)
    
    # Customize axis borders for better visual appearance
    ax = plt.gca()
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)

    # Adjust layout to avoid overlapping elements
    plt.tight_layout()
    
    # Save the figure to disk or display it interactively
    if output_path:
        plt.savefig(output_path, dpi=300)
        plt.close()
    else:
        plt.show()
    
# --------------------------------------------------
# PART 2 : Top 10 genes with the highest read counts
# --------------------------------------------------

def plot_gene_total(gene_totals, top_n=10, log_scale=True, output_path=None):
    
    # Sort genes by total counts in descending order
    items = sorted(gene_totals.items(), key=lambda x: x[1], reverse=True)
    if top_n:
        items = items[:top_n]

    genes = [g for g, _ in items]
    values = [v for _, v in items]

    # Create the figure and bar plot
    plt.figure(figsize=(12, 6))
    colors = plt.cm.tab10(range(len(values)))
    bars = plt.bar(genes, values, color=colors)

    # Add numerical labels above each bar
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

    # Set axis labels and plot title
    plt.xlabel("Genes", fontsize=12, fontweight="bold")
    plt.ylabel("Total counts", fontsize=12, fontweight="bold")
    plt.title("Top genes by total count", fontsize=14, fontweight="bold", pad=15)

    # Apply logarithmic scale to the y-axis if requested
    if log_scale:
        plt.yscale("log")
        plt.ylabel("Total counts (log scale)", fontsize=12, fontweight="bold", labelpad=15)
    
    # Format tick labels
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.yticks(fontsize=10)

    # Customize axis borders for better visual appearance
    ax = plt.gca()
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)

    # Adjust layout to avoid overlapping elements
    plt.tight_layout()

    # Save the figure to disk or display it interactively
    if output_path:
        plt.savefig(output_path, dpi=300)
        plt.close()
    else:
        plt.show()