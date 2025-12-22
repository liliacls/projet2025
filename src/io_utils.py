import gzip


def load_archs4_counts_only(path="ARCHS4.tsv.gz"):
    with gzip.open(path, "rt", encoding="utf-8") as f:
        header = f.readline().rstrip("\n").split("\t")
        tissues = header[2:]

        data = {}

        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 3:
                continue

            gene = parts[0]
            stat = parts[1]

            if stat != "count":
                continue

            counts = []
            for x in parts[2:]:
                try:
                    counts.append(int(x))
                except ValueError:
                    try:
                        counts.append(int(float(x)))
                    except ValueError:
                        counts.append(0)

            data[gene] = counts

    return tissues, data

if __name__ == "__main__":
    print("DEBUG: io_utils lancé directement")

    tissues, data = load_archs4_counts_only("data/mini_archs4.tsv.gz")

    print("Tissues:", tissues)
    print("Data:", data)
