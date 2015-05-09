def process_FASTA(file):
    lines = open(file).read().splitlines()
    FASTA_seq = lines[1::2] # do not read the > seqx metadata
    return FASTA_seq

seqA = process_FASTA("sequences.fa")
print(len(seqA[1]))