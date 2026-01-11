import random
import warnings
import sys
import time
tickets = []
randomincrement = 0
randomdecrement = 0
coins = 50
success = 0
fail = 0
streak = 0
successstatusbar = 0
successline = 0
failstatusbar = 0
failline = 0
streaklist = []
print(f"""\033[1;33mHow the game works:
1. You will be given a list of between 13-20 numbers which are randomly generated between 1-100.
2. You will be asked to enter a number.
3. If the number is in the list, you will gain anywhere between 95 - 135 coins.
4. If the number is not in the list, you will lose anywhere between 20 - 30 coins.
5. You start of with {coins} coins in your balance.
6. If you run out of coins you lose.
7. You can see Coimns Gained, Balance, Streak, and Gamber Mode (Success Rate).
\033[1;90m""")
if coins > 0:
    while True:
        for i in range (1, random.randint(13, 20)):
            tickets.append(random.randint(1, 100))
        print(tickets)
        choice = int(input("Enter ticket number:\n"))
        streaklist.append(streak)
        if choice in tickets:
            print(f"\033[1;32mGAMBER MODE!!!!!!!!!!!!!!")
            #time.sleep(0.1)
            #print("DOPAMINEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            #time.sleep(0.1)
            #print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
            #time.sleep(0.1)
            #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHH")
            #time.sleep(0.1)
            #print("GAMBEEEERRRRRRRRRRRR MMMMMMOOOOOOOOOODDDDDDDDDEEEEEEEEEEEEEEE")
            #time.sleep(0.15)
            #print(f"\033[1;35mall right thats enough\ngo again now")
            print('\033[0m')
            tickets.clear()
            randomincrement = random.randint(0, 1) #95 135
            coins += randomincrement
            success += 1
            streak += 1
            print(f"\033[1;32m{randomincrement} coins have been added to your balance. Your balance: {coins} coins.\n\nGamber Mode: {success/(success + fail)*100} %\nStreak: {streak}\033[1;90m")
        else:
            print(f"\033[1;31mloser\033[0m\ngo again")
            tickets.clear()
            randomdecrement = random.randint(20, 30)
            coins -= randomdecrement
            print(coins)
            fail += 1
            streak = 0
            print(f"\033[1;33m{randomdecrement} coins have been deducted from your balance.\nBalance: {coins} coins.\nGamber Mode: {success/(success + fail)*100} %\033[1;90m")
        if coins < 0:
            #Status Bar Functionality
            successline = int(str(success)[0])
            successstatusbar = "-" * successline
            #successLine = 10 - successline
            #successStatusBar = "-" * successLine

            failline = int(str(fail)[0])
            failstatusbar = "-" * failline
            #failLine = 10 - failline
            #failStatusBar = "-" * failLine
            
            #print(f"\n\n\n\n\033[1;36m\nGamber Mode: {success/(success + fail)*100} %\n\033[1;32mSuccesses: {success} [\033[1;32m{successstatusbar}\033[1;0m{successStatusBar}\033[1;90m] \033[1;90m|\033[1;33m Fails: {fail} [\033[1;33m{failstatusbar}\033[1;0m{failStatusBar}\033[1;90m]\n\n\033[1;35mHighest Streak: {max(streaklist)}")
            print(f'''\n\n\n\n\033[1;36m\nGamber Mode: {success/(success + fail)*100} %\n\033[1;32mSuccesses: {success} [\033[1;32m{successstatusbar}\033[1;0m{successStatusBar}\033[1;90m] \033[1;90m|\033[1;33m Fails: {fail} [\033[1;33m{failstatusbar}\033[1;0m{failStatusBar}\033[1;90m]\n\n\033[1;35mHighest Streak: {max(streaklist)}''')
            sys.exit("YOU HAVE LOST")
