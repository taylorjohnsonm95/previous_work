#!/usr/bin/env python3
#get_path.py

import subprocess

#open ko output
ko = open('ko.txt')
#open files for out and error files
out = open('get_path.txt', 'w')
err = open('get_path.err', 'w')

#iterate over lines of ko output
for ko_line in ko:
    #remove line terminator
    ko_line = ko_line.rstrip()
    #split line on whitespace
    fields = ko_line.split()
    if len(fields) > 1:
        ko = fields[1]

        result = subprocess.call("curl http://rest.kegg.jp/link/pathway/ko/", stdout=out, stderr=err, shell=True)

