with open("C:/Users/reino/Downloads/rosalind_iprb.txt") as new_file:
    #Read in file and split the numbers, than transform them into #floats. 
    numbers = new_file.read().split()
    L = [float(i) for i in numbers]

G = L[0]
B = L[1]
D = L[2]

def dominant_probability(G, B, D):
    total = G + B + D
    # Calculate P(No A) when two Belgians are mingling:
    P_heterozygote = (B / total) * ((B - 1) / (total - 1)) * 0.25

    # Calculate P(No A) when two Dutchies are mingling:
    P_recessive = (D / total) * ((D - 1) / (total - 1)) * 1

    # Calculate P(No A) when A Belgian and a Dutch are mingling:
    P_hetero_recessive = ((B / total) * (D / (total - 1)) + (D / total) * (B / (total - 1))) * 0.5

    #Calculate probability of having no A (summing them):
    P_No_A = P_heterozygote + P_recessive + P_hetero_recessive

    # Calculate the Probability of having a dominant allel
    P_A = 1 - P_No_A
    print(round(P_A, 5))

dominant_probability(G, B, D)