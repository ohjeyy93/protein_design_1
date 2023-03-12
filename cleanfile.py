#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 15:56:13 2020
@author: karen
"""
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
clean_file = open("new_trial.fasta","w")
with open("961713595786-human.fasta","r") as fopen:
    for lines in fopen:
        if lines.startswith(">"):
            #if "H3N2" in lines:
            #    print(lines)
            #    print(lines.split("Influenza A virus ")[1].split("|Strain Name:")[0].strip("(H3N2)"))
            if "H3N2" not in lines:
                print(lines)
                #print(len(lines.split("Influenza A virus ")[1].split("|Strain Name:")[0]))
                print(lines.split("Influenza A virus ")[1].split("|Strain Name:")[0])
        #clean_file.write(">"+name+"\n")
        else:
            clean_file.write(lines)
clean_file.close()