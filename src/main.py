import os
import webbrowser

from io_utils import load_archs4
from stats_utils import total_count_tissue, total_count_gene, summarize
from plotting import plot_tissue_total, plot_gene_total

def generate_html_report(path, tissues, data):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Expression Matrix Report</title>
    <style>
    body {{
        font-family: Arial, sans-serif;
        margin: 40px;
    }}

    h1 {{
        margin-top: 0;
    }}

    .summary-box {{
        border: 2px solid black;
        background-color: #fde7ef; /* rose pâle */
        padding: 20px 25px;
        border-radius: 8px;
        max-width: 900px;
        margin-bottom: 40px;
    }}

    .figure-box {{
    border: 2px solid black;
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 40px;
    max-width: 950px;
}}

    img {{
        max-width: 900px;
        margin-bottom: 40px;
    }}
</style>
</head>
<body>

<div class="summary-box">
    <h1>Expression Matrix — Summary Report</h1>

    <p><strong>File:</strong> {path}</p>
    <p><strong>Number of tissues / cells:</strong> {len(tissues)}</p>
    <p><strong>Number of genes:</strong> {len(data)}</p>
</div>

<h2>Top 10 tissues / cells by total read counts</h2>
<div class="figure-box">
    <img src="top_tissues.png">
</div>

<h2>Top 10 genes by total read counts</h2>
<div class="figure-box">
    <img src="top_genes.png">
</div>

</body>
</html>
"""
    with open("web_report/report.html", "w", encoding="utf-8") as f:
        f.write(html)


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
    os.makedirs("web_report", exist_ok=True)

    plot_tissue_total(tissue_totals, top_n=10, log_scale=True, output_path="web_report/top_tissues.png" )
   
    plot_gene_total(gene_totals, top_n=10, log_scale=True, output_path="web_report/top_genes.png")

    generate_html_report(path, tissues, data)

    report_path = os.path.abspath("web_report/report.html")
    webbrowser.open("file://" + report_path)

if __name__ == "__main__":
    main()