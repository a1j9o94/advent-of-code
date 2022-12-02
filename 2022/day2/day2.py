

def getScoreResult(game):
    pickArray = [*game]
    theirEncryptedSelection = pickArray[0]
    myEncryptedSelection = pickArray[2]

    theirDecodedSelection = decode(theirEncryptedSelection, "t")
    myDecodedSelection = decode(myEncryptedSelection, "m")

    resultScore = getResultScore(theirDecodedSelection, myDecodedSelection)

    selectionScore = getSelectionScore(myDecodedSelection)

    return resultScore + selectionScore

def getSelectionScore(selection):
    if selection == "rock":
        return 1
    if selection == "paper":
        return 2
    if selection == "scissors":
        return 3

def getResultScore(theirSelection, mySelection):
    if theirSelection == "rock":
        if mySelection == "rock":
            return 3
        if mySelection == "paper":
            return 6
        if mySelection == "scissors":
            return 0
    if theirSelection == "paper":
        if mySelection == "rock":
            return 0
        if mySelection == "paper":
            return 3
        if mySelection == "scissors":
            return 6
    if theirSelection == "scissors":
        if mySelection == "rock":
            return 6
        if mySelection == "paper":
            return 0
        if mySelection == "scissors":
            return 3

def decode(selection, player):
    if player == "t":
        if selection == "A":
            return "rock"
        if selection == "B":
            return "paper"
        if selection == "C":
            return "scissors"
    if player == "m":
        if selection == "X":
            return "rock"
        if selection == "Y":
            return "paper"
        if selection == "Z":
            return "scissors"


if __name__ == '__main__':
    data_file = open('day2.txt', 'r')
    raw_rps_data = data_file.readlines()
    my_total_score = 0
    for game in raw_rps_data:
        my_total_score += getScoreResult(game.strip())

    print("My total Score: " + str(my_total_score))
