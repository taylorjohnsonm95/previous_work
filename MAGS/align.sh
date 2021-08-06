#!/bin/bash

#$ -cwd
#$ -N assembly
#$ -t 1
#$ -pe smp 30
#$ -q compute.q


SAMPLELIST='pwd'/input_file.txt

SAMPLE=($(awk "NR==$SGE_TASK_ID" $SAMPLELIST))
SAMPLEID=${SAMPLE[0]}
FWDFASTQ=${SAMPLE[1]}
REVFASTQ=${SAMPLE[2]}
UNPFASTQ=${SAMPLE[3]}

OUTDIR=./align/
mkdir -p ${OUTDIR}

. /etc/profile.d/modules.sh
module load default-environment
module load intel-tbb-oss/intel64/2017_20160722oss
module load bowtie2/2.3.2
module load samtools/1.4.1
module load picard/2.9.4

bowtie2 -q -p 16 --sensitive-local -x MAGS \
    -1 ${FWDFASTQ} -2 ${REVFASTQ} -U ${UNPFASTQ} -S ${OUTDIR}/${SAMPLEID}.aligned.sam 

samtools view -blS ${OUTDIR}/${SAMPLEID}.aligned.sam | samtools sort -@ 16 -T \
    sorting_${SAMPLEID} -o ${OUTDIR}/${SAMPLEID}.aligned.sorted.bam

samtools index ${OUTDIR}/${SAMPLEID}.aligned.sorted.bam

java -jar picard.jar MarkDuplicates INPUT=${OUTDIR}/${SAMPLEID}.aligned.sorted.bam \
    METRICS_FILE=${SAMPLEID}.mark_duplicates.metrics.txt \
    OUTPUT=${OUTDIR}/${SAMPLEID}.aligned.sorted.duplicates.removed.bam \
    REMOVE_SEQUENCING_DUPLICATES=true \
    MAX_FILE_HANDLES_FOR_READ_ENDS_MAP=1000 TMP_DIR=.

samtools index ${OUTDIR}/${SAMPLEID}.aligned.sorted.duplicates_removed.bam
    

