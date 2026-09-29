print("================================")
print("         NUCLEON")
print("   DNA Sequence Analysis Tool")
print("================================")
print("Which operation do you wanna do with a sample DNA?" )
print("1. Analyze DNA")
print("2. Compare DNA sequences")
print("3. Exit")

choice = int(input("What do you want to do? "))
if choice==1:
    source=int(input("Enter 1 for manual input or 2 for text from file= "))
    if source==1:
        dna=input("Enter the DNA sequence=").upper()
    elif source==2:
      file=open("sample.txt","r")
      dna=file.read().strip()
      file.close()
      print("DNA sequence loaded= ",dna)
    else:
      print("Invalid input source.")
    length=len(dna)
    validation=True
    for i in dna:
      if i in "ATGC":
         pass
      else:
        validation=False
    if validation==True:
        print("Valid Sequence")
        A=dna.count("A")
        T=dna.count("T")
        G=dna.count("G")
        C=dna.count("C")
        GC=0
        GC=((G+C)/length)*100
        print(GC)
        
        rev=""   
        for i in dna:
          if i=="A":
           rev=rev+"T"
          elif i=="T":
           rev=rev+"A"
          elif i=="G":
           rev=rev+"C"
          elif i=="C":
           rev=rev+"G"
        print("Reverse Complementary=",rev[::-1])
        
        motif = input("Enter motif=").upper()
        motif_search=dna.find(motif)
        print("Motif search=",motif_search)

        rna=""
        for i in dna:
            if i =="A":
                rna=rna+"U"
            elif i=="T":
                rna=rna+"A"
            elif i=="G":
                rna=rna+"C"
            elif i=="C":
                rna=rna+"G"
        print("RNA =",rna)
        
        protein=""
        codons = {
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine",

    "UCU": "Serine", "UCC": "Serine",
    "UCA": "Serine", "UCG": "Serine",

    "UAU": "Tyrosine", "UAC": "Tyrosine",
    "UAA": "Stop", "UAG": "Stop",

    "UGU": "Cysteine", "UGC": "Cysteine",
    "UGA": "Stop", "UGG": "Tryptophan",

    "CUU": "Leucine", "CUC": "Leucine",
    "CUA": "Leucine", "CUG": "Leucine",

    "CCU": "Proline", "CCC": "Proline",
    "CCA": "Proline", "CCG": "Proline",

    "CAU": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",

    "CGU": "Arginine", "CGC": "Arginine",
    "CGA": "Arginine", "CGG": "Arginine",

    "AUU": "Isoleucine", "AUC": "Isoleucine",
    "AUA": "Isoleucine", "AUG": "Methionine",

    "ACU": "Threonine", "ACC": "Threonine",
    "ACA": "Threonine", "ACG": "Threonine",

    "AAU": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",

    "AGU": "Serine", "AGC": "Serine",
    "AGA": "Arginine", "AGG": "Arginine",

    "GUU": "Valine", "GUC": "Valine",
    "GUA": "Valine", "GUG": "Valine",

    "GCU": "Alanine", "GCC": "Alanine",
    "GCA": "Alanine", "GCG": "Alanine",

    "GAU": "Aspartic acid", "GAC": "Aspartic acid",
    "GAA": "Glutamic acid", "GAG": "Glutamic acid",

    "GGU": "Glycine", "GGC": "Glycine",
    "GGA": "Glycine", "GGG": "Glycine"
}
        for i in range(0,len(rna),3):
            codon=rna[i:i+3]
            if len(codon)==3:
                if (codons[codon])=="Stop":
                    break
                else:
                    protein=protein+(codons[codon])+" "
            else:
                pass
            
        print("The protein is ",protein)

    else:
     print("Invalid Sequence")
    
elif choice==2:
    print("===COMPARISON OF 2 DNA SEQUENCES===")
    dna1=input("Enter the 1st DNA sequence=").upper()
    dna2=input("Enter the 2nd DNA sequence=").upper()
    mutations=0
    if len(dna1)==len(dna2):
     for i in range(len(dna1)):
         if dna1[i]!=dna2[i]:
             print("Position" ,i ,":", dna1[i],"-->" ,dna2[i],"= Mutation")
             mutations=mutations+1
     print("Total no. of mutations=",mutations)
    else:
        print("The sequences must have the same length.")
else:
    print("Invalid Operation")

 

    
                 

