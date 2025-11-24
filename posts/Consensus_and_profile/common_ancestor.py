with open("C:/Users/reino/OneDrive/Desktop/Portfolio2/posts/Consensus_and_profile/data.txt") as new_file:
    sequences = {}
    current_label = None
    for line in new_file:
        line = line.strip()
        if line.startswith('>'):
            current_label = line[1:] 
            sequences[current_label] = ''
        else:
            sequences[current_label] += line
dic = {"A":0, "G":0, "T":0, "C": 0}
sequence_L = []
consensus = []
for key, value in sequences.items():
    sequence_L.append(value)
print(sequence_L)

for base in sequence_L:
    if base == 