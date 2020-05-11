import time
from playsound import playsound

timeLeft = 0
mins = 0
pomo_finished = 0



def startPomodoro():
    
    timeLeft = 25
    mins = 0

    print("Starting Pomodoro")
    while timeLeft != mins:
        time.sleep(60)
        timeLeft -= 1
    print("Pomodoro Finished") 
    startBreak()
    

def startBreak():
    timeLeft = 5
    mins = 0

    print("starting Short Break")
    while timeLeft != mins:
        time.sleep(60)
        timeLeft -= 1
    print("Short Break Finished")
    

 

def askAdmin():
    print("welcome you useless looser! want motivation to get things done..")
    print("Well too bad, aint gonna help")
    print("(type 'y' if you want to secretly start the timer 'n' if you dont)")

askAdmin()
user_choice = input()
while user_choice == 'y':
    target_pomodoros = 3 
    while pomo_finished != target_pomodoros:
        playsound('assets/doit.mp3')
        startPomodoro()
        playsound('assets/woho.mp3')
        print("1 Pomodoro Finished")
        pomo_finished += 1
        print("Number of Pomodoro finished {} / {}".format(pomo_finished, target_pomodoros))
    print('You have reached your goal! good job')
    playsound('assets/applause.mp3')
    askAdmin()
    user_choice = input()

print("goodbye!")