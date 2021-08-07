## Scripts

assembly.sh

Assembles reads from each sample individually using megahit


concatenate.sh

Combines all of the assemblies while keeping sample names with vamb function and 
builds an index with bowtie2


align.sh

Aligns samples with bowtie2, sorts, indexes and removes duplicates


bin.sh

Bins concatenated assembly with vamb and uses depth as input


