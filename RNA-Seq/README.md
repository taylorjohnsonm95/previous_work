
# Scripts

trimAll.sh

trims reads by quality score and removes adapters 

AipBuild.sh

Build GMAP database 

buildIIT.sh

Index intron splice sites so align reads across introns and not within them 

alignAll.sh

Align reads against GMAP database with GSNAP

sortAll.sh

Convert to sorted BAM file 

indexAll.sh

Create index from BAM file

mergeAll.sh

Merge all BAM files into one file

runTrinity.sh

Assemble the transcriptome

analyzeTrinity.sh

Get contig stats

trinityDenNovo.sh

de-novo assembly

analyzeTrinityDeNovo.sh

Get contig stats


# Methods
## Reference-guided and De novo assembly of RNA-Seq data
Read alignments produced from RNA-Sequencing are used to build two types of Transcriptomes. One is reference-guided and one is de novo. Trinity [1] will be used for both types of assemblies. The 25 paired reads used for the alignment were trimmed based on quality score and adapter sequences. A GMAP database was created to align the trimmed files. The alignments were sorted and indexed.
For the reference-guided assembly, sorted bam files were merged to a single bam file using samtools [2].  Trinity used this file to assemble a genome-guided Transcriptome as a fasta file in the output directory. TrinityStats was used to view the size of the assembled contigs and length distribution of the assembly.
De novo assembly required a list of files for left and right reads.  After running Trinity the output fasta files was directed to a new directory. TrinityStats was used again to view length and contig information. 

[1]Brian J Haas, Alexie Papanicolaou, Moran Yassour, Manfred Grabherr, Philip D Blood, Joshua Bowden, Matthew Brian Couger, David Eccles, Bo Li, Matthias Lieber, Matthew D Macmanes, Michael Ott, Joshua Orvis, Nathalie Pochet, Francesco Strozzi, Nathan Weeks, Rick Westerman, Thomas William, Colin N Dewey, Robert Henschel, Richard D Leduc, Nir Friedman, and Aviv Regev. "De Novo Transcript Sequence Reconstruction from RNA-seq Using the Trinity Platform for Reference Generation and Analysis." Nature Protocols 8.8 (2013): 1494-1512. Web.

[2]Li, Heng, Bob Handsaker, Alec Wysoker, Tim Fennell, Jue Ruan, Nils Homer, Gabor Marth, Goncalo Abecasis, and Richard Durbin. "The Sequence Alignment/Map Format and SAMtools." Bioinformatics 25.16 (2009): 2078-079. Web.
