#import the library
import importlib
moduleName = input('DNAFile.txt') #assign variable
importlib.import_module(moduleName) #moduleName into the libmod

file ="DNAFile.txt" #store content in file
f = open(file, "r") #read file
DNA = f.read() #store content of f
DNA = DNA.replace("\n", "")  
DNA = DNA.replace("\r", "") 
#translate function
def translate(DNA):
    #initialize variables
    protein = ""
    # if dna is not devisible by 3, discard the extra nucleotides
    if len(DNA)%3 == 2:
        print("The DNA code that you have entered has 2 extra nucleotides. Please check the sequence. We will be translating by dicarding the last 2 necleotides ")
        DNA = DNA[:-2] # remove last 2 nuclieotides
    elif len(DNA)%3 ==1:
        print("The DNA code that you have entered has an extra nucleotide. Please check the sequence. We will be translating by dicarding the last necleotide ")
        DNA = DNA[:-1] # remove last nuclieotide
    #Create a tabel containing all the codons and possible amino acids (Mindblowing, I know. There's a reason for doing this at 11pm XD)
    table = {"ATA":"I", "ATC":"I", "ATT":"I",
             "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L", "TTA":"L", "TTG":"L",
             "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
             "TTC":"F", "TTT":"F",
             "ATG":"M"}
    #compare codons with amino acids in the tabel and add correct amino acid to the protein
    for i in range(0, len(DNA), 3):
            codon = DNA[i:i + 3]
            if codon not in table:
                protein += "X" # if codon is not one of the 5, add X to protein
            else: 
                protein += table[codon] #add corresponding amino acid from table to protein
    #print (protein) #for error catching purpose
    return protein


# the mutate function
def mutate(DNA):
    #open the text file called DNA.txt
    DNA = open('DNAFile.txt', 'r')
    #initialize variables
    count = 0
    s = "letters"
    a = 0
    while s != "": #while not EoF
        s = DNA.readline() #read line by line
        s = s.strip()
        count += 1 #count the lines
        if s == "a": #if the line contains "a"
            a  = count
            #print(a) #error catching purposes
            break #stop after first "a
    #open DNAFile.txt to write from     
    with open("DNAFile.txt", "rt") as f:
        #open normalDNA.txt to write to (create if nonex)
        with open("normalDNA.txt", "wt") as fn:
            for line in f: #while not Eof
                fn.write(line.replace("a", "A"))# I'm out of ideas       
    #open DNAFile.txt to write from     
    with open("DNAFile.txt", "rt") as f:
        #open normalDNA.txt to write to (create if nonex)
        with open("mutatedDNA.txt", "wt") as fm:
            for line in f: #while not Eof
                fm.write(line.replace("a", "T"))# It actually works XD
    return

# txtTranslate function
def txtTranslate():
    with open("normalDNA.txt", "r") as fn:
        ndna = fn.read() #store content of fn
        translate(ndna) #just translate the new dna -_-
    with open("mutatedDNA.txt", "r") as fm:
        mdna = fn.read() #store content of fn
        translate(mdna) #just translate the new dna -_-
    

#I don't know what I'm doing anymore 8(