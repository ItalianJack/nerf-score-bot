import os

from discord import player

def generateScoreSheet(guildID,players):                # guildID passed as int, float, or str; players is list of str for player names
    dest = open(str(guildID)+'_scores.txt','w')         # Create new or overwrite old score sheet file for given guild
    for entry in players:                               # For every entry in list "players", create entry in file with format "name\n0\n0"
        dest.write(players[players.index(entry)]+'\n') 
        dest.write('0\n')
        dest.write('0\n')
    dest.close()

def importScores(score_file):                           # score_file is file containing scores
    inputFile = open(score_file,'r')                    # import score file
    players = {}
    for line in inputFile:                              # for every line in the score file, create and fill a dict entry
        playerName = line.rstrip()
        kills = int(inputFile.readline().rstrip())
        deaths = int(inputFile.readline().rstrip())
        players[playerName]=[kills,deaths]
    inputFile.close()
    return players                                      # return the dict

def modifyScores(file,targetPlayer,killOrDeath,change): 
    source = open(file,'r')
    tempDest = open('tempscores.txt','w')
    for line in source:
        name = line.rstrip()
        kills = int(source.readline().rstrip())
        deaths = int(source.readline().rstrip())
        if name == targetPlayer:
            if killOrDeath == 'kill':
                kills += change
            elif killOrDeath == 'death':
                deaths += change
        tempDest.write(name + '\n')
        tempDest.write(str(kills) + '\n')
        tempDest.write(str(deaths) + '\n')
    source.close()
    tempDest.close()
    os.remove(file)
    os.rename('tempscores.txt',file)

def sortPlace(playerData):
    print(sorted(playerData.items(), key=lambda i:i[0]))
    print(sorted(playerData.items(), key=lambda i:i[1]))
    return sorted(playerData.items(), key=lambda i:i[0])

    
        