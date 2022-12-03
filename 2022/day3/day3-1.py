

if __name__ == '__main__':
    data_file = open('day3Data.txt', 'r')
    raw_rucksack_data = data_file.readlines()

    totalScore = 0;
    for line in raw_rucksack_data:
        line = line.strip()
        halfPoint = int((len(line)/2))
        halves = [[line[0:halfPoint],line[halfPoint:int(len(line))]]]
        common_elements = [[element for element in x[0]
                            if element in x[1]][0:1] for x in halves]
        lettersList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
                       "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        scores = [[lettersList.index(element[0])+1 if len(element)>0 else 0] for element in common_elements]
        totalScore += scores[0][0]

        print(halves)
        print(common_elements)
        print(scores)

    print(totalScore)