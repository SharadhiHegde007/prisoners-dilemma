total_score_1 = 0
total_score_2 = 0
rounds = int(input("Enter number of rounds you want the game to continue for: "))

def play_rounds(a,b):
    if a=="C" and b=="C":
        score_1 = 1
        score_2 = 1
    elif a=="C" and b=="D":
        score_1 = 0
        score_2 = 3
    elif a=="D" and b=="C":
        score_1 = 3
        score_2 = 0
    elif a=="D" and b=="D":
        score_1 = 2
        score_2 = 2

    return (score_1, score_2)

for i in range (rounds):
    a = str(input("Enter action taken by Prisoner A: "))
    b = str(input("Enter action taken by Prisoner B: "))
    score_1, score_2 = play_rounds(a, b)
    total_score_1 = total_score_1 + score_1
    total_score_2 = total_score_2 + score_2
    print ("Prisoner A gets", score_1)
    print ("Prisoner B gets", score_2)

print ("Final Scores: ")
print ("Prisoner A: ", total_score_1)
print ("Prisoner B: ", total_score_2)
if total_score_1 > total_score_2:
    print ("Prisoner B is the winner!")
elif total_score_2 > total_score_1:
    print ("Prisoner A is the winner!")
else:
    print ("It's a draw!")
           
