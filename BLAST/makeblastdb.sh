#!/usr/bin/env bash

makeblastdb \
 -in ../RNA-Seq/trinity_de-novo/Trinity.fasta \ 
 -dbtype nucl \
 -parse_seqids
