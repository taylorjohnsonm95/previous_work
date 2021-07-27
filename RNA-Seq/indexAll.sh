#!/usr/bin/env bash
#indexAll.sh

#initialize a variable that contains the bam directory
fastqPath="/home/johnson.ta/BINF6308/RNA-Seq/bam/"
#initialize a variable that contains the sample suffix
sampleSuffix=".sorted.bam"
indexOut="bam/"

#loop through the sorted bam files
function indexAll {
for files in $fastqPath*$sampleSuffix
do
    #remove the path
    pathRemoved="${files/$fastqPath/}"
    #remove the sample suffix
    sampleName="${pathRemoved/$sampleSuffix/}"

#use samtools to create an index
samtools index \
    $fastqPath$sampleName$sampleSuffix \
    1>"$fastqPath/${sampleName}.sorted.bam.bai"
done
}
indexAll 1>indexAll.log 2>indexAll.err &


