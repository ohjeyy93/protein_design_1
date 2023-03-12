with open("test.txt", "r") as r1:
    for lines in r1:
        if "Strain" in lines:
            #print(lines.split("(")[1])
            #if len(lines.split("(")[1].split("/")[3])==4:
            #    print((lines.split("(")[1]).split("/")[0],(lines.split("(")[1]).split("/")[1],(lines.split("(")[1]).split("/")[3])
            if len(lines.split("(")[1].split("/")[3])==2 and int(lines.split("(")[1].split("/")[3])<24:
                #print((lines.split("(")[1]).split("/")[0],(lines.split("(")[1]).split("/")[1],str(20)+(lines.split("(")[1]).split("/")[3])
                print((lines.split("(")[1]).split("/")[0]+"/"+(lines.split("(")[1]).split("/")[1]+"/"+(lines.split("(")[1]).split("/")[2]+"/"+str(20)+(lines.split("(")[1]).split("/")[3])
            if len(lines.split("(")[1].split("/")[3])==2 and int(lines.split("(")[1].split("/")[3])>24:
                print((lines.split("(")[1]).split("/")[0]+"/"+(lines.split("(")[1]).split("/")[1]+"/"+(lines.split("(")[1]).split("/")[2]+"/"+str(19)+(lines.split("(")[1]).split("/")[3])
                #print((lines.split("(")[1]).split("/")[0],(lines.split("(")[1]).split("/")[1],str(19)+(lines.split("(")[1]).split("/")[3])
            #if int(lines.split("(")[1].split("/")[3])<24:
            #    print((lines.split("(")[1]).split("/")[0],(lines.split("(")[1]).split("/")[1],str(20)+(lines.split("(")[1]).split("/")[3])