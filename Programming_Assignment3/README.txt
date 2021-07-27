# File Splitting and Nucleotide Stats

# Scripts

## pdb_fasta_splitter.py

./pdb_fasta_splitter.py --infile ss.txt

## nucleotide_statistics_from_fasta.py 

./nucleotide_statistics_from_fasta.py --infile influenza.fasta --outfile influenza.stats.txt

# Description

pdb_fasta_splitter.py splits a fasta file into header and seq lists. It then appends primary structures with headers to a file and secondary structures with  headers to another file. nucelotide_statistics_from_fasta.py also splits a fasta file. It appends nucleotide stats such as count, length, gc content and accession number to a new file. 
