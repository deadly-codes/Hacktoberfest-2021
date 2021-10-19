import random

def choose():
    words = ["rainbow","science","computer","programming","mathematics","player","condition","reverse","water","board"]
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled = "".join(random.sample(word,len(word)))
    return jumbled


def thank(p1n,p2n,p1,p2):
    print(p1n,"Your score is = ",p1)
    print(p2n,"Your score is = ",p2)
    print("Thank's for playing")
    print("Have a nice day")        

def play():

    p1name = input("Player1, Enter your name = ")
    p2name = input("Player2, Enter your name = ")
    pp1 = 0
    pp2 = 0
    turn = 0
    while(1):
        #Computer's Task
        picked_word = choose()
        #Create the question
        qn = jumble(picked_word)
        print(qn)
        # Player1
        if turn%2==0:
            print(p1name,"Your turn.")
            ans = input("What's on my mind? = ")
            if ans==picked_word:
                pp1 = pp1+1
                print("YOur score is = ",pp1)
                turn = turn+1
            else:
                print("Better luck next time. I though = ",picked_word)
            c = input("Press 1 to continue and 0 to quit = ")
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        # Player2
        else:
            print(p1name,"Your turn.")
            ans = input("What's on my mind?")
            if ans==picked_word:
                pp2 = pp2+1
                print("YOur score is = ",pp2)
            else:
                print("Better luck next time. I though = ",picked_word)
            c = input("Press 1 to continue and 0 to quit = ")
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn = turn+1    

# Driver code 
if __name__ == '__main__': 
      
    # play() function calling 

    play()
