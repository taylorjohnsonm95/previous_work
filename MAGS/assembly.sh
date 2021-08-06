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

OUTDIR=./assembly/
mkdir -p ${OUTDIR}

. /etc/profile.d/modules.sh
module load default-environment
module load megahit/1.1.3

megahit -t 16 -1 ${FWDFASTQ} -2 ${REVFASTQ} -r ${UNPFASTQ} -o ${OUTDIR}/${SAMPLEID}

