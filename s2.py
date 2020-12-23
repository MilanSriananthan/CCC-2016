question = int(input())
people = int(input())
Dmoji = input()
Dmoji = Dmoji.split(" ")
Peg = input()
Peg = Peg.split(" ")

def makeNum(seq):
    hold = []
    for i in seq:
        hold.append(int(i))
    return hold

Dmoji = makeNum(Dmoji)
Peg = makeNum(Peg)

def lowest(seq1, seq2):
    teams = []
    total = 0
    seq1.sort()
    seq2.sort()
    for i in range(len(seq1)):
        teams.append([seq1[i], seq2[i]])
    for i in teams:
        total = total + max(i)
    return total

def highest(seq1, seq2):
    teams = []
    total = 0
    seq1.sort()
    seq2.sort()
    for i in range(len(seq1)):
        teams.append([seq1[i], seq2[-i-1]])
    for i in teams:
        total = total + max(i)
    return total

if question == 1:
    print(lowest(Dmoji,Peg))
else:
    print(highest(Dmoji,Peg))