import pandas as pd
import numpy as np
import itertools
import datetime


class Player:
    """
    Class for each player.  Easy way to get player points and salary

    """
    def __init__(self, playerName, position, points, salary):

        self.playerName = playerName
        self.position = position
        self.points = points
        self.salary = salary

    def getName(self):
        return self.playerName

    def getPosition(self):
        return self.position

    def getPoints(self):
        return self.points

    def getSalary(self):
        return self.salary


def lineupScore(lineup, memo):
    """
    Lineup: an array containing names of players in the lineup
    memo: a dictionary with:
        keys: lineup arrays
        values: dictionary with:
            keys: 
                Score: sum of fantasy points
                Cost: sum of salaries


    """
    if lineup in memo.keys():
        return memo[lineup]['Score'], memo[lineup]['Cost']
    if len(lineup) == 1:
        memo[lineup] = {}
        memo[lineup]['Score'] = list(lineup)[0].getPoints()
        memo[lineup]['Cost'] = list(lineup)[0].getSalary()
        return memo[lineup]['Score'], memo[lineup]['Cost']
    lineupList = list(lineup)
    first = lineupList[:1]
    rest = lineupList[1:]
    firstScore = lineupScore(tuple(first), memo)
    restScore = lineupScore(tuple(rest), memo)
    memo[tuple(rest)] = {}
    memo[tuple(rest)]['Score'] = restScore[0]
    memo[tuple(rest)]['Cost'] = restScore[1]
    return firstScore[0] + restScore[0], firstScore[1] + restScore[1]

def prune(players):
    pruned = []
    for i in players:
        isValid = True
        for j in players:
            if i != j:
                if (i.getSalary() >= j.getSalary()) and (i.getPoints() < j.getPoints()):
                    isValid = False
        if isValid:
            pruned.append(i)
    return pruned

def pruneGroup(group):
    a = list(group)
    pruned = []
    pruneDict = {}
    for i in a:
        cost = sum(x.getSalary() for x in i)
        points = sum(x.getPoints() for x in i)
        if cost not in pruneDict.keys():
            pruneDict[cost] = i
        if points > sum(x.getPoints() for x in pruneDict[cost]):
            pruneDict[cost] = i
    for key1 in pruneDict.keys():
        isValid = True
        for key2 in pruneDict.keys():
            if key1 != key2:
                if (key1 >= key2) and (sum([x.getPoints() for x in pruneDict[key1]]) < sum([x.getPoints() for x in pruneDict[key2]])):
                    isValid = False
        if isValid:
            pruned.append(pruneDict[key1])
    return pruned


def getBestLineup(QB, RB, WR, TE, FLEX, DEF):
    bestScore = 0
    bestLineup = None
    salaryCap = 50000
    lineupDict = {}
    for qb in QB:
        print qb.getName()
        for rb in RB:
            print [x.getName() for x in list(rb)]
            for wr in WR:
                for te in TE:
                    for flex in FLEX:
                        if (flex not in rb) and (flex not in wr) and (flex != te):
                            for defense in DEF:
                                lineup = tuple(sorted([qb] + list(rb) + list(wr) + [te, flex, defense]))
                                #lineupAnalysis = lineupScore(lineup, lineupDict)
                                score = sum(x.getPoints() for x in list(lineup))
                                cost = sum(x.getSalary() for x in list(lineup))
                                if cost <= salaryCap:
                                    if score > bestScore:
                                        bestScore = score
                                        bestLineup = lineup

    bestLineupNames = []
    for player in list(bestLineup):
        bestLineupNames.append(player.getName())
    return bestLineupNames, bestScore


if __name__ == '__main__':
    startTime = datetime.datetime.now()
    QB = []
    RB = []
    WR = []
    TE = []
    FLEX = []
    DEF = []
    qbfile = pd.read_excel('DKpositions.xlsx', sheetname="DK QB")
    rbfile = pd.read_excel('DKpositions.xlsx', sheetname="DK RB")
    wrfile = pd.read_excel('DKpositions.xlsx', sheetname="DK WR")
    tefile = pd.read_excel('DKpositions.xlsx', sheetname="DK TE")
    deffile = pd.read_excel('DKpositions.xlsx', sheetname="DK DEF")
    for index, row in qbfile.iterrows():
        x = Player(row['Player'], 'QB', row['FP'], row['Cost'])
        QB.append(x)
    for index, row in rbfile.iterrows():
        x = Player(row['Player'], 'RB', row['FP'], row['Cost'])
        RB.append(x)
        FLEX.append(x)
    for index, row in wrfile.iterrows():
        x = Player(row['Player'], 'WR', row['FP'], row['Cost'])
        WR.append(x)
        FLEX.append(x)
    for index, row in tefile.iterrows():
        x = Player(row['Player'], 'TE', row['FP'], row['Cost'])
        TE.append(x)
        FLEX.append(x)
    for index, row in deffile.iterrows():
        x = Player(row['Player'], 'Def', row['FP'], row['Cost'])
        DEF.append(x)
    WR = itertools.combinations(WR, 3)
    RB = itertools.combinations(RB, 2)
    QB  = prune(QB)
    RB = pruneGroup(RB)
    WR = pruneGroup(WR)
    TE = prune(TE)
    FLEX = prune(FLEX)
    DEF = prune(DEF)
    print len(QB), len(RB), len(WR), len(TE), len(FLEX), len(DEF)
    print getBestLineup(QB, RB, WR, TE, FLEX, DEF)
    endTime = datetime.datetime.now()
    print endTime - startTime







