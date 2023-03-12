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
clean_file = open("allH3human_shortNames_2.fasta","w")
with open("961713595786-human.fasta","r") as fopen:
    for lines in fopen:
        if lines.startswith(">"):
            #print(lines.split("Strain Name:")[1])
            #print(lines.split("Strain Name:")[1].split("/")[3])
            #print(lines.split("Strain Name:")[1].split("/")[3].split("|")[0])
            if len(lines.split("Strain Name:")[1].split("|")[0].split("/")) == 4:
                if len(lines.split("Strain Name:")[1].split("/")[3].split("|")[0])==2 and int(lines.split("Strain Name:")[1].split("/")[3].split("|")[0])<24:
                    #print((lines.split("(")[1]).split("/")[0],(lines.split("(")[1]).split("/")[1],str(20)+(lines.split("(")[1]).split("/")[3])
                    clean_file.write((lines.split("Strain Name:")[1]).split("/")[0]+"/"+(lines.split("Strain Name:")[1]).split("/")[1]+"/"+(lines.split("Strain Name:")[1]).split("/")[2]+"/"+str(20)+(lines.split("Strain Name:")[1]).split("/")[3].split("|")[0]+"\n")
                if len(lines.split("Strain Name:")[1].split("/")[3].split("|")[0])==2 and int(lines.split("Strain Name:")[1].split("/")[3].split("|")[0])>24:
                    clean_file.write((lines.split("Strain Name:")[1]).split("/")[0]+"/"+(lines.split("Strain Name:")[1]).split("/")[1]+"/"+(lines.split("Strain Name:")[1]).split("/")[2]+"/"+str(19)+(lines.split("Strain Name:")[1]).split("/")[3].split("|")[0]+"\n")
                if len(lines.split("Strain Name:")[1].split("/")[3].split("|")[0])==4:
                    clean_file.write((lines.split("Strain Name:")[1]).split("/")[0]+"/"+(lines.split("Strain Name:")[1]).split("/")[1]+"/"+(lines.split("Strain Name:")[1]).split("/")[2]+"/"+(lines.split("Strain Name:")[1]).split("/")[3].split("|")[0]+"\n")
            if len(lines.split("Strain Name:")[1].split("|")[0].split("/")) == 3:
                if len(lines.split("Strain Name:")[1].split("/")[2].split("|")[0])==2 and int(lines.split("Strain Name:")[1].split("/")[2].split("|")[0])<24:
                    #print((lines.split("(")[1]).split("/")[0],(lines.split("(")[1]).split("/")[1],str(20)+(lines.split("(")[1]).split("/")[3])
                    clean_file.write((lines.split("Strain Name:")[1]).split("/")[0]+"/"+(lines.split("Strain Name:")[1]).split("/")[1]+"/"+str(20)+(lines.split("Strain Name:")[1]).split("/")[2].split("|")[0]+"\n")
                if len(lines.split("Strain Name:")[1].split("/")[2].split("|")[0])==2 and int(lines.split("Strain Name:")[1].split("/")[2].split("|")[0])>24:
                    clean_file.write((lines.split("Strain Name:")[1]).split("/")[0]+"/"+(lines.split("Strain Name:")[1]).split("/")[1]+"/"+str(19)+(lines.split("Strain Name:")[1]).split("/")[2].split("|")[0]+"\n")
                if len(lines.split("Strain Name:")[1].split("/")[2].split("|")[0])==4:
                    clean_file.write((lines.split("Strain Name:")[1]).split("/")[0]+"/"+(lines.split("Strain Name:")[1]).split("/")[1]+"/"+(lines.split("Strain Name:")[1]).split("/")[2].split("|")[0]+"\n")
        else:
            clean_file.write(lines)
clean_file.close()