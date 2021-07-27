#!/usr/bin/env Rscript
#mergeAll.R

#load blast results using tab (\t) as separator
blast <- read.table("../BLAST/alignPredicted.txt", sep="\t", header=FALSE, quote = "",)
#set column names to match fields in BLAST
colnames(blast) <- c("qseqid", "sacc", "qlen", "slen", "length", "nident", "pident", "evalue", "stitle")
#calculate cooverage as nident/slen
blast$cov <- blast$nident/blast$slen
#select blast rows where coverage is greater than .9
blast <- subset(blast, cov > .9, select=-c(stitle))

#read kegg.txt
kegg <- read.table("kegg.txt", sep="\t", header=FALSE)
#set column names for kegg
colnames(kegg) <- c("sacc", "kegg")
#remove the up: prefix
kegg$sacc <- gsub("up:", "", kegg$sacc)

#merge BLAST and kegg
blast_kegg <- merge(blast, kegg)

#read ko.txt
ko <- read.table("ko.txt", sep="\t", header=FALSE)
#set column names for ko
colnames(ko) <- c("kegg", "ko")
#remove ko: prefix
ko$kegg <- gsub("ko:", "", ko$kegg)

#merge kegg and ko
kegg_ko <- merge(blast_kegg, ko)

#read get_path.txt
path <- read.table("get_path.txt", sep="\t", header=FALSE)
#set column names for path
colnames(path) <- c("ko", "path")
#remove path: prefix
path$ko <- gsub("path:", "", path$ko)

#merge ko and path
ko_path <- merge(kegg_ko, path)

#read getPathDesc.sh
desc <- read.table("ko", sep="\t", header=FALSE)
#set column names for desc
colnames(desc) <- c("path", "desc")

#merge path and desc
path_desc <- merge(ko_path, desc)

#read sp_go.txt
GO <- read.csv("sp_go.txt", sep="\t", header=FALSE)
#set column names for GO
colnames(GO) <- c("sacc", "GO")

#merge desc and GO
desc_GO <- merge(path_desc, GO)

#write to a file
write.csv(desc_GO, file = "table.txt")

