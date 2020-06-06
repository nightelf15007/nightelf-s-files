# the translate function
def translate(dna):
    file ="DNAFile.txt"
    f = open(file, "r")
    dna = f.read()
    dna = dna.replace("\n", "")
    dna = dna.replace("\r", "")

    #initialize variables
    protein = ""
    # if dna is not devisible by 3, discard the extra nucleotides
    if len(dna)%3 == 2:
        print("The DNA code that you have entered has 2 extra nucleotides. Please check the sequence. We will be translating by dicarding the last 2 necleotides ")
        dna = dna[:-2] # remove last 2 nuclieotides
    elif len(dna)%3 ==1:
        print("The DNA code that you have entered has an extra nucleotide. Please check the sequence. We will be translating by dicarding the last necleotide ")
        dna = dna[:-1] # remove last nuclieotide
    #Create a tabel containing all the codons and possible amino acids (mindblowing, I know. There's a reason for doing this at 11pm)
    table = {"ATA":"I", "ATC":"I", "ATT":"I", # amin acid I's corrosponding codons
             "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L", "TTA":"L", "TTG":"L", # amin acid L's corrosponding codons
             "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V", # amin acid V's corrosponding codons
             "TTC":"F", "TTT":"F", # amin acid F's corrosponding codons
             "ATG":"M"} # amin acid M's corrosponding codons
    #compare codons with amino acids in the tabel and add correct amino acid to the protein
    for i in range(0, len(dna), 3):
        codon = dna[i:i + 3]
        if codon not in table: # if codon is not one of the 5, add X to protein
            protein += "X"
        else:
            protein += table[codon]
    print(protein) #for error catching purpose
    return protein
    
# the mutate function
def mutate():
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
            print(a) #error catching purposes (to be be commented out)
            break #stop after first "a
    #open DNAFile.txt to write from
    with open("DNAFile.txt", "rt") as f:
        #open normalDNA.txt to write to (create if nonex)
        with open("normalDNA.txt", "wt") as fn:
            for line in f: #while not Eof
                fn.write(line.replace("a", "A"))# I'm out of ideas
    with open("DNAFile.txt", "rt") as f:    
                #open normalDNA.txt to write to (create if nonex)
        with open("mutatedDNA.txt", "wt") as fm:
            for line in f: #while not Eof
                fm.write(line.replace("a", "T"))# It actually works XD

# txtTranslate function
def txtTranslate():
    mutate() #have to mutate to ensure the files are right
    file ="normalDNA.txt"
    f = open(file, "r")
    normalDNAF = f.read()
    normalDNAF = normalDNAF.replace("\n", "")
    normalDNAF = normalDNAF.replace("\r", "")
    normalDNA = translate(normalDNAF) #translate the file
    
    file1 ="normalDNA.txt"
    ff = open(file1, "r") 
    mutatedDNAF = ff.read()
    mutatedDNAF = mutatedDNAF.replace("\n", "")
    mutatedDNAF = mutatedDNAF.replace("\r", "")
    mutatedDNA = translate(mutatedDNAF) #translate the file   
    mutatedDNA = translate(ff)
    print("Normal DNA: " + normalDNA) #print the normal dna
    print("Mutated DNA: " + mutatedDNA) #porint the mutated dna
    
txtTranslate()