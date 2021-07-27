#!/usr/bin/env python3
#get_ko

import subprocess

#open KEGG to KO mapping
kegg = open('kegg.txt')
kegg_ids = {}
#open files for stdout and stderr
out = open('ko.txt', 'w')
err = open('ko.err', 'w')

#iterate over lines of KEGG IDs
for kegg_line in kegg:
    #remove line terminator
    kegg_line = kegg_line.rstrip()
    #split line on whitespace
    fields = kegg_line.split()
    if len(fields) > 1:
        kegg = fields[1]
        kegg_ids[kegg] = 1

for kegg_id in kegg_ids:
    print(kegg_id)
    result = subprocess.call("curl http://rest.kegg.jp/link/ko/" + kegg_id, stdout=out, stderr=err, shell=True)

