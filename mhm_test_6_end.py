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
clean_file = open("new_simple_test_3.fasta","w")
with open("allH3human_shortNames (3).fasta","r") as fopen:
    for lines in fopen:
        #print(lines)
        if lines.startswith(">"):
            #print(lines.split("/")[-1])
            #print(lines)
            #print(lines.strip("\n"))
            #print(lines[0:-3])
            #print(lines.split("/")[-1])
            #print(len(lines.split("/")[-1]))
            if len(lines.split("/")[-1]) ==3 and int(lines.split("/")[-1])>24:
                clean_file.write(lines[0:-3]+"19"+lines[-3::])
            if len(lines.split("/")[-1]) ==3 and int(lines.split("/")[-1])<24:
                clean_file.write(lines[0:-3]+"20"+lines[-3::])
            if len(lines.split("/")[-1]) ==4:
                lines=lines[0:-5]+"\n"
                if len(lines.split("/")[-1]) ==3 and int(lines.split("/")[-1])>24:
                    clean_file.write(lines[0:-3]+"19"+lines[-3::])
                if len(lines.split("/")[-1]) ==3 and int(lines.split("/")[-1])<24:
                    clean_file.write(lines[0:-3]+"20"+lines[-3::])
            if len(lines.split("/")[-1]) ==5:
                clean_file.write(lines)
            if len(lines.split("/")[-1])!=3 and len(lines.split("/")[-1])!=4 and len(lines.split("/")[-1])!=5:
                print(lines)
                
        else:
            clean_file.write(lines)
clean_file.close()

#Nepal