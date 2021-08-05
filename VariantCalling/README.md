# Title

Variant Calling

# Scripts

## getGenome.sh

Retrieves the reference genome from database

## getReads.sh

Retrieves NGS reads used in comparison paper

## trimReads.sh

Quality trims the reads using Trimmomatic

## indexGenome.sh

Indexes the genome for use by BWA

## alignReads.sh

Aligns the reads using bwa mem

## sort.sh

Sorts the file created by bwa mem to a sorted bam

## indexReads.sh

Creates an index for reads

## runDeepVariant.sh

Produces a VCF file using DeepVariant

# Methods

Variant calling is a process to identify variants from sequence data.
The first step to find variation is to trim NGS reads based on quality
using the program Trimmomatic (Bolger, Lohse, and Usadel 2014). The
trimmed reads from an individual are then aligned against the indexed
reference genome using BWA (Li and Durbin 2009). The alignments are
analyzed using a variant calling program such as Genome Analysis Tool
Kil (McKenna et al. 2010) or DeepVariant (Supernat et al. 2018)

# Refereneces

<div id="refs" class="references">

<div id="ref-Bolger">

Bolger, Anthony M., Marc Lohse, and Bjoern Usadel. 2014. “Trimmomatic: A
Flexible Trimmer for Illumina Sequence Data.” *Bioinformatics (Oxford,
England)* 30 (15): 2114–20.
<https://doi.org/10.1093/bioinformatics/btu170>.

</div>

<div id="ref-Li">

Li, Heng, and Richard Durbin. 2009. “Fast and Accurate Short Read
Alignment with Burrows-Wheeler Transform.” *Bioinformatics (Oxford,
England)* 25 (14): 1754–60.
<https://doi.org/10.1093/bioinformatics/btp324>.

</div>

<div id="ref-McKenna">

McKenna, Aaron, Matthew Hanna, Eric Banks, Andrey Sivachenko, Kristian
Cibulskis, Andrew Kernytsky, Kiran Garimella, et al. 2010. “The Genome
Analysis Toolkit: A MapReduce Framework for Analyzing Next-Generation
DNA Sequencing Data.” *Genome Research* 20 (9): 1297–1303.
<https://doi.org/10.1101/gr.107524.110>.

</div>

<div id="ref-Supernat">

Supernat, Anna, Oskar Valdimar Vidarsson, Vidar M. Steen, and Tomasz
Stokowy. 2018. “Comparison of Three Variant Callers for Human Whole
Genome Sequencing.” *Scientific Reports* 8 (1): 17851–1.
<https://doi.org/10.1038/s41598-018-36177-7>.

</div>

</div>
