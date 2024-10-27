#convert to exe: pyinstaller --onefile game.py
import time
import sys
from colorama import Fore

def animate():
    
    sys.stdout.write('\rLoading |')
    time.sleep(0.1)
    sys.stdout.write('\rLoading /')
    time.sleep(0.1)
    sys.stdout.write('\rLoading -')
    time.sleep(0.1)
    sys.stdout.write('\rLoading \\')
    time.sleep(0.1)
    sys.stdout.write('\rLoading |')
    time.sleep(0.1)
    sys.stdout.write('\rLoading /')
    time.sleep(0.1)
    sys.stdout.write('\rLoading -')
    time.sleep(0.1)
    sys.stdout.write('\rLoading \\')
    time.sleep(0.1)
    sys.stdout.write('\rDone!     ')
    
def game():
    animate()
    print('       ')
    print(Fore.GREEN + '1 = Easy')
    print(Fore.YELLOW + '2 = Normal')
    print(Fore.RED + '3 = Hard')
    print(Fore.CYAN + '4 = Asian')
    print(Fore.WHITE + '5 = Chinese')
    print(Fore.MAGENTA + '6 = Emotional Damage')
    mode = input(Fore.WHITE + 'Select a difficulty: ')
    if mode == '1':
        print(Fore.RED + 'Failure')
        print('You died!')
        print(Fore.WHITE + 'RESTART')
        print('      ')
        time.sleep(2)
        game()
    
    if mode == '6':
        ans = input('Do you want to touch the tree?(Yes or No)')
        if ans == 'Yes':
            print(Fore.RED + 'Hit by tree')
            print('You died!')
            print(Fore.WHITE + 'RESTART')
            print('      ')
            time.sleep(2)
            game()
        if ans == 'No':
            ans = input("Do you want to hide behind the tree?(Yes or No)")
            if ans == 'No':
                print(Fore.GREEN + "Enemy says:uh.. headquarters? Yeah, there's an enemy right here!")
                time.sleep(3)
                print(Fore.RED + 'Enemy alerted')
                print('You died!')
                print(Fore.WHITE + 'RESTART')
                print('      ')
                time.sleep(2)
                game()
            if ans == 'Yes':
                ans = input("Hide more or less?(More or Less)")
                if ans == 'Less':
                    print("Enemy says:Uh... hq I think there's an enemy right there")
                    time.sleep(3)
                    print(Fore.RED + 'Enemy alerted')
                    print('You died!')
                    print(Fore.WHITE + 'RESTART')
                    print('      ')
                    time.sleep(2)
                    game()
                if ans == 'More':
                    print('Enemy says:you know ve really dumb if someone like just hide behind that tree,')
                    print("like if anyone hiding there he's gonna have like negative iq to hide behind that one specific tree,")
                    print("laying on the grass would have been a better disguise like you'd have to be so dumb you call people")
                    print("to ask their phone number, he's gonna be so dumb he makes the rayman look like james bond you know")
                    print("I wish somebody was behind that tree just so we can laughs ")
                    ans = input('Anything means getting your gun out')
                    print("'Make your dad proud'")
                    ans = input('Have you done it yet?(Yes or No)')
                    if ans == 'No':
                        time.sleep(1)
                        print(Fore.RED + 'You made your dad sad')
                        print('You died!')
                        print(Fore.WHITE + 'RESTART')
                        print('      ')
                        time.sleep(2)
                        game()
                    if ans == 'Yes':
                        ans = input("Fast or Slow?")
                        if ans == 'Slow': 
                            print("You hit the enemy")
                            print(Fore.RED + 'Enemy alerted')
                            print('You died!')
                            print(Fore.WHITE + 'RESTART')
                            print('      ')
                            time.sleep(2)
                            game()
                        if ans == "Fast":
                            print(Fore.RED + "Enemy killed!")
                            print('You WIN!!!!')
                            print('Signed by Steven he:S̷t̷e̷v̷e̷n̷H̷e̷')
                            
                    
                       
    if mode == '5':
        ans = input('Do you want to move? (Yes or No)')
        if ans == 'No':
            print(Fore.RED + '\rNeighbour"s kid did better')
            print('You died!')
            print(Fore.WHITE + 'RESTART')
            print('      ')
            time.sleep(2)
            game()
        if ans == 'Yes':
            print("Neighbour:The enemy is tough ahead, you're gonna have to heal up")
            time.sleep(1)
            print('For 10 coins, this potion will boost your attack power')
            ans = input('Do you want to buy?(Yes or No)')
            if ans == 'No':
                print(Fore.RED + 'Social Anxiety')
                print('You died!')
                print(Fore.WHITE + 'RESTART')
                print('      ')
                time.sleep(2)
                game() 
            if ans == 'Yes':
                ans = input('Are you sure? Yes = yes No = Go away')
                if ans == 'Yes':
                    print(Fore.RED + 'The game is finally helpful...')
                    time.sleep(1)  
                    print('     ')
                    print('NOT ENOUGH COINS') 
                    print('You died!')
                    print(Fore.WHITE + 'RESTART')
                    print('      ')
                    time.sleep(2)    
                    game()
                if ans == 'No':
                    print(Fore.RED + "Boss:NEIGHBOUR's Kid")
                    print("He says:Hey, haven't seen you since high school!")
                    print("Continues:Yeah, I just got back from collage")
                    ans = input('Type anything means Where?')
                    print('You asks:Oh, where did you go?')
                    print("Harvard")
                    ans = input("ask:you didn't go to med school, did you? (Yes or No)")
                    if ans == 'No':
                        print("Ultra Emotonal Damage")
                        print('You died!')
                        print(Fore.WHITE + 'RESTART')
                        print('      ')
                        time.sleep(2)
                        game()    
                    if ans == 'Yes':  
                        ans = input('Sure? Or say: I entertainted 20 million people and uh, 4 milllion of them enjoyed it enough to subscribe and follow')
                        if ans == 'Yes':
                            print("neighbour's kid:Nah nah nah, law school")
                            print('works for exposure') 
                            print('You died!')
                            print(Fore.WHITE + 'RESTART')
                            print('      ')
                            time.sleep(2)
                            game()
                        if ans == 'No':
                            print("Neighbour's kid asks you:You pay anything for that?") 
                            print('You say:This game is sponsored by Word')
                            print("Neighbour's kid takes a lot of damage")
                            print('you said:from Microsoft')
                            print("Neighbour's kid died")         
                            print('You WIN!!!!')
                            print('Signed by Steven he:S̷t̷e̷v̷e̷n̷H̷e̷')              
                            

    if mode == '4':
        print(Fore.CYAN + 'Asian')
        print(Fore.MAGENTA + '    ')
        animate()
        print('         ')
        print('What will you do if there is a leave dropping on you?')
        print(Fore.YELLOW + '1 = Walk away')
        print(Fore.GREEN + '2 = Block it with your hand')
        ans = input('')
        if ans == '1':
            print(Fore.RED + 'STEPPED ON BRANCH')
            print(Fore.RED + 'You died!')
            print(Fore.WHITE + 'RESTART')
            print('         ')
            time.sleep(2)
            game()
        if ans == '2':
            ans = input('Do you want to use +Block? (Yes or No)')
            if ans == 'No':
                ans = input('Do you want to block the sun? (Yes or No)')
                if ans == 'No':
                    print(Fore.RED + 'HIT BY LEAVE')
                    time.sleep(0.1)
                    print(Fore.RED + 'Ask:WAS IT POISONOUS?')
                    print(Fore.RED + 'No. Just Regular Leaf')
                    print(Fore.RED + 'You Died!')
                    print(Fore.WHITE + 'RESTART')
                    print('          ')
                    time.sleep(2)
                    game()   
                if ans == 'Yes':
                    print('Say:Finally, some action')
                    time.sleep(0.3)
                    print(Fore.CYAN + 'Boss:Aunty with 1,500,000 health asks you:Steven, when you get so fat?')
                    ans = input('Do you want to use +Block?')
                    if ans == 'No':
                        print(Fore.RED + 'Emotional Damage')
                        print(Fore.RED + 'You Died!')
                        print(Fore.WHITE + 'RESTART')
                        print('          ')
                        time.sleep(2)
                        game()    
                    if ans == 'Yes':
                        print(Fore.CYAN + 'Boss:Aunty with 1,500,000 health asks you:You still try being a actor?')
                        print(Fore.RED + 'Unemployment')
                        print(Fore.RED + 'You Died!')
                        print(Fore.WHITE + 'RESTART')
                        print('          ')
                        time.sleep(2)
                        game() 
            if ans == 'Yes':
                print(Fore.RED + 'Tanned Too Hard')   
                print(Fore.RED + 'You Died!')
                print(Fore.WHITE + 'RESTART')
                print('          ')
                time.sleep(2)
                game()         
            
game()
        