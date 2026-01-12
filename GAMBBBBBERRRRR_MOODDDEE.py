import random
import sys
import math
import time
tickets = []
streaklist = []

history = []
greendash = "\033[1;32m—"
reddash = "\033[1;33m—"


randomincrement = 0
randomdecrement = 0

coins = random.randint(475, 525)

success = 0
fail = 0

streak = 0

successbar = 0
successpercent = 0

failbar = 0
failpercent = 0

gambermode = 0

print(f"""\033[1;33mHere;s how the game works:
1. You will be given a list of between 15-17 numbers which are randomly generated between 1-100.
2. You will be asked to enter a number.
3. If the number is in the list, you will gain anywhere between 65 - 80 coins.
4. If the number is not in the list, you will lose anywhere between 30- 40 coins.
5. You start of with {coins} coins in your balance.
6. If you run out of coins you lose.
7. After every round you can see your basic stats.
\033[1;90m""")
while True:
    if coins > 0:
            for _ in range (random.randint(15, 17)):
                tickets.append(random.randint(1, 100))
            #print(tickets)
            choice = int(input("Enter ticket number:\n"))
            streaklist.append(streak)
            if choice in tickets:
                print(f"\033[1;32mGAMBER MODE!!!!!!!!!!!!!!")
                time.sleep(0.1)
                print("DOPAMINEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                time.sleep(0.1)
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHH")
                time.sleep(0.15)
                print(f"\033[1;35mall right thats enough\ngo again now")
                print('\033[0m')
                tickets.clear()
                randomincrement = random.randint(65, 80)
                coins += randomincrement
                success += 1
                streak += 1
                history.append(greendash)
                gambermode = (success*100/(success + fail))
                print(f"\033[1;32m{randomincrement} coins have been added to your balance. Your balance: {coins} coins.\n\nGamber Mode: {round(gambermode, 2)} %\nStreak: {streak}\033[1;90m")
            else:
                print(f"\033[1;31mloser\033[0m\ngo again")
                tickets.clear()
                randomdecrement = random.randint(30, 40)
                coins -= randomdecrement
                fail += 1
                streak = 0
                history.append(reddash)
                gambermode = (success*100/(success + fail))
                print(f"\033[1;33m{randomdecrement} coins have been deducted from your balance.\nBalance: {coins} coins.\nGamber Mode: {round(gambermode, 2)} %\033[1;90m")
            
    else:
                gambermode = (success*100/(success + fail))
                #Status Bar Functionality
                successpercent = int(str(round(gambermode, -1))[0])
                successbar = "—" * successpercent
                #successLine = 10 - successline
                #successStatusBar = "-" * successLine

                failpercent = 10 - successpercent
                failbar = "—" * failpercent
                #failLine = 10 - failline
                #failStatusBar = "-" * failLine
                
                #print(f"\n\n\n\n\033[1;36m\nGamber Mode: {success/(success + fail)*100} %\n\033[1;32mSuccesses: {success} [\033[1;32m{successstatusbar}\033[1;0m{successStatusBar}\033[1;90m] \033[1;90m|\033[1;33m Fails: {fail} [\033[1;33m{failstatusbar}\033[1;0m{failStatusBar}\033[1;90m]\n\n\033[1;35mHighest Streak: {max(streaklist)}")
                
                print(f'''
                
                ------------YOU HAVE LOST------------

                \033[1;36mGamber Mode: {round(gambermode, 2)} % \033[1;90m[\033[1;32m{successbar}\033[1;33m{failbar}\033[1;90m]
                History : [{" ".join(history)}\033[91;0m]
                \033[1;32mSuccesses: {success} \033[1;90m|\033[1;33m Fails: {fail}
                \033[1;35mHighest Streak: {max(streaklist)}
                \033[1;33m
                ''')

                sys.exit('''

                YOU HAVE LOST

                ''')
