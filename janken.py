import random
def letsPlay(text):
        u = len(text)
        choiceOfBot = random.choice(["rock", "paper", "scissors"])
        d = len(choiceOfBot)
        if (u==4 and d==8) or (u==5 and d==4) or (u==8 and d==5):
            return f"{choiceOfBot} You won this time, but next time!\nNext time ill win"
        elif (u==d):
            return f"{choiceOfBot}, Its a tie, again"
        else:
            return f"{choiceOfBot}, Yes......YEs.....YES....YES!!, i win wooooh"