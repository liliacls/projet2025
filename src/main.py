import sys
from io_utils import load_archs4_counts_only

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <path_to_file.tsv.gz>")
        sys.exit(1)

    path = sys.argv[1]

    tissues, data = load_archs4_counts_only(path)

    print("Tissues:", tissues[:5])
    print("Nb genes:", len(data))

if __name__ == "__main__":
    main()
