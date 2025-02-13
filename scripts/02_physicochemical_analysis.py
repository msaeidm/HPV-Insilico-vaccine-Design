from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio import SeqIO

def analyze_protein(seq_record):
    seq = str(seq_record.seq)
    analysed_seq = ProteinAnalysis(seq)
    mw = analysed_seq.molecular_weight()
    pI = analysed_seq.isoelectric_point()
    gravy = analysed_seq.gravy()
    instability = analysed_seq.instability_index()
    return mw, pI, gravy, instability

def main():
    # Load the fusion construct
    record = SeqIO.read("data/sequences/Fusion_Construct.fasta", "fasta")
    mw, pI, gravy, instability = analyze_protein(record)
    print(f"Molecular Weight: {mw:.2f} Da")
    print(f"Isoelectric Point: {pI:.2f}")
    print(f"GRAVY: {gravy:.2f}")
    print(f"Instability Index: {instability:.2f}")

    # Save results to a table
    with open("results/tables/physicochemical_properties.csv", "w") as f:
        f.write("Property,Value\n")
        f.write(f"Molecular Weight,{mw:.2f}\n")
        f.write(f"Isoelectric Point,{pI:.2f}\n")
        f.write(f"GRAVY,{gravy:.2f}\n")
        f.write(f"Instability Index,{instability:.2f}\n")

if __name__ == "__main__":
    main()
