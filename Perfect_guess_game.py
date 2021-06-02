import random      #import for randon no generation

   # Class for checking guesses and returning steps

class checkrandomNo():      
    choice= ["you guessed correct", "go little higher", "go little lower"]
    def __init__(self,num):
        self.no = num
    def check(self):               
        if self.no ==ranNo:
            return 0
        elif self.no <ranNo:
            return 1
        elif self.no >ranNo:
            return 2

#*** main program    

num=None
counter=0
ranNo=random.randint(1,10)
while (num != ranNo):
    num=int(input("Enter your guess from 1 to 10 "))
    userNUM=checkrandomNo(num)
    print(userNUM.choice[userNUM.check()])
    counter = counter+1
print(f"Congrates, you have doen it in {counter} times")

# ****Highscore maintaining in separate file***8
with open("highscore.txt", "r") as f:
    previousHightscore=int(f.read())

if previousHightscore>counter:
    with open("highscore.txt", "w") as f:
        f.write(str(counter))
    print("congratuions, who have made a highscore")

