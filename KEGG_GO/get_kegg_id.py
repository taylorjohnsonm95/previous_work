#!/usr/bin/env python3
#get_kegg_id.py

import subprocess

#open BLAST ouput
blast_output = open('../BLAST/alignPredicted.txt')
#open files for stdout and stderr
out = open('kegg.txt', 'w')
err = open('kegg.err', 'w')

#iterate over lines of BLAST output
for blast_line in blast_output:
    #remove line terminator 
    blast_line = blast_line.rstrip()
    #split line on whitespace
    fields = blast_line.split()
    sp = fields[1]
    evalue = fields[7]
    print(sp + "\t" + evalue)
    #check for evalue less than 1e-180
    if float(fields[7]) < float("1e-180"):
        #call the KEGG API
        result = subprocess.call("curl http://rest.kegg.jp/conv/genes/uniprot:" + sp, stdout=out, stderr=err, shell=True)


