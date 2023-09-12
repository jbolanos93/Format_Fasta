"""
This script will format nucleotide bases to be the same length of string. 

Example: 

>Seq1
ATGGG
GGGGG
ATTGT
>Seq2
ATGAGAGAGAAG
ATGAGAGAGAAG
ATGAGAGAGAAG

output will be: 
>Seq1
ATGGGGGG
GGGGGGGG
ATTGTGAA
>Seq2
ATGAGAGA
GAAGATGA
GAGAGAAG
ATGAGAGA
GAAG

"""
import random
import sys

def FormatLine(aString:str,string_length:int)-> None:
    
    Starting_string=aString.strip("\n")
    #print(f"Starting String Length is f{len(Starting_string)}")
    #print(f"\n\nStarting String is {Starting_string}\n\n")
    
    FinalString=""
    count=0
    
    #print(f" starting string len {len(Starting_string)} > desired : {string_length}")
    #return
    
    #if len(Starting_string) > string_length:
        
    for i in Starting_string:
        
        FinalString+=i
        count+=1
        
        if count % string_length ==0:
            FinalString+="\n"
            count=0
    
    #print(f"\n\nFinal String {FinalString}")
    finallyis=FinalString.replace("\n","")
    #print(f"Final String Length is {len(finallyis)}")
    return FinalString

def printingFormat(length_of_nucleotide):
    print(f"Formatting new Fasta to format\n\n>SequenceHeader")
    for i in range(0,10):
        bases=["A","T","G","C"]
        base=random.choice(bases)
        print(base*length_of_nucleotide)
    print("<",end="")
    print("-" * (length_of_nucleotide -2),end="")
    print(">")
    print(" " *((length_of_nucleotide//2) -7),end="")
    print(f"Length {length_of_nucleotide}")
    print("<",end="")
    print("-" * (length_of_nucleotide -2),end="")
    print(">\n")

def format_fasta(PathToFasta:str,length_of_nucleotide:int) -> None: 
    isHeader=None
    isSequence=None
    
    #used to indicate first pass of fasta string/header
    First=True
    
    #Set file name
    name=PathToFasta.split("/")
    name=name[len(name)-1]
    original=name
    name=f"NewFormat_"+name
    new_file_name=PathToFasta.replace(original,name)
    
    print(f"Reading file: {PathToFasta}")
    print(f"Saving new  file as: {new_file_name}")
    
    # write file 
    with open (new_file_name,"w+") as new_file:
        
        #read file
        with open (PathToFasta,"r") as f:
            
            file=f.readlines()
            
            StringBuilder=""
            
            for line in file:
                if line.startswith(">") and First:
                    
                    #Print BS
                    length_of_nucleotide=int(length_of_nucleotide)
                    printingFormat(length_of_nucleotide)
                    
                    
                    
                    new_file.write(line)
                    First=False
                    continue
                
                elif line.startswith(">"):
                    #print(f"String receiving is: {StringBuilder}")
                    nuc_line=FormatLine(StringBuilder,length_of_nucleotide)
                    new_file.write(f"{nuc_line}\n")
                    new_file.write(line)
                    StringBuilder=""
                    #break
                
                else:
                    StringBuilder+=line.strip("\n")

        nuc_line=FormatLine(StringBuilder,length_of_nucleotide)
        new_file.write(f"{nuc_line}\n")
    
    print(f"Done")
    
    return
def check_file_ext(filename:str)-> bool:
    if filename.endswith(".fasta") or filename.endswith(".FASTA") or filename.endswith(".fa"):
        return True
    else: return False
    
    
    
    

def how_to_use(error:int, data:str)-> None:
    if error ==1:
        print(f"To use script:\n\nRun as follows:\n\npython Format_Fasta.py <Path to Fasta> <Length of Sequence>\n\nWhere <Path to Fasta> is the path to the fasta file you want to format. (extension of the file should be .fa .fasta .FASTA)\n<Length of Sequence> is an integer determining how many bases to have per squence.\n\nExapmle: python Format_Fasta.py /Users/Foo/Desktop/Fasta_file.fasta 35")
    elif error ==2:
        print(f"To use script:\n\nRun as follows:\n\npython Format_Fasta.py <Path to Fasta> <Length of Sequence>\n\nWhere <Path to Fasta> is the path to the fasta file you want to format. (extension of the file should be .fa .fasta .FASTA)\n<Length of Sequence> is an integer determining how many bases to have per squence.\n\nExapmle: python Format_Fasta.py <Path to Fasta>  {data}")
    elif error ==3:
        print(f"To use script:\n\nRun as follows:\n\npython Format_Fasta.py <Path to Fasta> <Length of Sequence>\n\nWhere <Path to Fasta> is the path to the fasta file you want to format. (extension of the file should be .fa .fasta .FASTA)\n<Length of Sequence> is an integer determining how many bases to have per squence.\n\nExapmle: python Format_Fasta.py {data} <Length of Sequence> ")
    elif error ==3:
        print(f"Make sure to use a string paramater for <Path to fasta> and integer only for length of sequence.")

def check_args():
    if len(sys.argv)==1:
        print("Arguments not entered properly.")
        how_to_use(1,"")
        sys.exit()
    
    elif len(sys.argv)==2:
        print("Missing an Argument!")
        
        
        try:
           seq_length=int(sys.argv[1])
           print("Missing File Path Argument!")
           how_to_use(2,seq_length)
           
        except:
           print("Missing Sequence length Argument!")
           file_path=(sys.argv[1])
           how_to_use(3,file_path)
           sys.exit()
        
        
            
    elif len(sys.argv)==3:
        if check_file_ext(sys.argv[1]):
            try:
                length=int(sys.argv[2])
                print("Arguments okay. Running Script.")
                
            except: 
                how_to_use(1,"")
                sys.exit()
            
        elif check_file_ext(sys.argv[2]):
            print("fasta file used in second argument position!\nRun Again  and follow the formats below.\n")
            how_to_use(1,"")
            sys.exit()
            
        
        
        elif not sys.argv[1].endswith(".fasta") and not sys.argv[2].endswith(".fasta"):
            print("Makse sure you are using a fasta file.")
            how_to_use(1,"")
            sys.exit()
            
        print("Arguments okay. Running Script.")
    
    elif len(sys.argv)>3:
        print("Too many arguments!")
        how_to_use(1,"")
        sys.exit()
        
            
            
        
        #how_to_use()
        #sys.exit()


def main():
    #checking arguments
    check_args()
    
    #Running Script.
    file=sys.argv[1] 
    sequence_length=sys.argv[2]
    
    format_fasta(file,sequence_length)
    
    
    return



if __name__ == "__main__":
    main()