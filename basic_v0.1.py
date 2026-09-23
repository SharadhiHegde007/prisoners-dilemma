#This is a tiny game designed to simulate the concept of the Prisoner's Dilemma.
#According to the problem, there are two prisoners - say, P1 and P2 - who are given a choice to reduce their sentence.
#If P1 chooses to confess (or "cooperate") and P2 does the same, they both get a year in prison.
#If one of them "cooperates" and the other does the opposite by choosing "defect", the one who cooperates gets 3 years, while the one who defects gets off free.
#If they both end up choosing to "defect", both get 2 years each.
#Their choices and the subsequent results are displayed in what's called a Payoff Matrix.
#Here, in this simulation of a single game, the user gets to choose what each prisoner does - "C" for cooperate, and "D" for defect.
#The program then displays the payoff matrix and the final result.

a = str(input("Prisoner A's decision: "))
b = str(input("Prisoner B's decision: "))
from tabulate import tabulate
table_data = [
    ["Cooperate", "(-2,-2)", "(-3,0)"],
    ["Defect",    "(0,-3)", "(-2,-2)"]
]
print(tabulate(table_data, headers=["P1 / P2", "Cooperate", "Defect"], tablefmt="grid"))

if a=="C" and b=="C":
    print ("Both get minimum time. This is the optimal solution.")
elif (a=="C" and b=="D") or (a=="D" and b=="C"):
    print ("One cooperates and one defects. This harms the cooperative partner disproportionately.")
else:
    print ("Both refuse to cooperate. This leads to a fair resolution, but not the optimal one.")