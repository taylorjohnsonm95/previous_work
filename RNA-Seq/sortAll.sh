#!/usr/bin/env bash

#sortAll.sh

#initialize variable to contain directory of sam files
fastqPath="sam/"
sampleSuffix=".sam"
sortOutPath="bam/"

#make output directory
mkdir -p $sortOutPath

#loop through sam files
function sortAll {
for files in $fastqPath*$sampleSuffix
do 
#remove path from filename  
pathRemoved="${files/$fastqPath/}"
#remove suffix from pathRemoved
sampleName="${pathRemoved/$sampleSuffix/}"

#sort files and output into bam directory 
samtools sort \
$fastqPath$sampleName$sampleSuffix \
-o $sortOutPath${sampleName}.sorted.bam \

done

}


sortAll 1>sortAll.log 2>sortAll.err &

