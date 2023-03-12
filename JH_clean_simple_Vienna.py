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
                clean_file.write(">"+lines.split("Strain Name:")[1].split("|")[0][0:-2]+"19"+lines.split("Strain Name:")[1].split("|")[0][-2::]+"\n")
            if len(lines.split("Strain Name:")[1].split("|")[0].split("/")[-1])==2 and int(lines.split("Strain Name:")[1].split("|")[0].split("/")[-1])<24: 
                clean_file.write(">"+lines.split("Strain Name:")[1].split("|")[0][0:-2]+"20"+lines.split("Strain Name:")[1].split("|")[0][-2::]+"\n")
            if len(lines.split("Strain Name:")[1].split("|")[0].split("/")[-1])==3: 
                #print(lines)
                if "Vienna" not in lines:
                    if int(lines.split("Strain Name:")[1].split("|")[0].split("/")[-2])>24:
                    #print(lines.split("Strain Name:")[1].split("|")[0][0:-2])
                        #print(">"+lines.split("Strain Name:")[1].split("|")[0][0:-5]+"20"+lines.split("Strain Name:")[1].split("|")[0][-5:-3]+"\n")
                        #print(">"+lines.split("Strain Name:")[1].split("|")[0][0:-6]+"20"+lines.split("Strain Name:")[1].split("|")[0][-6:-4]+"\n")
                        clean_file.write(">"+lines.split("Strain Name:")[1].split("|")[0][0:-6]+"19"+lines.split("Strain Name:")[1].split("|")[0][-6:-4]+"\n")
                    if int(lines.split("Strain Name:")[1].split("|")[0].split("/")[-2])<24: 
                        #print(">"+lines.split("Strain Name:")[1].split("|")[0][0:-5]+"20"+lines.split("Strain Name:")[1].split("|")[0][-5:-3]+"\n")
                        #print(">"+lines.split("Strain Name:")[1].split("|")[0][0:-6]+"20"+lines.split("Strain Name:")[1].split("|")[0][-6:-4]+"\n")
                        clean_file.write(">"+lines.split("Strain Name:")[1].split("|")[0][0:-6]+"20"+lines.split("Strain Name:")[1].split("|")[0][-6:-4]+"\n")
                    #clean_file.write(">"+lines.split("Strain Name:")[1].split("|")[0]+"\n")
                if "Vienna" in lines:
                    #print(">"+lines.split("Strain Name:")[1].split("|")[0][0:-3]+"20"+lines.split("Strain Name:")[1].split("|")[0][-3:-1]+"\n")
                    #print(lines.split("Strain Name:")[1].split("|")[0].split("/")[-1][0:-1])
                    if int(lines.split("Strain Name:")[1].split("|")[0].split("/")[-1][0:-1])>24:
                    #print(lines.split("Strain Name:")[1].split("|")[0][0:-2])
                        #print(">"+lines.split("Strain Name:")[1].split("|")[0][0:-5]+"20"+lines.split("Strain Name:")[1].split("|")[0][-5:-3]+"\n")
                        #print(">"+lines.split("Strain Name:")[1].split("|")[0][0:-6]+"20"+lines.split("Strain Name:")[1].split("|")[0][-6:-4]+"\n")
                        #print(">"+lines.split("Strain Name:")[1].split("|")[0][0:-3]+"19"+lines.split("Strain Name:")[1].split("|")[0][-3:-1]+"\n")
                        clean_file.write(">"+lines.split("Strain Name:")[1].split("|")[0][0:-3]+"19"+lines.split("Strain Name:")[1].split("|")[0][-3:-1]+"\n")
                    if int(lines.split("Strain Name:")[1].split("|")[0].split("/")[-1][0:-1])<24: 
                        #print(">"+lines.split("Strain Name:")[1].split("|")[0][0:-5]+"20"+lines.split("Strain Name:")[1].split("|")[0][-5:-3]+"\n")
                        #print(">"+lines.split("Strain Name:")[1].split("|")[0][0:-6]+"20"+lines.split("Strain Name:")[1].split("|")[0][-6:-4]+"\n")
                        #print(">"+lines.split("Strain Name:")[1].split("|")[0][0:-3]+"20"+lines.split("Strain Name:")[1].split("|")[0][-3:-1]+"\n")
                        clean_file.write(">"+lines.split("Strain Name:")[1].split("|")[0][0:-3]+"20"+lines.split("Strain Name:")[1].split("|")[0][-3:-1]+"\n")
                    #clean_file.write(">"+lines.split("Strain Name:")[1].split("|")[0]+"\n")
            if len(lines.split("Strain Name:")[1].split("|")[0].split("/")[-1])==4:
                #print(lines.split("Strain Name:")[1].split("|")[0])
                clean_file.write(">"+lines.split("Strain Name:")[1].split("|")[0]+"\n")
            if len(lines.split("Strain Name:")[1].split("|")[0].split("/")[-1])>4:
                #print(">"+lines.split("Influenza A virus (")[1].split("(H3N2)")[0]+"\n")
                #print(lines)
                if "Wisconsin" in lines:
                    clean_file.write(">"+lines.split("Influenza A virus (")[1].split("(H3N2)")[0].split("X")[0][0:-3]+"20"+lines.split("Influenza A virus (")[1].split("(H3N2)")[0].split("X")[0][-3::]+"\n") 
                if "Nepal" in lines:
                    #print(">"+lines.split("Influenza A virus (")[1].split("(H3N2)")[0].split("X")[0]+"\n")
                    clean_file.write(">"+lines.split("Influenza A virus (")[1].split("(H3N2)")[0].split("X")[0].strip()+"\n") 
                if "Wisconsin" not in lines and "Nepal" not in lines:
                    #print(lines)
                    clean_file.write(">"+lines.split("Influenza A virus (")[1].split("(H3N2)")[0]+"\n")
            #print(lines.split("Strain Name:")[1].split("|")[0])
            #print(lines.split("Strain Name:")[1].split("|")[0].split("/")[-1])
        else:
            clean_file.write(lines)
clean_file.close()