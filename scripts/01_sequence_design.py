from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def read_fasta(file_path):
    records = list(SeqIO.parse(file_path, "fasta"))
    if records:
        return records[0].seq
    else:
        return None

def join_sequences(seq1, seq2, linker="GGGGGGGG"):
    return seq1 + Seq(linker) + seq2

def main():
    # Paths to your sequence files
    e6_path = "data/sequences/HPV16_E6.fasta"
    e7_path = "data/sequences/HPV16_E7.fasta"
    gp96_path = "data/sequences/GP96_NT.fasta"

    # Read sequences
    e6_seq = read_fasta(e6_path)
    e7_seq = read_fasta(e7_path)
    gp96_seq = read_fasta(gp96_path)

    if None in (e6_seq, e7_seq, gp96_seq):
        print("Error reading one or more sequence files.")
        return

    # Join E6 and E7 to form antigen part
    antigen_seq = join_sequences(e6_seq, e7_seq)
    # Join antigen with GP96_NT using linker
    fusion_seq = join_sequences(antigen_seq, gp96_seq)

    # Save fusion protein sequence
    fusion_record = SeqRecord(fusion_seq, id="E6E7-NTGP96", description="Fusion protein construct")
    SeqIO.write(fusion_record, "data/sequences/Fusion_Construct.fasta", "fasta")
    print("Fusion construct saved as Fusion_Construct.fasta")

if __name__ == "__main__":
    main()
