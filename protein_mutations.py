with open("h3cut.rmdl_0040.ddg.txt", "r") as r1:
    current_item=""
    current_score=0
    full_list=[]
    full_list_record=[]
    current_lines=""
    for lines in r1:
        if "ResID" not in lines:
            if 130 <= int(lines.split(" ")[2]) <=170:
                if float(lines.split("  ")[1])>0:
                    #print(lines)
                    if current_item!=lines.split(" ")[2]:
                        #print(current_item,current_score)
                        if current_lines not in full_list:
                        #print(current_lines)
                            if current_lines!="":
                                full_list+=[current_lines.strip("\n")]
                        current_item=lines.split(" ")[2]
                        current_score=float(lines.split("  ")[1])
                        current_lines=lines
                    if current_item==lines.split(" ")[2]:
                        #print(current_score)
                        #print(current_score)
                        #print(lines.split("  ")[1])
                        if current_score<float(lines.split("  ")[1]):
                            #print(lines)
                            current_score=float(lines.split("  ")[1])
                            current_lines=lines
    #print(list(set(full_list)))
    #print(full_list)
    #current_test=""
with open("original.fasta", "r") as r2:
    count=0
    lines_a=""
    lines_b=""
    lines_c=""
    for lines in r2:
        if "0040_A" in lines:
            count=0
        if count==0 and ">" not in lines:
            lines_a+=lines.strip("\n")
                #count+=1
        if "0040_B" in lines:
            count=1
        if count==1 and ">" not in lines:
            lines_b+=lines.strip("\n")
        if "0040_C" in lines:
            count=2
        if count==2 and ">" not in lines:
            lines_c+=lines.strip("\n")
    #print(lines_c)
    list_A=[]
    list_B=[]
    list_C=[]
    
    for item in list(set(full_list)):
        if item.startswith("C"):
            lines_c=lines_c[0:int(item.split(" ")[2])-1]+(item.split(" ")[3])+lines_c[int(item.split(" ")[2])::]
            list_C+=[item.split(" ")[2]]
        if item.startswith("B"):
            lines_b=lines_b[0:int(item.split(" ")[2])-1]+(item.split(" ")[3])+lines_b[int(item.split(" ")[2])::]
            list_B+=[item.split(" ")[2]]
        if item.startswith("A"):
            lines_a=lines_a[0:int(item.split(" ")[2])-1]+(item.split(" ")[3])+lines_a[int(item.split(" ")[2])::]
            list_A+=[item.split(" ")[2]]
    print(lines_a)
    print(lines_b)
    print(lines_c)
    
    #print(list_C)   
            
            #lines_c[0:int(item.split(" ")[2])-1]+(item.split(" ")[4])+lines_c[int(item.split(" ")[2])::]
            #print(lines_c[0:int(item.split(" ")[2])-1]+(item.split(" ")[3])+lines_c[int(item.split(" ")[2])::])

    #print(lines_c)
        #if item.startswith("A"):
        #    print(item)
        #if item.startswith("B"):
        #    print(item)
             
    #for item in list(set(full_list)):
    #    for lines in r2:
    #        print(item)
    #    if "168" in item:
    #        print(item)
    #        print(len(item))
            #current_test=item
        

                    #print(lines.split(" ")[0]+" "+lines.split(" ")[2]) 
                    #print(lines.split("  ")[1])
                        