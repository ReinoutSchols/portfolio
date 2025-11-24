

with open("C:/Users/reino/OneDrive/Desktop/Portfolio2/posts/Motif_DNA/rosalind_subs.txt") as new_file:
    DNA = new_file.readline().strip()
    motif = new_file.readline().strip()

def find_all_occurrences(string, sub):
    index_of_occurrences = []
    current_index = 0
    while True:
        current_index = string.find(sub, current_index)
        #print(current_index)
        if current_index == -1:
            return index_of_occurrences
        else:
            index_of_occurrences.append(current_index+1)
            current_index += 1

print(find_all_occurrences(DNA, motif))