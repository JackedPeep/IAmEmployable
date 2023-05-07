# write your class code above this line
# make no changes below this line
class Genome:
    def __init__(self, sequence):
        self.sequence = ""
        sequence = sequence.upper()
        for i in sequence:
            if i in ["A", "T", "C", "G"]:
                self.sequence += i

    def display(self):

        print(self.sequence)

    def genes(self):  # ATG start codon. ATG, TAG, TAA, or TGA are stop codons.
        i = 0
        g = 0
        while i < len(self.sequence):
            gene = self.sequence[i:i + 3]

            if gene == "ATG":
                i += 3
                g=1
                geneString = ""
                while i < len(self.sequence):
                    geneString += self.sequence[i]
                    gene = self.sequence[i:i + 3]

                    if gene in ["TAG", "TAA", "TGA"]:
                        i += 2
                        if len(geneString) > 3:
                            print(geneString[:-1])

                        break

                    i += 1
            i += 1

        if g==0:
            print("no gene is found")





def main():
    s1 = Genome("..T.aA.DERRfDww..t.wwWWwwGC..")
    s2 = Genome("TTATGTTTTAAGGATGGGGCGTTAGTT")
    s3 = Genome("TGTGTGTATAT")
    s4 = Genome("TTATGTTTAAGGATGGGGCGTTAGTT")

    s1.display()

    print("---")
    s2.display()
    s2.genes()

    print("---")
    s3.display()
    s3.genes()

    print("---")
    s4.display()
    s4.genes()


main()
#               s1
# TAATGC
# ---           s2
# TTATGTTTTAAGGATGGGGCGTTAGTT
# TTT
# GGGCGT
# ---           s3
# TGTGTGTATAT
# no gene is found
# ---           s4
# TTATGTTTAAGGATGGGGCGTTAGTT
# GGGCGT