import os
import re
import pandas as pd
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import Phylo
from Bio import AlignIO
from Bio.Align import AlignInfo
import subprocess
from prody import *
## Simplify name of sequences
clean_file = open("new_trial_2.fasta","w")
with open("961713595786-human.fasta","r") as fopen:
    for lines in fopen:
        #print(lines)
        if lines.startswith(">"):
            #print(lines)
            #print(lines.split("Strain Name:")[1].split("|")[0].split("/")[-1])
            if len(lines.split("Strain Name:")[1].split("|")[0].split("/")[-1])==2 and int(lines.split("Strain Name:")[1].split("|")[0].split("/")[-1])>24:
                #print(lines.split("Strain Name:")[1].split("|")[0][0:-2])
                clean_file.write(lines.split("Strain Name:")[1].split("|")[0][0:-2]+"19"+lines.split("Strain Name:")[1].split("|")[0][-2::])
            if len(lines.split("Strain Name:")[1].split("|")[0].split("/")[-1])==2 and int(lines.split("Strain Name:")[1].split("|")[0].split("/")[-1])<24: 
                clean_file.write(lines.split("Strain Name:")[1].split("|")[0][0:-2]+"20"+lines.split("Strain Name:")[1].split("|")[0][-2::]) 
            if len(lines.split("Strain Name:")[1].split("|")[0].split("/")[-1])==4:
                #print(lines.split("Strain Name:")[1].split("|")[0])
                clean_file.write(lines.split("Strain Name:")[1].split("|")[0]) 
            #print(lines.split("Strain Name:")[1].split("|")[0])
            #print(lines.split("Strain Name:")[1].split("|")[0].split("/")[-1])
        else:
            clean_file.write(lines)
clean_file.close()