import matplotlib.pyplot as plt

from io_utils import load_archs4
from stats_utils import total_count_tissue, total_count_gene, summarize
from plotting import plot_tissue_total, plot_gene_total

def main():
    path = "../data/ARCHS4.tsv.gz"

   
    print()
    print("Expression matrix — summary report")
    print("**********************************")
  
    # PARTIE 1 : Lecture matrice
    
    tissues, data = load_archs4(path)
    print()
    print("Input data")
    print("**********")
    print("File:",path)
    print("Number of tissues/cells :", len(tissues))
    print("Number of genes :", len(data))
   

    # PARTIE 2 : Totaux + min/max
  
    tissue_totals = total_count_tissue(tissues, data)
    gene_totals = total_count_gene(data)

    summary = summarize(tissues, data)


    print()
    print("Gene-level total counts")
    print("***********************")
    print("Min total counts :", (summary["genes"]["min"]["value"]))
    print("Gene(s) :", ", ".join(summary["genes"]["min"]["names"]))
    print("Max total counts :", (summary["genes"]["max"]["value"]))
    print("Gene(s) :", ", ".join(summary["genes"]["max"]["names"]))
   
    print()
    print("Tissue / cell-level total counts")
    print("********************************")
    print("Min total counts :", summary["tissues"]["min"]["value"])
    print("Tissue(s) :", ", ".join(summary["tissues"]["min"]["names"]))
    print("Max total counts :", summary["tissues"]["max"]["value"])
    print("Tissue(s) :", ", ".join(summary["tissues"]["max"]["names"]))

     
    # PARTIE 3 

    plot_tissue_total(tissue_totals, top_n=10, log_scale=True, output_path="web_report/top_tissues.png" )
    plot_gene_total(gene_totals, top_n=10, log_scale=True, output_path="web_report/top_genes.png")

if __name__ == "__main__":
    main()