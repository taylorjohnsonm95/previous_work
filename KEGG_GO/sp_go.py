#!/usr/bin/env python3
#sp_go.py

#open output file for writing
subset = open("sp_go.txt", 'w')
#open UniProt to Go Mapping file
sp = open("/scratch/SampleDataFiles/goa_uniprot_all.gaf")
#iterate over lines
for line in sp:
    #split on tabs
    fields = line.split("\t")
    #check for 6 columns
    if len(fields) > 4:
        #write columns 2 and 5
        subset.write(fields[1] + "\t" + fields[4] + "\n")

