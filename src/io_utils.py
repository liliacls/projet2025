import gzip 
    
def load_archs4_counts_only(path="ARCHS4.tsv.gz"):
    data = {}

    with gzip.open(path, "rt", encoding="utf-8") as f:
         first_line = f.readline().strip()
         header = first_line.split('\t')
         tissues = header[2:]

    for line in f :
          parts = line.rstrip("\n").split('\t')
          gene = parts[0]
          stat = parts[1]
          
          if stat != "count":
              continue

    counts = list(map(int, parts[2:]))
    data[gene] = dict(zip(tissues, counts))
    return tissues, data





