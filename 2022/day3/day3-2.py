
//The second example
if __name__ == '__main__':
    data_file = open('day3Data.txt', 'r')
    raw_rucksack_data = data_file.readlines()
    chunks = 3
    lineGroups = [[x.strip() for x in raw_rucksack_data[i:i+chunks]] for i in range(0,len(raw_rucksack_data),chunks)]
    common_elements = [[element for element in x[0]
                        if element in x[1] and element in x[2]][0:1] for x in lineGroups]
    lettersList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
                   "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    scores = [[lettersList.index(element[0])+1 if len(element) > 0 else 0]
              for element in common_elements]

    print(lineGroups)
    print(common_elements)
    print(scores)

    flatScores = [item for sublist in scores for item in sublist]
    print(len(flatScores))
    print(sum(flatScores))