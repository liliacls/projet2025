"""
Main script for the analysis and visualization of a gene expression matrix.

The workflow separates data loading, statistical analysis, visualization, and reporting to ensure clarity and modularity.

The os module is used to handle file system operations such as creating output directories and building platform-independent file paths.

The webbrowser module is used to automatically open the generated HTML report in the default web browser/
"""

import os
import webbrowser

from io_utils import load_matrix
from stats_utils import total_count_tissue, total_count_gene, summarize
from plotting import plot_tissue_total, plot_gene_total

def generate_html_report(report_dir, path, tissues, data):
   
    """ 
    Generate an HTML summary report for a gene expression matrix.

    The report includes :
    - Name and path of the input expression matrix file
    - Number of tissues/cells and genes
    - Visualization of the top 10 tissues and genes by total read counts
    
    The HTML report displays plots that are generated separately by the plotting functions.
    """

    # HTML content of the report
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
    # Build the path to the HTML report file
    report_file = os.path.join(report_dir, "report.html")
    
    # Write the HTML content to disk using UTF-8 encoding
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(html)

def main():

    """ Main entry point of the program
    
    This program :
    --------------
    1. Loads the expression matrix from a TSV/TSV.GZ file
    2. Computes total read counts per gene and per tissue/cell
    3. Identifies genes and tissues with minimum and maximum total counts
    4. Generates bar plots for the top 10 genes and tissues
    5. Creates and opens an HTML summary report
    """

    # Path to the input expression matrix
    path = "../data/ARCHS4.tsv.gz"
    report_dir = "web_report"
   
   
    print()
    print("Expression matrix — summary report")
    print("**********************************")
  
    # -----------------------------------
    # PART 1 : Load the expression matrix
    # -----------------------------------
    tissues, data = load_matrix(path)
   
    print()
    print("Input data")
    print("**********")
    print("File:", path)
    print("Number of tissues/cells :", len(tissues))
    print("Number of genes :", len(data))
   
    # ----------------------------------------------
    # PART 2 : Compute totals and summary statistics
    # ----------------------------------------------

    # Total read counts per tissue/cell
    tissue_totals = total_count_tissue(tissues, data)

    # Total read counts per gene
    gene_totals = total_count_gene(data)

    # Summary of min/max values for genes and tissues
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

    # ---------------------------------------
    # PART 3 : Generate plots and HTML report
    # ---------------------------------------

    # Create the output directory if it does not already exist
    os.makedirs(report_dir, exist_ok=True)

    # Generate and save the bar plot for tissues/cells
    plot_tissue_total(tissue_totals, top_n=10, log_scale=True, output_path=os.path.join(report_dir, "top_tissues.png"))
   
    # Generate and save the bar plot for genes
    plot_gene_total(gene_totals, top_n=10, log_scale=True, output_path=os.path.join(report_dir, "top_genes.png"))

    # Generate the HTML summary report
    generate_html_report(report_dir, path, tissues, data)
    
    # Open the HTML report in the default web browser
    report_path = os.path.abspath(os.path.join(report_dir, "report.html"))
    webbrowser.open("file://" + report_path)

if __name__ == "__main__":
    main()